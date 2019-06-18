import typing


types_node_list = typing.List['TypeNode']
data_node_list = typing.List['DataNode']
function_node_list = typing.List['FunctionNode']
attr_node_list = typing.List['AttrNode']
method_node_list = typing.List['MethodNode']
ins_node_list = typing.List['InstructionNode']
param_node_list = typing.List['ParamNode']
local_node_list = typing.List['LocalNode']
data = typing.Union[str, int] # algunas instrucciones pueden recivir tanto ctes
# como direcciones de memoria


class Node:
    pass


class ProgramNode(Node):

    def __init__(self, dottypes: types_node_list, dotdata: data_node_list,
                 dotcode: function_node_list):
        self.dottypes = dottypes
        self.dotdata = dotdata
        self.dotcode = dotcode


class TypeNode(Node):

    def __init__(self, tname: str, attrs: attr_node_list,
                 methods: method_node_list):
        # tener presente que tanto el nombre del methodo como el de los attr
        # van con el nombre del tipo delante por convencion para hacer mas facil
        # el encontrar a que tipo pertenece cada atributo o methodo
        self.tname = tname
        self.attrs = attrs
        self.methods = methods


class AttrNode(Node):

    def __init__(self, name: str):
        self.name = name


class MethodNode(Node):

    def __init__(self, name: str, fundest: str):
        # fundest: funcion a la que hacer referencia en la seccion .code
        self.name = name
        self.fundest = fundest


class DataNode(Node):

    def __init__(self, vname: str, value: str):
        self.vname = vname
        self.value = value


class FunctionNode(Node):

    def __init__(self, name: str, params: param_node_list,
                 localvars: local_node_list, instructions: ins_node_list):
        self.fname = name
        self.params = params
        self.localvars = localvars
        self.instructions = instructions


class ParamNode(Node):

    def __init__(self, destaddr: str):

        self.destaddr = destaddr


class LocalNode(Node):

    def __init__(self, destaddr: str):

        self.destaddr = destaddr


class InstructionNode(Node):
    pass


class AssignNode(InstructionNode):

    def __init__(self, destaddr: str, source):
        self.destaddr = destaddr
        self.source = source


class ArithmeticNode(InstructionNode):

    def __init__(self, destaddr: str, sleft: str, sright: str):
        self.destaddr = destaddr
        self.sleft = sleft
        self.sright = sright


class PlusNode(ArithmeticNode):
    pass


class MinusNode(ArithmeticNode):
    pass


class StarNode(ArithmeticNode):
    pass


class DivNode(ArithmeticNode):
    pass


# class BranchLessThanZeroNode(InstructionNode):
#
#     def __init__(self, saddr: str, label: str):
#         self.saddr = saddr
#         self.label = label


class TypeAttrInsNode(InstructionNode):

    def __init__(self, destaddr: str, typeaddr: str, attroffset: str):
        self.destattr = destaddr
        self.typeaddr = typeaddr
        self.attroffset = attroffset
        self.type = None

class GetAttrNode(TypeAttrInsNode):
    pass


class SetAttrNode(TypeAttrInsNode):
    pass


class ArrayIndexInsNode(InstructionNode):

    def __init__(self, destaddr: str, arrayaddr: str, offset: str):
        self.destaddr = destaddr
        self.arrayaddr = arrayaddr
        self.offset = offset


class GetIndexNode(ArrayIndexInsNode):
    pass


class SetIndexNode(ArrayIndexInsNode):
    pass


class AllocateNode(InstructionNode):

    def __init__(self, destaddr, typename: str):
        self.destaddr = destaddr
        self.typename = typename


class ArrayNode(InstructionNode):

    def __init__(self, destaddr: str, length: str):
        self.destaddr =  destaddr
        self.length = length


class TypeOfNode(InstructionNode):

    def __init__(self, destaddr: str, addr: str):
        self.destaddr = destaddr
        self.addr = addr


class LabelNode(InstructionNode):

    def __init__(self, label: str):
        self.label = label


class GotoNode(InstructionNode):

    def __init__(self, label: LabelNode):
        self.label = label


class IfNode(InstructionNode):

    def __init__(self, cond: str, label: LabelNode):
        self.cond = cond
        self.label = label


class StaticCallNode(InstructionNode):

    def __init__(self, destaddr: str, methodaddr: str):
        self.destaddr = destaddr
        self.methodaddr = methodaddr


class DinamicCallNode(InstructionNode):

    def __init__(self, destaddr: str, typeaddr: str, offset: str):
        self.destaddr = destaddr
        self.typeaddr = typeaddr
        self.offset = offset


class ArgNode(InstructionNode):

    def __init__(self, destaddr: str):
        self.destaddr = destaddr


class ReturnNode(InstructionNode):

    def __init__(self, addr: data=0):
        self.addr = addr


class LoadNode(InstructionNode):

    def __init__(self, destaddr: str, array: str):
        self.destaddr = destaddr
        self.array = array


class LengthNode(InstructionNode):

    def __init__(self, destaddr: str, arrayaddr: str):
        self.destaddr = destaddr
        self.arrayaddr = arrayaddr


class ConcatNode(InstructionNode):

    pass


class PrefixNode(InstructionNode):
    pass

class SubstringNode(InstructionNode):
    pass

class StrNode(InstructionNode):

    def __init__(self, destaddr: str,  value: str):
        self.destaddr = destaddr
        self.value = value


class ReadNode(InstructionNode):

    def __init__(self, destaddr: str):
        self.destaddr = destaddr


class PrintNode(InstructionNode):

    def __init__(self, straddr: str):
        self.straddr = straddr


class LessOrEqualThanNode(InstructionNode):

    def __init__(self, destaddr: str, sraddr1: str, sraddr2: str):

        self.destaddr = destaddr
        self.sraddr1 = sraddr1
        self.sraddr2 = sraddr2


class LessThanNode(InstructionNode):

    def __init__(self, destaddr: str, sraddr1: str, sraddr2: str):
        self.destaddr = destaddr
        self.sraddr1 = sraddr1
        self.sraddr2 = sraddr2


class EqualNode(InstructionNode):

    def __init__(self, destaddr: str, sraddr1: str, sraddr2: str):
        self.destaddr = destaddr
        self.sraddr1 = sraddr1
        self.sraddr2 = sraddr2


class NotNode(InstructionNode):

    def __init__(self, destaddr: str, sraddr: str):
        self.destaddr = destaddr
        self.sraddr = sraddr


class NegationNode(InstructionNode):

    def __init__(self, destaddr: str, sraddr: str):
        self.destaddr = destaddr
        self.sraddr = sraddr
