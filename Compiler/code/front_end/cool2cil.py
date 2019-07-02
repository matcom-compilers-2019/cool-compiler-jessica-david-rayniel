from collections import OrderedDict
from code.front_end import cil_ast
from typing import List, Optional, Tuple, Dict
from code.utils import visitor, cil_scoper
from code.utils.cil_scoper import CilScope
from code.front_end.semantic_checker_utils import *
from code.front_end import our_ast
import code.front_end.semantic_checker as semantic_checker
from code.back_end.cil2mips import MipsGenerator


class BaseCOOLToCILVisitor:
    def __init__(self, type_graph: 'TypesGraph'):
        self.dottypes = []
        self.dotdata = []
        self.dotcode = []
        self.current_type: Classbook = None
        self.current_method: tuple = None
        self.current_function: cil_ast.FunctionNode = None
        self.type_graph = type_graph

    @property
    def params(self):
        return self.current_function.params

    @property
    def localvars(self):
        return self.current_function.localvars

    @property
    def instructions(self):
        return self.current_function.instructions

    def register_param(self, vinfo: VariableInfo) -> str:
        vinfo.name = f'param_{self.current_function.fname}_{vinfo.name}_{len(self.params)}'
        param_node = cil_ast.ParamNode(vinfo.name)
        self.params.append(param_node)
        return vinfo.name

    def register_local(self, vinfo: VariableInfo) -> str:
        vinfo.name = f'local_{self.current_function.fname}_{vinfo.name}_{len(self.localvars)}'
        local_node = cil_ast.LocalNode(vinfo.name)
        self.localvars.append(local_node)
        return vinfo.name

    def define_internal_local(self) -> str:
        vinfo = VariableInfo('internal', None)
        return self.register_local(vinfo)

    def register_instruction(self, instruction: cil_ast.InstructionNode) -> \
            cil_ast.InstructionNode:
        self.instructions.append(instruction)
        return instruction

    def to_function_name(self, method_name: str, type_name: str) -> str:
        return f'function_{method_name}_at_{type_name}'

    def to_attr_name(self, type_name, attr_name):
        '''

        :param type_name: last type in redefining it
        :type type_name: str
        :param attr_name: attr name
        :type attr_name: str
        :return: attr name in cil
        :rtype: str
        '''
        return f'{type_name}_{attr_name}'

    def register_function(self, function_name: str) -> cil_ast.FunctionNode:
        function_node = cil_ast.FunctionNode(function_name, [], [], [])
        self.dotcode.append(function_node)
        return function_node

    def register_type(self, name: str) -> cil_ast.TypeNode:
        type_node = cil_ast.TypeNode(name, [], [])
        self.dottypes.append(type_node)
        return type_node

    def register_data(self, value: str) -> cil_ast.DataNode:
        vname = f'data_{len(self.dotdata)}'
        data_node = cil_ast.DataNode(vname, value)
        self.dotdata.append(data_node)
        return data_node


