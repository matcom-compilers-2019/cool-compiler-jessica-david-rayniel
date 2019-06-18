from collections import OrderedDict
from code.front_end import cil_ast
from typing import List, Optional
from code.utils import visitor, cil_scoper
from code.utils.cil_scoper import CilScope
from code.utils.semantic_checker_utils import *
from code.front_end import our_ast



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
    # todo ver que sea consistente el variable info

    def register_param(self, vinfo: VariableInfo) -> str:
        vinfo.name = f'param_{self.current_function.fname}_{vinfo.name}_{len(self.params)}'
        param_node = cil_ast.ParamNode(vinfo.name)
        self.params.append(param_node)
        return vinfo.name

    # def register_local(self, vinfo: VariableInfo) -> str:
    #     vinfo.name = f'local_{self.current_function.fname}_{vinfo.name}_{len(self.localvars)}'
    #     local_node = cil_ast.LocalNode(vinfo.name)
    #     self.localvars.append(local_node)
    #     return vinfo.name

    # si ya la variable local esta no volver a definir otra, puesto que ese
    # valor es necesario a la hora de asignar
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
    # todo al final quite esto
    def to_function_attr_name(self, attr_name: str, type_name: str):
        return f'attr_init_func_{attr_name}_at_{type_name}'

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

    def __init__(self, type_graph: 'TypesGraph'):
        super().__init__(type_graph)
        self.not_counter = 0
        self.equal_counter = 0
        self.less_than_node_counter = 0
        self.if_counter = 0
        self.while_counter = 0
        self.less_or_equal_counter = 0
        self.is_void_counter = 0

    @visitor.on('ASTNode')
    def visit(self, node):
        pass

    @visitor.when(our_ast.ProgramNode)
    def visit(self, node: our_ast.ProgramNode, scope: 'CilScope'):
        ######################################################
        # node.classes -> [ ClassNode ... ]
        ######################################################
        # todo definir la funcion que retorna void para los attr vacios, definir el
        #  tipo dinamico void que tenga la funcion magica que lanza excepcion
        self.register_type('Void')
        # todo crear las funciones builtin
        self.current_function = self.register_function('entry')
        instance = self.define_internal_local()
        result = self.define_internal_local()
        self.register_instruction(cil_ast.AllocateNode(instance, 'Main'))
        self.register_instruction(cil_ast.ArgNode(instance))
        self.register_instruction(cil_ast.StaticCallNode(result, 'main'))
        self.register_instruction(cil_ast.ReturnNode(0))
        self.current_function = None

        for clas in node.classes:
            self.visit(clas, scope.create_child())

        return cil_ast.ProgramNode(self.dottypes, self.dotdata, self.dotcode)

    @visitor.when(our_ast.ClassNode)
    def visit(self, node, scope):
        ####################################################################
        # node.name -> str
        # node.parent -> str
        # node.attrs -> [ AttrNode ... ]
        # node.methods -> [ MethodNode ... ]
        ####################################################################

        self.current_type = self.type_graph.types_nodes[node.name]
        # Your code here!!! (Handle all the .TYPE section)
        type_node: cil_ast.TypeNode = self.register_type(node.name)
        # una sola funcion que retorne el tipo void
        # todo crear dos constructores uno para los methodos y otro para los
        #  attr

        for attr, _ in self.current_type.all_attributes():
            tipe = self.current_type.find_attr(attr, internal=True)
            type_node.attrs.append(cil_ast.AttrNode(f'{tipe[1]}_{attr}'))

            scope.define_variable(attr, f'{tipe[1]}_{attr}')


        for method, _ in self.current_type.all_methods():
            tipe = self.current_type.find_method(method, internal=True)
            type_node.methods.append(cil_ast.MethodNode(
                f'{tipe[1]}_{method}', self.to_function_name(method, tipe[1])))

        # se crea el constructor de attr
        self.current_method = (('return', node.name,),)

        self.current_function = self.register_function(self.to_function_name(
            '_attr_con', node.name))

        type_node.methods.append(
            cil_ast.MethodNode('_attr_con', self.to_function_name('_attr_con',
                                                                  node.name)))

        self.register_param(VariableInfo('self', self.current_type))

        self.register_instruction(
            cil_ast.StaticCallNode(
                'self', self.to_function_name('_attr_con',
                                              self.current_type.parent.name)))

        attrs = (f for f in node.attrs)
        var = None
        for attr, child_scope in zip(attrs, scope.create_child()):
            if attr.value:
                var = self.visit(attr, child_scope)

                self.register_instruction(cil_ast.SetAttrNode('self',
                                      f'{self.current_type.name}_{attr.name}',
                                        var))

            else: self.register_instruction(cil_ast.SetAttrNode('self',
                            f'{self.current_type.name}_{attr.name}', 'Void'))

        self.register_instruction(cil_ast.ReturnNode('self'))

        self.current_function = None
        self.current_method = None
        #############################

        methods = (f for f in node.methods)
        for method, child_scope in zip(methods, scope.create_child()):
            self.visit(method, child_scope)

        self.current_type = None
