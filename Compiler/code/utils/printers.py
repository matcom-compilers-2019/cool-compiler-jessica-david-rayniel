from code.utils import visitor
from code.front_end import cil_ast


class MipsGenerator:

    def __init__(self):
        pass

    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(cil_ast.ProgramNode)
    def visit(self, node: cil_ast.ProgramNode):
        print('ProgramNode')


    @visitor.when(cil_ast.TypeNode)
    def visit(self, node: cil_ast.TypeNode):
        pass

    @visitor.when(cil_ast.AttrNode)
    def visit(self,node: cil_ast.AttrNode):
        pass

    @visitor.when(cil_ast.DataNode)
    def visit(self, node: cil_ast.DataNode):
        pass

    @visitor.when(cil_ast.FunctionNode)
    def visit(self, node: cil_ast.FunctionNode):
        pass

    @visitor.when(cil_ast.ParamNode)
    def visit(self, node: cil_ast.ParamNode):
        pass

    @visitor.when(cil_ast.LocalNode)
    def visit(self, node: cil_ast.LocalNode):
        pass

    @visitor.when(cil_ast.InstructionNode)
    def visit(self, node: cil_ast.InstructionNode):
        pass

    @visitor.when(cil_ast.AssignNode)
    def visit(self, node: cil_ast.AssignNode):
        pass

    @visitor.when(cil_ast.ArithmeticNode)
    def visit(self, node: cil_ast.ArithmeticNode):
        pass

    @visitor.when(cil_ast.PlusNode)
    def visit(self, node: cil_ast.PlusNode):
        pass

    @visitor.when(cil_ast.MinusNode)
    def visit(self, node: cil_ast.MinusNode):
        pass

    @visitor.when(cil_ast.StarNode)
    def visit(self, node: cil_ast.StarNode):
        pass

    @visitor.when(cil_ast.DivNode)
    def visit(self, node: cil_ast.DivNode):
        pass

    @visitor.when(cil_ast.TypeAttrInsNode)
    def visit(self, node: cil_ast.TypeAttrInsNode):
        pass

    @visitor.when(cil_ast.GetAttrNode)
    def visit(self, node: cil_ast.GetAttrNode):
        pass
    @visitor.when(cil_ast.SetAttrNode)
    def visit(self, node: cil_ast.SetAttrNode):
        pass

    @visitor.when(cil_ast.ArrayIndexInsNode)
    def visit(self, node: cil_ast.ArrayIndexInsNode):
        pass

    @visitor.when(cil_ast.GetIndexNode)
    def visit(self, node: cil_ast.GetIndexNode):
        pass

    @visitor.when(cil_ast.SetIndexNode)
    def visit(self, node: cil_ast.SetIndexNode):
        pass

    @visitor.when(cil_ast.AllocateNode)
    def visit(self, node: cil_ast.AllocateNode):
        pass

    @visitor.when(cil_ast.ArrayNode)
    def visit(self, node: cil_ast.ArrayNode):
        pass

    @visitor.when(cil_ast.TypeOfNode)
    def visit(self, node: cil_ast.TypeOfNode):
        pass

    @visitor.when(cil_ast.LabelNode)
    def visit(self, node: cil_ast.LabelNode):
        pass

    @visitor.when(cil_ast.GotoNode)
    def visit(self, node: cil_ast.GotoNode):
        pass

    @visitor.when(cil_ast.IfNode)
    def visit(self, node: cil_ast.IfNode):
        pass

    @visitor.when(cil_ast.StaticCallNode)
    def visit(self, node: cil_ast.StaticCallNode):
        pass

    @visitor.when(cil_ast.DinamicCallNode)
    def visit(self, node: cil_ast.DinamicCallNode):
        pass

    @visitor.when(cil_ast.ReturnNode)
    def visit(self, node: cil_ast.ReturnNode):
        pass

    @visitor.when(cil_ast.LoadNode)
    def visit(self, node: cil_ast.LocalNode):
        pass

    @visitor.when(cil_ast.ReadStrNode)
    def visit(self, node: cil_ast.ReadStrNode):
        pass

    @visitor.when(cil_ast.PrintStrNode)
    def visit(self, node: cil_ast.PrintStrNode):
        pass

    @visitor.when(cil_ast.ReadIntNode)
    def visit(self, node: cil_ast.ReadIntNode):
        pass

    @visitor.when(cil_ast.PrintIntNode)
    def visit(self, node: cil_ast.PrintIntNode):
        pass

    @visitor.when(cil_ast.LessOrEqualThanNode)
    def visit(self, node: cil_ast.LessOrEqualThanNode):
        pass

    @visitor.when(cil_ast.LessThanNode)
    def visit(self, node: cil_ast.LessThanNode):
        pass

    @visitor.when(cil_ast.EqualNode)
    def visit(self, node: cil_ast.EqualNode):
        pass

    @visitor.when(cil_ast.GreatherOrEqualThanNode)
    def visit(self, node: cil_ast.GreatherOrEqualThanNode):
        pass

    @visitor.when(cil_ast.AndNode)
    def visit(self, node: cil_ast):
        pass

    @visitor.when(cil_ast.NotNode)
    def visit(self, node: cil_ast.NotNode):
        pass

    @visitor.when(cil_ast.NegationNode)
    def visit(self, node: cil_ast.NegationNode):
        print('neg' + str())

    @visitor.when(cil_ast.SuperSetAttrNode)
    def visit(self, node: cil_ast.SuperSetAttrNode):
       print('SuperSetAttr')

    @visitor.when(cil_ast.AbortNode)
    def visit(self, node: cil_ast.AbortNode):
       print('Abort')

    @visitor.when(cil_ast.ExceptNode)
    def visit(self, node: cil_ast.ExceptNode):
        print('Except')