class COOLToCILVisitor(BaseCOOLToCILVisitor):

    def __init__(self, type_graph: 'TypesGraph', program: our_ast.ProgramNode):
        super().__init__(type_graph)
        self.disptch_static_counter = 0
        self.case_counter = 0
        self.not_counter = 0
        self.equal_counter = 0
        self.less_than_node_counter = 0
        self.if_counter = 0
        self.while_counter = 0
        self.less_or_equal_counter = 0
        self.is_void_counter = 0
        self.types = Types(type_graph)
        self.types.get_attrs()
        self.types.get_methods()
        self.number = 0

        scope = CilScope()
        self.result = self.visit(program, scope)

    def give_unic_label(self, comment = "unique"):
        self.number +=1
        result = "label_de_cil_" + str(comment) + str(self.number)
        return result

    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(our_ast.ProgramNode)
    def visit(self, node: our_ast.ProgramNode, scope: 'CilScope'):
        ######################################################
        # node.classes -> [ ClassNode ... ]
        ######################################################
        self._create_object_type()
        self._create_io_type()
        self._do_abort()
        self._do_copy()
        self._do_type_name()

        self._do_concat_func()
        self._do_length_func()
        self._do_substr_func()

        self._do_in_int()
        self._do_in_string()
        self._do_out_int()
        self._do_out_string()

        self._do_equals_string()
        self._do_attr_con_IO()
        self._do_attr_Object()
        self._do_met_con_Object()
        self._do_met_con_IO()

        for clas in node.classes:
            self.visit(clas, scope.create_child())

        self.current_function = self.register_function('main')

        instance = self.define_internal_local()
        vtable = self.define_internal_local()
        vtable_ed = self.define_internal_local()
        instance_ed = self.define_internal_local()
        result = self.define_internal_local()

        attr_count = 0
        methods_count = 0
        for type in self.dottypes:
            if type.tname == 'Main':
                attr_count = len(type.attrs)
                methods_count = len(type.methods)
                break

        self.register_instruction(cil_ast.AllocateNode(instance, attr_count))

        self.register_instruction(
            cil_ast.StaticCallNode(instance_ed,
                                   self.to_function_name('_attr_con',
                                                         'Main'),
                                   [instance]))
        self.register_instruction(cil_ast.AllocateNode(vtable, methods_count))

        self.register_instruction(
            cil_ast.StaticCallNode(vtable_ed,
                                   self.to_function_name('_method_con',
                                                         'Main'),
                                   [vtable]))
        self.register_instruction(cil_ast.SetAttrNode(vtable_ed, instance_ed,
                                                      1, 'Main'))
        self.register_instruction(
            cil_ast.DinamicCallNode(result, 'Main', 'main', instance,
                                    [instance]))
        self.register_instruction(cil_ast.ReturnNode(0))

        self.current_function = None

        entry = self.dotcode.pop()
        self.dotcode = [entry] + self.dotcode

        return cil_ast.ProgramNode(self.dottypes, self.dotdata, self.dotcode)

    @visitor.when(our_ast.ClassNode)
    def visit(self, node: our_ast.ClassNode, scope: CilScope):
        ####################################################################
        # node.name -> str
        # node.parent -> str
        # node.attrs -> [ AttrNode ... ]
        # node.methods -> [ MethodNode ... ]
        ####################################################################
        # nombre del attr: {nombre del tipo}_{nombre del attr}
        # nombre de la funcion: function_{method_name}_at_{type_name}'
        # nombre del methodo:
        # {ultimo tipo que lo redefine}_{nombre del methodo}_{funcion a la que hace ref}
        self.current_type = self.type_graph.types_nodes[node.name]
        # Your code here!!! (Handle all the .TYPE section)
        type_node: cil_ast.TypeNode = self.register_type(node.name)

        type_node.attrs.append(cil_ast.AttrNode('_name'))
        type_node.attrs.append(cil_ast.AttrNode('_vtable'))
        type_node.attrs.append(cil_ast.AttrNode('_begin'))
        type_node.attrs.append(cil_ast.AttrNode('_len'))

        for attr, _ in self.current_type.all_attributes(clean=False).items():
            tipe = self.current_type.find_attr(attr, internal=True)
            type_node.attrs.append(cil_ast.AttrNode(self.to_attr_name(tipe[1], attr)))

            scope.define_variable(attr, self.to_attr_name(tipe[1], attr))
        # todo llamara a alguien para ver quien hizo los numeros negativos en mips
        for method, _ in self.current_type.all_methods(clean=False).items():
            tipe = self.current_type.find_method(method, internal=True)
            type_node.methods.append(
                cil_ast.MethodNode(method, self.to_function_name(method,
                                                                   tipe[1])))

        # se crea el constructor de attr
        self.current_method = (('return', node.name,),)

        self.current_function = self.register_function(self.to_function_name(
            '_attr_con', node.name))

        self_param = self.register_param(VariableInfo('self', self.current_type))
        # todo dividir entre 0 en la parte de la division lanzar except
        temp = self.define_internal_local()
        begin = self.register_local(VariableInfo('begin'))
        length = self.register_local(VariableInfo('len'))
        name = self.register_local(VariableInfo('name'))
        #print("*************************************************************************************************************************************")
        #print(str(self.current_type.name) + " : "+str(self.current_type.parent.name))
        #print("*************************************************************************************************************************************")

        r_name = self.register_data("\"" +node.name + "\"").vname #Aqui registro el nombre de la clase y me quedo con el nombre que se el dio en la punto data para poder setiarlo

        self.register_instruction(
            cil_ast.StaticCallNode(
                temp, self.to_function_name('_attr_con',
                                              self.current_type.parent.name), [self_param]))
        self.register_instruction(cil_ast.AssignNode(self_param, temp))
        var = None
        attr: our_ast.AttrNode
        for attr in node.attrs:
            child_scope = scope.create_child()

            var = self.visit(attr, child_scope)
            self.register_instruction(cil_ast.SetAttrNode(var, self_param,
                                    self.types.attrs[node.name][attr.name],
                                    node.name))
        self.register_instruction(
            cil_ast.AssignNode(begin, self.type_graph.types_nodes[node.name].begin))
        self.register_instruction(cil_ast.AssignNode(length, len(node.attrs)))

        self.register_instruction(cil_ast.SetAttrNode(begin, self_param, 2))
        self.register_instruction(cil_ast.SetAttrNode(length, self_param, 3))
        self.register_instruction(cil_ast.SetAttrNode(r_name,self_param,0))
        self.register_instruction(cil_ast.ReturnNode(self_param))
        # todo falta setear el name
        self.current_function = None
        self.current_method = None
        #############################
        # creando el constuctor de methodos

        self.current_function = self.register_function(self.to_function_name(
            '_method_con', node.name))

        vtable = self.register_param(VariableInfo('_vtable', node.name))

        for method in type_node.methods:
            self.register_instruction(
                cil_ast.SuperSetAttrNode(vtable, method.name, method.fundest,
                                         node.name))
        self.register_instruction(cil_ast.ReturnNode(vtable))
        self.current_function = None
        self.current_method = None
        #############################
        for method in node.methods:
            child_scope = scope.create_child()
            self.visit(method, child_scope)

        self.current_type = None

    @visitor.when(our_ast.MethodNode)
    def visit(self, node: our_ast.MethodNode, scope: CilScope):
        ###############################
        # node.name -> str
        # node.params -> [ ParamNode ... ]
        # node.return_type -> str
        # node.body -> [ ExprNode ... ]
        ###############################
        self.current_method = self.current_type.find_method(node.name,
                                                            internal=True)
        # Your code here!!! (Handle PARAMS)
        self.current_function = self.register_function(
            self.to_function_name(node.name, self.current_type.name))

        self_param = self.register_param(VariableInfo('self', self.current_type.name))
        scope.define_variable('self', self_param)
        for param_node in node.params:
            param_cil_name = self.register_param(
                VariableInfo(param_node.name, param_node.type))
            scope.define_variable(param_node.name, param_cil_name)
        ##################################################################
        value = self.visit(node.body, scope)
        # Your code here!!! (Handle RETURN)
        self.register_instruction(cil_ast.ReturnNode(value))

        self.current_function = None
        self.current_method = None

    @visitor.when(our_ast.IdNode)
    def visit(self, node: our_ast.IdNode, scope: CilScope):
        ###############################
        # node.name -> str
        ###############################
        # Your code here!!!

        if scope.locals[node.name].split('_')[0] in self.type_graph.types_nodes.keys():
            result = self.define_internal_local()
            self.register_instruction(cil_ast.GetAttrNode(result, scope.locals['self'],
                  self.types.attrs[self.current_type.name][node.name], node.static))

            return result

        return scope.locals[node.name]
        #################################################################

    @visitor.when(our_ast.AssigNode)
    def visit(self, node, scope: CilScope):
        ###############################
        # node.name -> str
        # node.value -> ExprNode
        ###############################
        # Your code here!!!
        value: str = self.visit(node.value, scope)
        # se verifican que sean attr de la clase para usar otras instrucciones
        if value.split('_')[0] in self.type_graph.types_nodes.keys():
            if scope.locals[node.name].split('_')[0] in \
                    self.type_graph.types_nodes.keys():
                temp = self.define_internal_local()
                self.register_instruction(
                    cil_ast.GetAttrNode(temp, scope.locals['self'],
                            self.types.attrs[self.current_type.name][value.split('_')[1]],
                                        node.value.static))
                self.register_instruction(
                    cil_ast.SetAttrNode(temp, scope.locals['self'],
                                        self.types.attrs[self.current_type.name][node.name],
                                        node.value.static))
            else:
                self.register_instruction(
                    cil_ast.GetAttrNode(scope.locals[node.name], scope.locals['self'],
                        self.types.attrs[self.current_type.name][value.split('_')[1]],
                                        node.value.static))
        else:
            if scope.locals[node.name].split('_')[0] in \
                    self.type_graph.types_nodes.keys():
                self.register_instruction(cil_ast.SetAttrNode(value, scope.locals['self'],
                                        self.types.attrs[self.current_type.name][node.name],
                                        node.value.static))
            else:
                self.register_instruction(cil_ast.AssignNode(
                    scope.locals[node.name], value))
        return scope.locals[node.name]
        ########################################################

    @visitor.when(our_ast.ConstantNode)
    def visit(self, node, scope):
        ###############################
        # node.value -> str | bool | int
        ###############################

        # Your code here!!! (Pretty easy ;-))
        temp = self.define_internal_local()

        if isinstance(node, our_ast.StringNode):
            data_name = self.register_data(node.value).vname
            self.register_instruction(cil_ast.LoadNode(temp, data_name))
        elif isinstance(node, our_ast.BoolNode):
            if node.value:
                self.register_instruction(cil_ast.AssignNode(temp, 1))
            else: self.register_instruction(cil_ast.AssignNode(temp, 0))

        elif isinstance(node, our_ast.IntegerNode):
            self.register_instruction(cil_ast.AssignNode(temp, node.value))

        return temp
        ####################################

    @visitor.when(our_ast.PlusNode)
    def visit(self, node, scope):
        ###############################
        # node.left -> ExpressionNode
        # node.right -> ExpressionNode
        ###############################

        # Your code here!!!
        lvalue = self.visit(node.lvalue, scope)
        rvalue = self.visit(node.rvalue, scope)

        temp = self.define_internal_local()
        self.register_instruction(cil_ast.PlusNode(temp, lvalue, rvalue))

        return temp
        #################################################################

    @visitor.when(our_ast.MinusNode)
    def visit(self, node, scope):
        ###############################
        # node.left -> ExpressionNode
        # node.right -> ExpressionNode
        ###############################

        # Your code here!!!
        lvalue = self.visit(node.lvalue, scope)
        rvalue = self.visit(node.rvalue, scope)

        temp = self.define_internal_local()
        self.register_instruction(cil_ast.MinusNode(temp, lvalue, rvalue))

        return temp
        ###################################################################

    @visitor.when(our_ast.StarNode)
    def visit(self, node, scope):
        ###############################
        # node.left -> ExpressionNode
        # node.right -> ExpressionNode
        ###############################

        # Your code here!!!
        lvalue = self.visit(node.lvalue, scope)
        rvalue = self.visit(node.rvalue, scope)

        temp = self.define_internal_local()
        self.register_instruction(cil_ast.StarNode(temp, lvalue, rvalue))

        return temp
        ####################################################################

    @visitor.when(our_ast.DivNode)
    def visit(self, node, scope):
        ###############################
        # node.left -> ExpressionNode
        # node.right -> ExpressionNode
        ###############################

        # Your code here!!!
        lvalue = self.visit(node.lvalue, scope)
        rvalue = self.visit(node.rvalue, scope)

        temp = self.define_internal_local()
        self.register_instruction(cil_ast.DivNode(temp, lvalue, rvalue))

        return temp
        #####################################################################

    @visitor.when(our_ast.IfNode)
    def visit(self, node: our_ast.IfNode, scope):
        result = self.define_internal_local()
        cond_var = self.visit(node.condition, scope)

        after = cil_ast.LabelNode(f'after_{self.if_counter}'+self.give_unic_label())
        endif = cil_ast.LabelNode(f'endif_{self.if_counter}'+self.give_unic_label())

        self.if_counter += 1

        self.register_instruction(cil_ast.IfNode(cond_var, after))

        fbody_value = self.visit(node.false_body, scope)
        self.register_instruction(cil_ast.AssignNode(result, fbody_value))

        self.register_instruction(cil_ast.GotoNode(endif))
        self.register_instruction(after)

        tbody_value = self.visit(node.true_body, scope)
        self.register_instruction(cil_ast.AssignNode(result, tbody_value))

        self.register_instruction(endif)

        return result

    @visitor.when(our_ast.WhileNode)
    def visit(self, node: our_ast.WhileNode, scope):

        cont = cil_ast.LabelNode(f'continue_{self.while_counter}'+self.give_unic_label())
        loop = cil_ast.LabelNode(f'loop_{self.while_counter}'+self.give_unic_label())
        endloop = cil_ast.LabelNode(f'endloop_{self.while_counter}'+self.give_unic_label())

        self.while_counter += 1

        temp = self.visit(node.condition, scope)

        self.register_instruction(cil_ast.IfNode(temp, loop))
        self.register_instruction(cil_ast.GotoNode(endloop))
        self.register_instruction(loop)

        self.visit(node.body, scope)

        self.register_instruction(cil_ast.GotoNode(cont))

        self.register_instruction(endloop)
        temp1 = self.define_internal_local()
        temp2 = self.define_internal_local()
        self.register_instruction(cil_ast.AllocateNode(temp1, 3))
        self.register_instruction(cil_ast.AssignNode(temp2, 0))
        self.register_instruction(cil_ast.SetAttrNode(temp2, temp1, 2))

        return temp1

    @visitor.when(our_ast.DispatchSelfNode)
    def visit(self, node: our_ast.DispatchSelfNode, scope):
        args_list = [scope.locals['self']]

        for expr in node.args:
            args_list.append(self.visit(expr, scope))

        temp = self.define_internal_local()
        self.register_instruction(
            cil_ast.DinamicCallNode(temp, self.current_type.name, node.name,
            scope.locals['self'], args_list))

        return temp


    @visitor.when(our_ast.DispatchStaticNode)
    def visit(self, node: our_ast.DispatchStaticNode, scope):
        self.disptch_static_counter += 1

        result = self.define_internal_local()
        begin_cond = self.define_internal_local()
        cond = self.define_internal_local()
        constant = self.define_internal_local()

        is_void = cil_ast.LabelNode(f'is_void{self.disptch_static_counter}'+self.give_unic_label())
        end_if = cil_ast.LabelNode(f'end_dispatch{self.disptch_static_counter}'+self.give_unic_label())

        args_list = []

        for expr in node.args:
            args_list.append(self.visit(expr, scope))

        expr_var = self.visit(node.expr, scope)
        args_list = [expr_var] + args_list

        if node.expr.static in ('Int', 'Bool', 'String'):
            self.register_instruction(
                cil_ast.StaticCallNode(result, self.to_function_name(node.name,
                                       node.expr.static), args_list))
        else:
            self.register_instruction(cil_ast.GetAttrNode(
                begin_cond, expr_var, 2, node.expr.static))
            self.register_instruction(cil_ast.AssignNode(constant, 0))
            self.register_instruction(cil_ast.EqualNode(cond, begin_cond, constant))
            self.register_instruction(cil_ast.IfNode(cond, is_void))
            self.register_instruction(cil_ast.GotoNode(end_if))
            self.register_instruction(is_void)
            self.register_instruction(cil_ast.ExceptNode())
            self.register_instruction(end_if)

            self.register_instruction(
                cil_ast.DinamicCallNode(
                    result, node.expr.static, node.name, expr_var, args_list))
        return result

    @visitor.when(our_ast.DispatchInheritsNode)
    def visit(self, node: our_ast.DispatchInheritsNode, scope):
        variables = []

        for expr in node.args:
            variables.append(self.visit(expr, scope))

        expr_var = self.visit(node.expr, scope)
        variables = [expr_var] + variables

        is_void = self.define_internal_local()
        const = self.define_internal_local()
        begin = self.define_internal_local()
        temp = self.define_internal_local()

        cont = cil_ast.LabelNode('continue'+self.give_unic_label())
        end = cil_ast.LabelNode('end'+self.give_unic_label())

        # if expr_var.static in ('Int', 'String', 'Bool'):
        #     self.register_instruction(cil_ast.ArgNode(expr_var))
        #     for var in variables:
        #         self.register_instruction(cil_ast.ArgNode(var))
        #     self.register_instruction(
        #         cil_ast.StaticCallNode(temp, self.to_function_name(node.name, )

        self.register_instruction(cil_ast.AssignNode(const, 0))
        self.register_instruction(cil_ast.GetAttrNode(begin, expr_var, 2))
        self.register_instruction(cil_ast.EqualNode(is_void, begin, const))

        self.register_instruction(cil_ast.IfNode(is_void, cont))
        self.register_instruction(cil_ast.GotoNode(end))
        self.register_instruction(cont)
        self.register_instruction(cil_ast.ExceptNode())
        self.register_instruction(end)

        self.register_instruction(
            cil_ast.DinamicCallNode(temp, node.type, node.name, expr_var,
                                    variables))
        return temp

    @visitor.when(our_ast.BlockNode)
    def visit(self, node: our_ast.BlockNode, scope):
        var = None
        for var in node.body:
            var = self.visit(var, scope)
        temp = self.define_internal_local()

        self.register_instruction(cil_ast.AssignNode(temp, var))

        return temp

    @visitor.when(our_ast.NewNode)
    def visit(self, node: our_ast.NewNode, scope):
        instance = self.define_internal_local()
        vtable = self.define_internal_local()
        vtable_ed = self.define_internal_local()
        instance_ed = self.define_internal_local()

        if node.type in ('Int', 'Bool',):
            self.register_instruction(cil_ast.AssignNode(instance_ed, 0))

        elif node.type == 'String':
            data = self.register_data('').vname
            self.register_instruction(cil_ast.LoadNode(instance_ed, data))

        else:
            type: cil_ast.TypeNode
            attr_count = 0
            methods_count = 0
            for type in self.dottypes:
                if type.tname == node.type:
                    attr_count = len(type.attrs)
                    methods_count = len(type.methods)
                    break

            self.register_instruction(cil_ast.AllocateNode(instance, attr_count))

            self.register_instruction(
                cil_ast.StaticCallNode(instance_ed, self.to_function_name('_attr_con',
                                                                    node.type), [instance]))
            self.register_instruction(cil_ast.AllocateNode(vtable, methods_count))

            self.register_instruction(
                cil_ast.StaticCallNode(vtable_ed,
                                       self.to_function_name('_method_con', node.type),
                                       [vtable]))
            self.register_instruction(cil_ast.SetAttrNode(vtable_ed, instance_ed,
                                                            1, node.type))
        return instance_ed

    @visitor.when(our_ast.LessThanNode)
    def visit(self, node: our_ast.LessThanNode, scope):
        lvar = self.visit(node.lvalue, scope)
        rvar = self.visit(node.rvalue, scope)

        temp_result = self.define_internal_local()
        self.register_instruction(cil_ast.LessThanNode(temp_result, lvar, rvar))

        return temp_result

    @visitor.when(our_ast.EqualNode)
    def visit(self, node: our_ast.EqualNode, scope):
        lvar = self.visit(node.lvalue, scope)
        rvar = self.visit(node.rvalue, scope)
        temp_result = self.define_internal_local()

        if node.rvalue.static == 'String':
            self.register_instruction(
                cil_ast.StaticCallNode(
                    temp_result, self.to_function_name('equals_string', 'String'),
                [lvar, rvar]))
        else:
            self.register_instruction(cil_ast.EqualNode(temp_result, lvar, rvar))

        return temp_result

    @visitor.when(our_ast.LessOrEqualNode)
    def visit(self, node: our_ast.LessOrEqualNode, scope):

        lvar = self.visit(node.lvalue, scope)
        rvar = self.visit(node.rvalue, scope)

        temp_result = self.define_internal_local()
        self.register_instruction(cil_ast.LessOrEqualThanNode(temp_result, lvar,
                                                              rvar))
        return temp_result
    # todo scope nuevo en clase, metodo, lets, branch
    # todo branch, params, let,
    @visitor.when(our_ast.NotNode)
    def visit(self, node: our_ast.NotNode, scope):

        expr = self.visit(node.value, scope)
        temp_result = self.define_internal_local()
        self.register_instruction(cil_ast.NotNode(temp_result, expr))

        return temp_result

    @visitor.when(our_ast.AttrNode)
    def visit(self, node: our_ast.AttrNode, scope: CilScope):
        local = self.register_local(VariableInfo(node.name, node.type))

        if not node.value:
            if node.type == 'Int':
                self.register_instruction(cil_ast.AssignNode(local, 0))
            elif node.type == 'String':
                data = self.register_data('').vname
                self.register_instruction(cil_ast.LoadNode(local, data))
            elif node.type == 'Bool':
                self.register_instruction(cil_ast.AssignNode(local, 0))
            else:
                const = self.define_internal_local()
                self.register_instruction(cil_ast.AllocateNode(local, 4))
                self.register_instruction(cil_ast.AssignNode(const, 0))
                self.register_instruction(cil_ast.SetAttrNode(const, local, 2))
        else:
            var = self.visit(node.value, scope)
            scope.define_variable(node.name, local)
            self.register_instruction(cil_ast.AssignNode(local, var))

        return local

    @visitor.when(our_ast.IsVoidNode)
    def visit(self, node: our_ast.IsVoidNode, scope):
        var = self.visit(node.expr, scope)

        begin_value = self.define_internal_local()
        temp2 = self.define_internal_local()
        const = self.define_internal_local()

        temp_result = self.define_internal_local()

        self.register_instruction(cil_ast.GetAttrNode(begin_value, var, 2,
                                                      node.expr.static))
        self.register_instruction(cil_ast.AssignNode(const, 0))
        self.register_instruction(cil_ast.EqualNode(temp2, begin_value, const))
        is_void_cond = cil_ast.LabelNode('is_void'+self.give_unic_label()) # todo ver que el label sea unico
        end = cil_ast.LabelNode('end'+self.give_unic_label())
        self.register_instruction(cil_ast.IfNode(temp2, is_void_cond))
        self.register_instruction(cil_ast.AssignNode(temp_result, 0))
        self.register_instruction(cil_ast.GotoNode(end))
        self.register_instruction(is_void_cond)
        self.register_instruction(cil_ast.AssignNode(temp_result, 1))
        self.register_instruction(end)
        # si el begin es 0 para los void entonces basta con hacerle not
        return temp_result

    @visitor.when(our_ast.NegationNode)
    def visit(self, node: our_ast.NegationNode, scope):

        var = self.visit(node.value, scope)

        temp_result = self.define_internal_local()

        self.register_instruction(cil_ast.NegationNode(temp_result, var))

        return temp_result

    @visitor.when(our_ast.SelfNode)
    def visit(self, node: our_ast.SelfNode, scope: CilScope):
        return scope.locals['self']

    @visitor.when(our_ast.LetNode)
    def visit(self, node: our_ast.LetNode, scope: cil_scoper.CilScope):

        child_scope = scope.create_child()
        attr: our_ast.AttrNode
        for attr in node.initializers:
            var = self.visit(attr, child_scope)

        temp_result = self.visit(node.body, child_scope)

        return temp_result

    @visitor.when(our_ast.CaseNode)
    def visit(self, node: our_ast.CaseNode, scope: CilScope):
        self.case_counter += 1
        var = self.visit(node.condition, scope)
        branch: our_ast.BranchNode

        node.branches = list(node.branches)

        node.branches.sort(key=lambda branch:
            self.type_graph.types_nodes[branch.type].deph)

        result = self.define_internal_local()
        cond_begin = self.define_internal_local()

        if node.condition.static in ('Int', 'String', 'Bool'):
            self.register_instruction(
                cil_ast.AssignNode(
                    cond_begin, self.type_graph.types_nodes[node.condition.static.name].begin))
        else:
            self.register_instruction(cil_ast.GetAttrNode(cond_begin, var, 2,
                                                      node.condition.static))
        vars = []
        for branch in node.branches:
            lvar = self.define_internal_local()
            rvar = self.define_internal_local()
            cond = self.define_internal_local()
            vars.append(cond)
            self.register_instruction(
                cil_ast.GreatherOrEqualThanNode(
                    lvar, cond_begin, self.type_graph.types_nodes[branch.type].begin))
            self.register_instruction(
                cil_ast.LessOrEqualThanNode(
                    rvar, cond_begin, self.type_graph.types_nodes[branch.type].end))
            self.register_instruction(cil_ast.AndNode(cond, lvar, rvar))

        end_case = cil_ast.LabelNode(f'end_case{self.case_counter}'+self.give_unic_label())

        for branch, index, cond in zip(node.branches, range(len(vars)), vars):
            branch_label = cil_ast.LabelNode(f'branch{index}_{self.case_counter}'+self.give_unic_label())
            next_label = cil_ast.LabelNode(f'next{index}_{self.case_counter}'+self.give_unic_label())

            self.register_instruction(cil_ast.IfNode(cond, branch_label))
            self.register_instruction(cil_ast.GotoNode(next_label))
            self.register_instruction(branch_label)

            branch_var = self.register_local(VariableInfo(branch.name, branch.type))
            scope.define_variable(branch.name, branch_var)

            self.register_instruction(cil_ast.AssignNode(branch_var, var))

            expr_value = self.visit(branch.expr, scope)
            self.register_instruction(cil_ast.AssignNode(result, expr_value))
            self.register_instruction(cil_ast.GotoNode(end_case))
            self.register_instruction(next_label)

        self.register_instruction(cil_ast.ExceptNode())
        self.register_instruction(end_case)

        return result

    def _do_substr_func(self):
        self.current_function = self.register_function(
            self.to_function_name('substr', 'String'))

        string = self.register_param(VariableInfo('self'))
        index = self.register_param(VariableInfo('index'))
        length = self.register_param(VariableInfo('length'))

        cond1 = self.register_local(VariableInfo('cond1'))
        cond2 = self.register_local(VariableInfo('cond2'))
        cond3 = self.register_local(VariableInfo('cond3'))
        length_string = self.register_local(VariableInfo('length_string'))
        second_index = self.register_local(VariableInfo('second_index'))
        substr = self.register_local(VariableInfo('substr'))
        actual_char = self.register_local(VariableInfo('actual_char'))
        other_index = self.register_local(VariableInfo('other_index'))
        temp_index = self.register_local(VariableInfo('temp_index'))
        temp_other_index = self.register_local(VariableInfo('temp_other_index'))
        const0 = self.define_internal_local()
        const1 = self.define_internal_local()

        end = cil_ast.LabelNode('end'+self.give_unic_label())
        error1 = cil_ast.LabelNode('error1'+self.give_unic_label())
        error2 = cil_ast.LabelNode('error2'+self.give_unic_label())
        cont1 = cil_ast.LabelNode('continue1'+self.give_unic_label())
        cont2 = cil_ast.LabelNode('continue2'+self.give_unic_label())
        cont = cil_ast.LabelNode('continue'+self.give_unic_label())

        self.register_instruction(cil_ast.AssignNode(other_index, 0))

        self.register_instruction(
            cil_ast.StaticCallNode(length_string,
                                   self.to_function_name('length', 'String'), [string]))

        self.register_instruction(cil_ast.PlusNode(second_index, index, length))
        self.register_instruction(cil_ast.AssignNode(const0, 0))
        self.register_instruction(cil_ast.LessThanNode(cond1, index, const0))
        self.register_instruction(cil_ast.GreatherThanNode(cond2, second_index,
                                                           length))
        self.register_instruction(cil_ast.IfNode(cond1, error1))
        self.register_instruction(cil_ast.GotoNode(cont1))
        self.register_instruction(error1)
        self.register_instruction(cil_ast.ExceptNode())
        self.register_instruction(cont1)
        self.register_instruction(cil_ast.IfNode(cond2, error2))
        self.register_instruction(cil_ast.GotoNode(cont2))
        self.register_instruction(error2)
        self.register_instruction(cil_ast.ExceptNode())
        self.register_instruction(cont2)
        self.register_instruction(cil_ast.ArrayNode(substr, length))
        self.register_instruction(cont)
        self.register_instruction(cil_ast.GetIndexNode(actual_char, string, index))
        self.register_instruction(cil_ast.SetIndexNode(actual_char, substr, other_index))
        self.register_instruction(cil_ast.GreatherOrEqualThanNode(cond3, other_index, length))
        self.register_instruction(cil_ast.IfNode(cond3, end))
        self.register_instruction(cil_ast.AssignNode(temp_index, index))
        self.register_instruction(cil_ast.AssignNode(temp_other_index, other_index))
        self.register_instruction(cil_ast.AssignNode(const1, 1))
        self.register_instruction(cil_ast.PlusNode(other_index, temp_other_index, const1))
        self.register_instruction(cil_ast.PlusNode(index, temp_index, const1))
        self.register_instruction(cil_ast.GotoNode(cont))
        self.register_instruction(end)

        self.register_instruction(cil_ast.ReturnNode(substr))

        self.current_function = None

    def _do_length_func(self):
        self.current_function = self.register_function(
            self.to_function_name('length', 'String'))

        string= self.register_param(VariableInfo('string', 'String'))

        length = self.register_local(VariableInfo('length'))
        actual_char = self.register_local(VariableInfo('actual_char'))
        index = self.register_local(VariableInfo('index'))
        cond = self.register_local(VariableInfo('cond'))
        temp1 = self.define_internal_local()
        temp_index = self.register_local(VariableInfo('temp_index'))
        temp_length = self.register_local(VariableInfo('temp_length'))
        const = self.define_internal_local()

        end = cil_ast.LabelNode('end'+self.give_unic_label())
        cont = cil_ast.LabelNode('continue'+self.give_unic_label())

        self.register_instruction(cil_ast.AssignNode(length, 0))
        self.register_instruction(cont)
        self.register_instruction(cil_ast.GetAttrNode(actual_char, string, index, 'String'))
        self.register_instruction(cil_ast.AssignNode(temp1, 0))
        self.register_instruction(cil_ast.EqualNode(cond, actual_char, temp1))
        self.register_instruction(cil_ast.IfNode(cond, end))
        self.register_instruction(cil_ast.AssignNode(temp_length, length))
        self.register_instruction(cil_ast.AssignNode(const, 1))
        self.register_instruction(cil_ast.PlusNode(length, temp_length, const))
        self.register_instruction(cil_ast.AssignNode(temp_index, index))
        self.register_instruction(cil_ast.PlusNode(index, temp_index, const))
        self.register_instruction(cil_ast.GotoNode(cont))
        self.register_instruction(end)
        self.register_instruction(cil_ast.ReturnNode(length))

        self.current_function = None

    def _do_copy(self):
        self.current_function = self.register_function(
            self.to_function_name('copy', 'Object'))
        instance = self.register_param(VariableInfo('instance'))

        type_size = self.register_local(VariableInfo('type_size'))
        new_instance = self.register_local(VariableInfo('new_instance'))
        times = self.register_local(VariableInfo('times'))
        cond = self.register_local(VariableInfo('cond'))
        attr = self.register_local(VariableInfo('attr'))
        temp_times = self.register_local(VariableInfo('temp_times'))
        const = self.define_internal_local()
        cont = cil_ast.LabelNode('continue'+self.give_unic_label())
        end = cil_ast.LabelNode('end'+self.give_unic_label())

        self.register_instruction(cil_ast.GetAttrNode(type_size, instance, 3))
        self.register_instruction(cil_ast.AllocateNode(new_instance, type_size))
        self.register_instruction(cil_ast.AssignNode(times, 0))
        self.register_instruction(cont)
        self.register_instruction(cil_ast.EqualNode(cond, times, type_size))
        self.register_instruction(cil_ast.IfNode(cond, end))
        self.register_instruction(cil_ast.GetAttrNode(attr, instance, times))
        self.register_instruction(cil_ast.SetAttrNode(attr, new_instance, times))
        self.register_instruction(cil_ast.AssignNode(temp_times, times))
        self.register_instruction(cil_ast.AssignNode(const, 1))
        self.register_instruction(cil_ast.PlusNode(times, temp_times, const))
        self.register_instruction(cil_ast.GotoNode(cont))
        self.register_instruction(end)

        self.register_instruction(cil_ast.ReturnNode(new_instance))

        self.current_function = None

    def _do_concat_func(self):
        self.current_function = self.register_function(
            self.to_function_name('concat', 'String'))
        # todo falta desambiguar los labels
        string1 = self.register_param(VariableInfo('string1', 'String'))
        string2 = self.register_param(VariableInfo('string2', 'String'))

        length1 = self.register_local(VariableInfo('length1'))
        length2 = self.register_local(VariableInfo('length2'))
        actual_char = self.register_local(VariableInfo('actual_char'))
        index = self.register_local(VariableInfo('index'))
        temp_index = self.register_local(VariableInfo('temp_index'))
        result = self.register_local(VariableInfo('result'))
        sum = self.register_local(VariableInfo('sum'))
        cond = self.register_local(VariableInfo('cond'))
        second_index = self.register_local(VariableInfo('second_index'))
        array = self.register_local(VariableInfo('array'))
        const0 = self.define_internal_local()

        self.register_instruction(
            cil_ast.StaticCallNode(length1, self.to_function_name('length', 'String'),
                                   [string1]))
        self.register_instruction(cil_ast.AssignNode(index, 0))

        self.register_instruction(
            cil_ast.StaticCallNode(length2, self.to_function_name('length', 'String'),
                                   [string2]))
        self.register_instruction(cil_ast.PlusNode(sum, length1, length2))

        temp1 = self.define_internal_local()
        self.register_instruction(cil_ast.AssignNode(temp1, 1))
        self.register_instruction(cil_ast.AssignNode(const0, 0))
        temp2 = self.define_internal_local()
        self.register_instruction(cil_ast.PlusNode(temp2, sum, temp1))
        self.register_instruction(cil_ast.ArrayNode(array, temp2))

        cont = cil_ast.LabelNode('continue'+self.give_unic_label())
        end1 = cil_ast.LabelNode('end1'+self.give_unic_label())
        end2 = cil_ast.LabelNode('end2'+self.give_unic_label())

        self.register_instruction(cont)
        self.register_instruction(cil_ast.GetIndexNode(actual_char, string1, index))
        self.register_instruction(cil_ast.EqualNode(cond, actual_char, const0))
        self.register_instruction(cil_ast.IfNode(cond, end1))
        self.register_instruction(cil_ast.SetAttrNode(actual_char, result, index, 'String'))
        self.register_instruction(cil_ast.AssignNode(temp_index, index))
        self.register_instruction(cil_ast.PlusNode(index, temp_index, temp1))
        self.register_instruction(cil_ast.GotoNode(cont))
        self.register_instruction(end1)
        self.register_instruction(cil_ast.GetIndexNode(actual_char, string2, second_index))
        self.register_instruction(cil_ast.EqualNode(cond, actual_char, const0))
        self.register_instruction(cil_ast.IfNode(cond, end2))
        self.register_instruction(cil_ast.SetIndexNode(actual_char, result, index))
        self.register_instruction(cil_ast.AssignNode(temp_index, second_index))
        self.register_instruction(cil_ast.PlusNode(second_index, temp_index, temp1))
        self.register_instruction(cil_ast.AssignNode(temp_index, index))
        self.register_instruction(cil_ast.PlusNode(index, temp_index, temp1))
        self.register_instruction(cil_ast.GotoNode(end1))
        self.register_instruction(end2)
        self.register_instruction(cil_ast.SetIndexNode(const0, result, index))

        self.register_instruction(cil_ast.ReturnNode(result))

        self.current_function = None

    def _create_object_type(self):
        type_node = self.register_type('Object')
        # nombre vtable, begin, len
        type_node.methods.append(
            cil_ast.MethodNode('abort', self.to_function_name('abort', 'Object')))
        type_node.methods.append(
            cil_ast.MethodNode('type_name', self.to_function_name('type_name',
                                                                  'Object')))
        type_node.methods.append(
            cil_ast.MethodNode('copy', self.to_function_name('copy', 'Object')))

        type_node.attrs.append(cil_ast.AttrNode('_name'))
        type_node.attrs.append(cil_ast.AttrNode('_vtable'))
        type_node.attrs.append(cil_ast.AttrNode('_begin'))
        type_node.attrs.append(cil_ast.AttrNode('_len'))
        self.object_type = type_node

    def _create_io_type(self):
        type_node = self.register_type('IO')

        type_node.methods.append(
            cil_ast.MethodNode('abort',
                               self.to_function_name('abort', 'Object')))
        type_node.methods.append(
            cil_ast.MethodNode('type_name',
                               self.to_function_name('type_name', 'Object')))
        type_node.methods.append(
            cil_ast.MethodNode('copy', self.to_function_name('copy', 'Object')))
        type_node.methods.append(
            cil_ast.MethodNode('out_string',
                               self.to_function_name('out_string', 'IO')))
        type_node.methods.append(
            cil_ast.MethodNode('out_int',
                               self.to_function_name('out_int', 'IO')))
        type_node.methods.append(
            cil_ast.MethodNode('in_string',
                               self.to_function_name('in_string', 'IO')))
        type_node.methods.append(
            cil_ast.MethodNode('in_int', self.to_function_name('in_int', 'IO')))

        type_node.attrs.append(cil_ast.AttrNode('_name'))
        type_node.attrs.append(cil_ast.AttrNode('_vtable'))
        type_node.attrs.append(cil_ast.AttrNode('_begin'))
        type_node.attrs.append(cil_ast.AttrNode('_len'))
        self.io_type = type_node

    def _do_abort(self):

        self.current_function = self.register_function(
            self.to_function_name('abort', 'Object'))

        result = self.register_param(VariableInfo('self', 'Object'))
        self.register_instruction(cil_ast.AbortNode())
        self.register_instruction(cil_ast.ReturnNode(result))
        self.current_function = None

    def _do_type_name(self):
        self.current_function = self.register_function(
            self.to_function_name('type_name', 'Object'))
        self_param = self.register_param(VariableInfo('self', 'Object'))
        data = self.register_local(VariableInfo('data', 'String'))
        name = self.register_local(VariableInfo('name', 'String'))
        self.register_instruction(cil_ast.GetAttrNode(data, self_param, 0))
        self.register_instruction(cil_ast.LoadNode(name, data))

        #self.register_instruction(cil_ast.PrintStrNode(name))
        self.register_instruction(cil_ast.ReturnNode(name))

        self.current_function = None

    def _do_out_string(self):
        self.current_function = self.register_function(
            self.to_function_name('out_string', 'IO'))

        self_param = self.register_param(VariableInfo('self', 'IO'))
        string_param = self.register_param(VariableInfo("string_param" , "String"))
        self.register_instruction(cil_ast.PrintStrNode(string_param))

        self.register_instruction(cil_ast.ReturnNode(self_param))

        self.current_function = None

    def _do_out_int(self):
        self.current_function = self.register_function(
            self.to_function_name('out_int', 'IO'))

        self_param = self.register_param(VariableInfo('self', 'IO'))
        int_param = self.register_param(VariableInfo("int_param", "Int"))
        self.register_instruction(cil_ast.PrintIntNode(int_param))
        self.register_instruction(cil_ast.ReturnNode(self_param))

        self.current_function = None

    def _do_in_string(self):
        self.current_function = self.register_function(
            self.to_function_name('in_string', 'IO'))

        instance = self.register_param(VariableInfo("self"))
        result = self.register_local(VariableInfo('local'))
        length = self.register_local(VariableInfo('length'))

        self.register_instruction(cil_ast.AssignNode(length, 1024))
        self.register_instruction(cil_ast.ArrayNode(result, length))
        self.register_instruction(cil_ast.ReadStrNode(result))
        self.register_instruction(cil_ast.ReturnNode(result))

        self.current_function = None

    def _do_in_int(self):
        self.current_function = self.register_function(
            self.to_function_name('in_int', 'IO'))
        instance = self.register_param(VariableInfo("self"))
        return_value  = self.register_local(VariableInfo('return_value', 'String'))
        self.register_instruction(cil_ast.ReadIntNode(return_value))
        self.register_instruction(cil_ast.ReturnNode(return_value))

        self.current_function = None
        # todo ponerle el tipo estatico
    def _do_attr_con_IO(self):
        self.current_function = self.register_function(self.to_function_name('_attr_con', 'IO'))
        param = self.register_param(VariableInfo('self'))
        io_begin = self.type_graph.types_nodes["IO"].begin
        io_length = len(self.types.attrs["IO"])
        io_name = self.register_data("\"IO\"").vname

        beg_local = self.register_local(VariableInfo("begin_local"))
        len_local = self.register_local(VariableInfo("len_local"))
        self.register_instruction(cil_ast.AssignNode(beg_local,io_begin))
        self.register_instruction(cil_ast.AssignNode(len_local,io_length))
        self.register_instruction(cil_ast.SetAttrNode(beg_local,param,2))
        self.register_instruction(cil_ast.SetAttrNode(len_local,param,3))
        self.register_instruction(cil_ast.SetAttrNode(io_name, param,0))
        self.register_instruction(cil_ast.ReturnNode(param))
        self.current_function = None

    def _do_attr_Object(self):
        self.current_function = self.register_function(self.to_function_name('_attr_con', 'Object'))
        param = self.register_param(VariableInfo('self'))
        ob_begin = self.type_graph.types_nodes["Object"].begin
        ob_length = len(self.types.attrs["Object"])
        ob_name = self.register_data("\"Object\"").vname

        beg_local = self.register_local(VariableInfo("begin_local"))
        len_local = self.register_local(VariableInfo("len_local"))
        self.register_instruction(cil_ast.AssignNode(beg_local, ob_begin))
        self.register_instruction(cil_ast.AssignNode(len_local, ob_length))
        self.register_instruction(cil_ast.SetAttrNode(beg_local, param, 2))
        self.register_instruction(cil_ast.SetAttrNode(len_local, param, 3))
        self.register_instruction(cil_ast.SetAttrNode(ob_name, param, 0))
        self.register_instruction(cil_ast.ReturnNode(param))
        self.current_function = None

    def _do_met_con_Object(self):
        #self.current_type = self.type_graph.types_nodes["Object"]
        # Your code here!!! (Handle all the .TYPE section
        self.current_function = self.register_function(self.to_function_name(
            '_method_con', "Object"))

        vtable = self.register_param(VariableInfo('_vtable', "Object"))

        for method in self.object_type.methods:
            self.register_instruction(
                cil_ast.SuperSetAttrNode(vtable, method.name, method.fundest,
                                         "Object"))
        self.register_instruction(cil_ast.ReturnNode(vtable))
        self.current_function = None

    def _do_met_con_IO(self):
        #self.current_type = self.type_graph.types_nodes["IO"]
        # Your code here!!! (Handle all the .TYPE section)
        self.current_function = self.register_function(self.to_function_name(
            '_method_con', "IO"))

        vtable = self.register_param(VariableInfo('_vtable', "IO"))

        for method in self.io_type.methods:
            self.register_instruction(
                cil_ast.SuperSetAttrNode(vtable, method.name, method.fundest,
                                         "IO"))
        self.register_instruction(cil_ast.ReturnNode(vtable))
        self.current_function = None

    def _do_equals_string(self):
        self.current_function = self.register_function(
            self.to_function_name('equals_string', 'String'))

        string1 = self.register_param(VariableInfo('string1', 'String'))
        string2 = self.register_param(VariableInfo('string2', 'String'))

        index = self.register_local(VariableInfo('index'))
        char1 = self.register_local(VariableInfo('char1'))
        char2 = self.register_local(VariableInfo('char2'))
        cond = self.register_local(VariableInfo('cond'))
        result = self.register_local(VariableInfo('result'))
        temp_index = self.register_local(VariableInfo('temp_index'))
        const1 = self.register_local(VariableInfo('const1'))

        cont = cil_ast.LabelNode('continue'+self.give_unic_label())
        equals = cil_ast.LabelNode('equals'+self.give_unic_label())
        not_end = cil_ast.LabelNode('not_end'+self.give_unic_label())
        not_equal = cil_ast.LabelNode('not_equal'+self.give_unic_label())
        end = cil_ast.LabelNode('end'+self.give_unic_label())

        self.register_instruction(cil_ast.AssignNode(index, 0))
        self.register_instruction(cil_ast.AssignNode(const1, 1))
        self.register_instruction(cont)
        self.register_instruction(cil_ast.GetIndexNode(char1, string1, index))
        self.register_instruction(cil_ast.GetIndexNode(char2, string2, index))
        self.register_instruction(cil_ast.EqualNode(cond, char1, char2))
        self.register_instruction(cil_ast.IfNode(cond, equals))
        self.register_instruction(cil_ast.GotoNode(not_equal))
        self.register_instruction(equals)
        self.register_instruction(cil_ast.IfNode(char1, not_end))
        self.register_instruction(cil_ast.AssignNode(result, 1))
        self.register_instruction(cil_ast.GotoNode(end))
        self.register_instruction(not_end)
        self.register_instruction(cil_ast.AssignNode(temp_index, index))
        self.register_instruction(cil_ast.PlusNode(index, temp_index, const1))
        self.register_instruction(cil_ast.GotoNode(cont))
        self.register_instruction(not_equal)
        self.register_instruction(cil_ast.AssignNode(result, 0))
        self.register_instruction(end)
        self.register_instruction(cil_ast.ReturnNode(result))

        self.current_function = None