# todo al inicializar un attr (ya sea en clase o en let) si es bool se le pone false, int 0,
#  string '' y en otro caso void
    @visitor.when(our_ast.MethodNode)
    def visit(self, node, scope: CilScope):
        ###############################
        # node.name -> str
        # node.params -> [ ParamNode ... ]
        # node.return_type -> str
        # node.body -> [ ExprNode ... ]
        ###############################
        # todo cuando el attr no tenga expr se inicializa con el tipo void, tener
        #  en cuenta entonces que en los dispatch si el typof es void debe dar
        #  runtime error, esto es poner una linea en los dispatch para que verifiquen
        #  y lancen exception
        self.current_method = self.current_type.find_method(node.name, internal=True)

        # Your code here!!! (Handle PARAMS)
        function_node = self.register_function(
            self.to_function_name(node.name, self.current_type.name))

        self.current_function = function_node

        self.register_param(VariableInfo('self', self.current_type.name))
        for param_node in node.params:
            param_cil_name = self.register_param(
                VariableInfo(param_node.name,
                             self.type_graph.types_nodes[param_node.type]))
            scope.define_variable(param_node.name, param_cil_name)
        ##################################################################

        for instruction in node.body:
            value = self.visit(instruction, scope)
        # Your code here!!! (Handle RETURN)

        self.register_instruction(cil_ast.ReturnNode(0))
        self.current_function = None

        self.current_method = None

    @visitor.when(our_ast.IdNode)
    def visit(self, node, scope):
        ###############################
        # node.name -> str
        ###############################

        # se busca el verdadero nombre de la variable en cil, que no es mas
        # que otra variable condistinto nombre en cil pero igual en cool, de
        # esta forma se obtiene el truco de ocultamiento

        # Your code here!!!
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
                # todo poner los typos a los setattr y getattr
                self.register_instruction(
                    cil_ast.GetAttrNode(temp, 'self', value.split('_')[1]))

                self.register_instruction(
                    cil_ast.SetAttrNode(temp, 'self',
                                        scope.locals[node.name].split('_')[1]))

            else:
                self.register_instruction(
                    cil_ast.GetAttrNode(scope.locals[node.name], 'self',
                                        value.split('_')[1]))
        else:
            if scope.locals[node.name].split('_')[0] in \
                    self.type_graph.types_nodes.keys():
                self.register_instruction(
                    cil_ast.SetAttrNode(value, 'self',
                                        scope.locals[node.name].split('_')[1]))

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
        # todo el asignode que tenga el builtin tiene que saber que el valor sea
        #  builint y por tanto por valor o por referencia, para eso poner el tipo
        #  estatico para el nodo del expr

        # todo no es posible crear variables dentro de los metodos solo a traves de
        #  de lets, los attr son los otros que los hacen a trves de los lets o de
        #  las constantes

        # todo poner en los allocate que pongan como primer attr del tipo el nombre del
        #  tipo como un attr, hay que poner en la .data los nombres de todos los tipos

        # todo poner en los case todas las posibilidades del los tipos dinamicos y
        #  por que rama se iria en caso de ser ese tipo
        #  para cada case, lo cual va a permitir que una vez en runtime se conoza el
        #  tipo dinamico solo tengo que buscar en esta estructura por que rama irme,
        #  mejor que hacer un lca en cil
        if isinstance(node, our_ast.StringNode):
            data_name = self.register_data(node.value).vname
            self.register_instruction(cil_ast.LoadNode(temp, data_name))
        # todo el asign node tiene que saber cuando es por valor y cuando por
        #  referencia
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

        cond_var = self.visit(node.condition, scope)

        after = cil_ast.LabelNode(f'after_{self.if_counter}')
        endif = cil_ast.LabelNode(f'endif_{self.if_counter}')

        self.if_counter += 1

        self.register_instruction(cil_ast.IfNode(cond_var, after))

        self.visit(node.false_body, scope)

        self.register_instruction(cil_ast.GotoNode(endif))
        self.register_instruction(after)

        self.visit(node.true_body, scope)

        self.register_instruction(endif)


    @visitor.when(our_ast.WhileNode)
    def visit(self, node: our_ast.WhileNode, scope):

        cont = cil_ast.LabelNode(f'continue_{self.while_counter}')
        loop = cil_ast.LabelNode(f'loop_{self.while_counter}')
        endloop = cil_ast.LabelNode(f'endloop_{self.while_counter}')

        self.while_counter += 1

        temp = self.visit(node.condition, scope)

        self.register_instruction(cil_ast.IfNode(temp, loop))
        self.register_instruction(cil_ast.GotoNode(endloop))
        self.register_instruction(loop)

        self.visit(node.body, scope)

        self.register_instruction(cil_ast.GotoNode(cont))

        self.register_instruction(endloop)
        temp1 = self.define_internal_local()
        self.register_instruction(cil_ast.AllocateNode(temp1, 'Void'))

        return temp1


    @visitor.when(our_ast.DispatchSelfNode)
    def visit(self, node: our_ast.DispatchSelfNode, scope):
        # todo modificar esto para que en el caso de que sea void
        variables = []

        for expr in node.args:
            variables.append(self.visit(expr, scope))

        self.register_instruction(cil_ast.ArgNode('self'))

        for var in variables:
            self.register_instruction(cil_ast.ArgNode(var))

        temp = self.define_internal_local()

        self.register_instruction(
            cil_ast.StaticCallNode(
                temp, self.to_function_name(node.name, self.current_type.name)))


    @visitor.when(our_ast.DispatchStaticNode)
    def visit(self, node: our_ast.DispatchStaticNode, scope):

        variables = []

        for expr in node.args:
            variables.append(self.visit(expr, scope))

        expr_var = self.visit(node.expr)

        self.register_instruction(cil_ast.ArgNode(expr_var))

        for var in variables:
            self.register_instruction(cil_ast.ArgNode(var))

        temp = self.define_internal_local()
        # todo necesito el typo de expr, para esto hacer el typof de la
        #  instancia del expr
        # self.register_instruction(
        #     cil_ast.StaticCallNode(
        #         temp, self.to_function_name(node.name, )))


    @visitor.when(our_ast.DispatchInheritsNode)
    def visit(self, node: our_ast.DispatchInheritsNode, scope):

        variables = []

        for expr in node.args:
            variables.append(self.visit(expr, scope))

        expr_var = self.visit(node.expr)

        self.register_instruction(cil_ast.ArgNode(expr_var))

        for var in variables:
            self.register_instruction(cil_ast.ArgNode(var))

        temp = self.define_internal_local()

        self.register_instruction(
            cil_ast.DinamicCallNode(temp, node.type,
                                    self.to_function_name(node.name,
                                                          node.type)))
        return temp

    @visitor.when(our_ast.BlockNode)
    def visit(self, node: our_ast.BlockNode, scope):

        variables = []

        for var in node.body:
            variables.append(self.visit(var))

        temp = self.define_internal_local()

        self.register_instruction(cil_ast.AssignNode(temp, variables[-1]))

        return temp


    @visitor.when(our_ast.NewNode)
    def visit(self, node: our_ast.NewNode, scope):

        temp = self.define_internal_local()
        temp2 = self.define_internal_local()
        # todo solo los news, los attr node y los builtin bool, string e int
        #  crean nuevas variables locales y es necesario una estructura
        #  de arbol tipo scope para que se sepa con que variable se esta
        #  trabajando
        self.register_instruction(cil_ast.AllocateNode(temp, node.type))

        self.register_instruction(cil_ast.ArgNode(temp))
        self.register_instruction(
            cil_ast.StaticCallNode(temp2, self.to_function_name('_attr_con',
                                                                node.type)))
        # todo revisar pq la clase Attribute en el type hace referencia al tipo
        #  del attr no al tipo al que pertenece, cuidado
        return temp2


    @visitor.when(our_ast.LessThanNode)
    def visit(self, node: our_ast.LessThanNode, scope):

        lvar = self.visit(node.lvalue)
        rvar = self.visit(node.rvalue)

        temp_rest = self.define_internal_local()
        temp_result = self.define_internal_local()

        self.register_instruction(cil_ast.MinusNode(temp_rest, lvar, rvar))

        label_not = cil_ast.LabelNode(f'not_{self.less_than_node_counter}')
        label_endbranch = cil_ast.LabelNode(f'endbranch_{self.less_than_node_counter}')

        self.less_than_node_counter += 1
        # todo look this
        self.register_instruction(cil_ast.BranchLessThanZeroNode(temp_rest,
                                                                 label_not.label))
        self.register_instruction(cil_ast.AssignNode(temp_result, 1))
        self.register_instruction(cil_ast.GotoNode(label_endbranch))
        self.register_instruction(label_not)
        self.register_instruction(cil_ast.AssignNode(temp_result, 0))
        self.register_instruction(label_endbranch)

        return temp_result


    @visitor.when(our_ast.EqualNode)
    def visit(self, node: our_ast.EqualNode, scope):

        lvar = self.visit(node.lvalue, scope)
        rvar = self.visit(node.rvalue, scope)

        temp_l = self.define_internal_local()
        temp_r = self.define_internal_local()
        notequal_label = cil_ast.LabelNode(f'notequal_{self.equal_counter}')
        endif_label = cil_ast.LabelNode(f'endif_{self.equal_counter}')

        self.equal_counter += 1

        self.register_instruction(cil_ast.AssignNode(temp_l, lvar))
        self.register_instruction(cil_ast.AssignNode(temp_r, rvar))

        temp_rest = self.define_internal_local()
        temp_result = self.define_internal_local()
        self.register_instruction(cil_ast.MinusNode(temp_rest, temp_l, temp_r))

        self.register_instruction(cil_ast.IfNode(temp_rest, notequal_label))

        self.register_instruction(cil_ast.AssignNode(temp_result, 1))
        self.register_instruction(cil_ast.GotoNode(endif_label))
        self.register_instruction(notequal_label)
        self.register_instruction(cil_ast.AssignNode(temp_result, 0))
        self.register_instruction(endif_label)

        return temp_result

    @visitor.when(our_ast.LessOrEqualNode)
    def visit(self, node: our_ast.LessOrEqualNode, scope):

        lvar = self.visit(node.lvalue)
        rvar = self.visit(node.rvalue)

        temp_result = self.define_internal_local()
        temp_rest = self.define_internal_local()
        end_label = cil_ast.LabelNode(f'end_{self.less_or_equal_counter}')
        continue_label = cil_ast.LabelNode(f'continue_{self.less_or_equal_counter}')
        not_label = cil_ast.LabelNode(f'not_{self.less_or_equal_counter}')

        self.less_or_equal_counter += 1

        self.register_instruction(cil_ast.MinusNode(temp_rest, rvar, lvar))
        self.register_instruction(cil_ast.IfNode(temp_rest, continue_label))
        self.register_instruction(cil_ast.AssignNode(temp_result, 1))

        self.register_instruction(cil_ast.GotoNode(end_label))
        self.register_instruction(continue_label)
        self.register_instruction(cil_ast.BranchLessThanZeroNode(temp_result,
                                                                 not_label.label))
        self.register_instruction(cil_ast.AssignNode(temp_result, 1))
        self.register_instruction(cil_ast.GotoNode(end_label))
        self.register_instruction(not_label)
        self.register_instruction(cil_ast.AssignNode(temp_result, 0))

        return temp_result
    # todo scope nuevo en clase, metodo, lets, branch
    # todo branch, params, let,
    @visitor.when(our_ast.NotNode)
    def visit(self, node: our_ast.NotNode, scope):

        expr = self.visit(node.value)

        makefalse_label = cil_ast.LabelNode(f'makefalse_{self.not_counter}')
        endif_label = cil_ast.LabelNode(f'endif_{self.not_counter}')

        self.not_counter += 1

        temp_result = self.define_internal_local()

        self.register_instruction(cil_ast.IfNode(expr, makefalse_label))
        self.register_instruction(cil_ast.AssignNode(temp_result, 1))
        self.register_instruction(cil_ast.GotoNode(endif_label))
        self.register_instruction(makefalse_label)
        self.register_instruction(cil_ast.AssignNode(temp_result, 0))
        self.register_instruction(endif_label)

        return temp_result

    @visitor.when(our_ast.AttrNode)
    def visit(self, node: our_ast.AttrNode, scope):

        var = self.visit(node.value)

        return var


    @visitor.when(our_ast.IsVoidNode)
    def visit(self, node: our_ast.IsVoidNode, scope):
        var = self.visit(node.expr)

        type_expr = self.define_internal_local()
        self.register_instruction(cil_ast.TypeOfNode(type_expr, var))

        temp_rest = self.define_internal_local()

        self.register_instruction(cil_ast.MinusNode(temp_rest, type_expr,
                                                    'Void'))

        isnotvoid_label = cil_ast.LabelNode(f'isnotvoid_{self.is_void_counter}')
        endif_label = cil_ast.LabelNode(f'endif_{self.is_void_counter}')

        self.is_void_counter += 1

        temp_result = self.define_internal_local()
        self.register_instruction(cil_ast.IfNode(temp_rest, isnotvoid_label))
        self.register_instruction(cil_ast.AssignNode(temp_result, 1))
        self.register_instruction(cil_ast.GotoNode(endif_label))
        self.register_instruction(isnotvoid_label)
        self.register_instruction(cil_ast.AssignNode(temp_result, 0))
        self.register_instruction(endif_label)

        return temp_result


    @visitor.when(our_ast.NegationNode)
    def visit(self, node: our_ast.NegationNode, scope):

        var = self.visit(node.value)

        temp_a = self.define_internal_local()

        self.register_instruction(cil_ast.AssignNode(temp_a, (2**32) - 1))
        temp_result = self.define_internal_local()
        self.register_instruction(cil_ast.MinusNode(temp_result, temp_a, var))

        return temp_result


    @visitor.when(our_ast.SelfNode)
    def visit(self, node: our_ast.SelfNode, scope):
        return 'self'

    @visitor.when(our_ast.LetNode)
    def visit(self, node: our_ast.LetNode, scope: cil_scoper.CilScope):

        child_scope = scope.create_child()

        for assig in node.initializers:
            var = self.visit(assig.value, child_scope)

            local = self.register_local(assig.name)

            self.register_instruction(cil_ast.AssignNode(local, var))

        temp_result = self.visit(node.body, child_scope)

        return temp_result











