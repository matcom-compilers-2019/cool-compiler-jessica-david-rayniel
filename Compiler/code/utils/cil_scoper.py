from typing import List, Dict, Tuple, Optional


class CilScope:

    def __init__(self, parent: 'CilScope' = None):
        self.locals: Dict[str, str] = {}
        self.parent = parent
        self.children: List['CilScope'] = []

    def create_child(self) -> 'CilScope':
        child = CilScope(self)
        child.locals = {vname: vcilname
                        for vname, vcilname in self.locals.items()}

        self.children.append(child)
        return child

    def define_variable(self, vname: str, vcilname: str) -> Tuple[str, str]:
        self.locals[vname] = vcilname
        return (vname, vcilname,)

    def find_variable(self, vname: str) -> Optional[Tuple[str, str]]:
        if vname in self.locals.keys(): return (vname, self.locals[vname],)
        elif self.parent: return self.parent.find_variable(vname)

        return None

    def is_defined(self, vname: str) -> bool:
        return self.find_variable(vname) is not None

    def is_local(self, vname: str) -> bool:
        return vname in self.locals.keys()