class Types():

    def __init__(self, graph: TypesGraph):
        self.types = graph.types_nodes
        self.attrs = None
        self.methods = None

    def get_attrs(self) -> Dict[str, Dict[str, int]]:
        if not self.attrs:
            self.attrs = OrderedDict()
            for type_name, class_book in self.types.items():
                self.attrs[type_name] = OrderedDict()
                self.attrs[type_name]['_name'] = 0
                self.attrs[type_name]['_vtable'] = 1
                self.attrs[type_name]['_begin'] = 2
                self.attrs[type_name]['_len'] = 3 # todo ver aqui si es correcto
                for index, attr in enumerate(class_book.all_attributes(clean=False).keys()):
                    self.attrs[type_name][attr] = index + 4

        return self.attrs

    def get_methods(self) -> Dict[str, Dict[str, Tuple[str, int]]]:
        if not self.methods:
            self.methods = OrderedDict()
            for type_name, class_book in self.types.items():
                self.methods[type_name] = OrderedDict()
                for index, method in enumerate(class_book.all_methods(clean=False).keys()):
                    self.methods[type_name][method] = (f'function_{method}_at_{type_name}',
                                                        index)
        return self.methods

# todo los metodos de print pueden imprimir booleanos, int, string, otros,
#  tener en cuenta
# class Hasher():
#
#     def __init__(self):
#         self.labels = 0
#         self.attrs = 0
#         self.methods = 0
#         self.params = 0
#
#     def hash_method(self, method_name: str, type_name: str) -> str:
#         return f'function_{method_name}_at_{type_name}'
#
#     def hash_param(self, param_name, function_name):
#         return f'param_{self.current_function.fname}_{vinfo.name}_{len(self.params)}'
#
#     def hash_local(self, ):
#         return f'local_{self.current_function.fname}_{vinfo.name}_{len(self.localvars)}'
#
#     def hash_data(self):
#         return f'data_{len(self.dotdata)}'
#
#     def hash_internal(self):
#         return
#

def main(pars):
    #pars = parser.main(r'C:\Users\LsW\Desktop\Proyecto de Compilacion Jessica Quesada, David '
    #r'Castillo, Rayniel Ramos,  y otros\Compiler\test\test_cases\complex.cl', testing_mode=False)
    #print(pars)
    checker = semantic_checker.TypeChecker(pars)
    checker.check()
    visitor = COOLToCILVisitor(checker.types_graph, checker.program_node)

    res = visitor.result
    func: cil_ast.FunctionNode
    for func in res.dotcode:
        print(func.fname)
        for param in func.params:
            print(param.destaddr)
        for loc in func.localvars:
            print(loc.destaddr)
        for ins in func.instructions:
            if isinstance(ins, cil_ast.ExceptNode):
                print('Except')
            elif isinstance(ins, cil_ast.AbortNode):
                print('Abort')
            elif isinstance(ins, cil_ast.SuperSetAttrNode):
                ins: cil_ast.SuperSetAttrNode
                print(f'SuperSetAttr: {ins.vtable}, {ins.method_name}, {ins.fname}')
            elif isinstance(ins, cil_ast.NegationNode):
                ins: cil_ast.NegationNode
                print(f'Negation: {ins.destaddr}, {ins.sraddr}')
            elif isinstance(ins, cil_ast.NotNode):
                ins: cil_ast.NotNode
                print(f'Not: {ins.destaddr}, {ins.sraddr}')
            elif isinstance(ins, cil_ast.AndNode):
                ins: cil_ast.AndNode
                print(f'And: {ins.destaddr}, {ins.sraddr1}, {ins.sraddr2}')
            elif isinstance(ins, cil_ast.GreatherThanNode):
                ins: cil_ast.GreatherThanNode
                print(f'GreatherThanNode: {ins.destaddr}, {ins.sraddr1}, {ins.sraddr2}')
            elif isinstance(ins, cil_ast.GreatherOrEqualThanNode):
                ins: cil_ast.GreatherOrEqualThanNode
                print(f'GreatherOrEqualThanNode: {ins.destaddr}, {ins.sraddr1}, {ins.sraddr2}')
            elif isinstance(ins, cil_ast.EqualNode):
                ins: cil_ast.EqualNode
                print(f'EqualNode: {ins.destaddr}, {ins.sraddr1}, {ins.sraddr2}')
            elif isinstance(ins, cil_ast.LessThanNode):
                ins: cil_ast.LessThanNode
                print(f'LessThanNode: {ins.destaddr}, {ins.sraddr1}, {ins.sraddr2}')
            elif isinstance(ins, cil_ast.LessOrEqualThanNode):
                ins: cil_ast.LessOrEqualThanNode
                print(f'LessOrEqualThanNode: {ins.destaddr}, {ins.sraddr1}, {ins.sraddr2}')
            elif isinstance(ins, cil_ast.PrintIntNode):
                ins: cil_ast.PrintIntNode
                print(f'PrintIntNode: {ins.straddr}')
            elif isinstance(ins, cil_ast.ReadIntNode):
                ins: cil_ast.ReadIntNode
                print(f'ReadIntNode: {ins.destaddr}')
            elif isinstance(ins, cil_ast.PrintStrNode):
                ins: cil_ast.PrintStrNode
                print(f'PrintStrNode: {ins.straddr}')
            elif isinstance(ins, cil_ast.ReadStrNode):
                ins: cil_ast.ReadStrNode
                print(f'ReadStrNode: {ins.destaddr}')
            elif isinstance(ins, cil_ast.LoadNode):
                ins: cil_ast.LoadNode
                print(f'LoadNode: {ins.destaddr}, {ins.array}')
            elif isinstance(ins, cil_ast.ReturnNode):
                ins: cil_ast.ReturnNode
                print(f'ReturnNode: {ins.addr}')
            elif isinstance(ins, cil_ast.DinamicCallNode):
                ins: cil_ast.DinamicCallNode
                print(f'DinamicCallNode: {ins.destaddr}, {ins.instance}, ...')
            elif isinstance(ins, cil_ast.StaticCallNode):
                ins: cil_ast.StaticCallNode
                print(f'StaticCallNode: {ins.destaddr}, {ins.methodaddr}, {ins.args}')
            elif isinstance(ins, cil_ast.IfNode):
                ins: cil_ast.IfNode
                print(f'IfNode: {ins.cond}, {ins.label}')
            elif isinstance(ins, cil_ast.GotoNode):
                ins: cil_ast.GotoNode
                print(f'GotoNode: {ins.label}')
            elif isinstance(ins, cil_ast.LabelNode):
                ins: cil_ast.LabelNode
                print(f'LabelNode: {ins.label}')
            elif isinstance(ins, cil_ast.ArrayNode):
                ins: cil_ast.ArrayNode
                print(f'ArrayNode: {ins.destaddr}, {ins.length}')
            elif isinstance(ins, cil_ast.AllocateNode):
                ins: cil_ast.AllocateNode
                print(f'AllocateNode: {ins.destaddr}, {ins.typesize}')
            elif isinstance(ins, cil_ast.SetIndexNode):
                ins: cil_ast.SetIndexNode
                print(f'SetIndexNode: {ins.destaddr}, {ins.arrayaddr}, {ins.offset}')
            elif isinstance(ins, cil_ast.GetIndexNode):
                ins: cil_ast.GetIndexNode
                print(f'GetIndexNode: {ins.destaddr}, {ins.arrayaddr}, {ins.offset}')
            elif isinstance(ins, cil_ast.SetAttrNode):
                ins: cil_ast.SetAttrNode
                print(f'SetAttrNode: {ins.destattr}, {ins.typeaddr}, {ins.attroffset}')
            elif isinstance(ins, cil_ast.GetAttrNode):
                ins: cil_ast.GetAttrNode
                print(f'GetAttrNode: {ins.destattr}, {ins.typeaddr}, {ins.attroffset}')
            elif isinstance(ins, cil_ast.AssignNode):
                ins: cil_ast.AssignNode
                print(f'AssignNode: {ins.destaddr}, {ins.source}')

    mips_generator = MipsGenerator(visitor.result, visitor.types)
    mips_generator.generate()
    mips_generator.__show__()
    mips_generator.instructions
    print(mips_generator.mains)
    with open(r'C:\Users\David\Desktop\ourhelloworld.s', 'w') as file:
        for ins in mips_generator.instructions:
            file.write(ins + '\n')