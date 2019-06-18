from collections import OrderedDict
from typing import List, Optional, Union, Dict

from code.front_end.our_ast import *
import itertools as itl


class SemanticAnalysisError(Exception):
    #Esception que voy a utilizar para detectar los errores semanticos, recive una lista de strings con los problemas y en su __str__ los imprime   
    def __init__(self, wrongs = ["Se encontraron errores semanticos"]):
        super()
        self.wrongs = wrongs
    def __str__(self):
        for bad in self.wrongs:
            print(bad)
            
            
#class TypeNode():
#    def __init__(self,astclassnode):
#        self.classnode = astclassnode
#        self.name = astclassnode.name
#        self.sons = []
#        
#    def add_child(self ,son):
#        #metodo que recibe una istancia de typesNodes para anadirla como como hijo.
#        self.sons.append(son)
#        son.parent = self
#    
    #def make_son_of(self,parent):
    #    self.parent = parent
    #    parent.add_child(self)
        
class TypesGraph():
    #Clase que va a facilitarme todo el manejo de la jerarquia de clases que detecto el parser. Ademas chequea algunos errores de tipo herencia y redefiniciones de metodos y demas.    
    #Tiene un LCA necesario para saber si una clase se conforma con otra necesario para el chequeo de tipos
    def __init__(self, programnode):
        self.program_node = programnode
        self.types_nodes: Dict[str, Classbook] = {} #diccionario de name de la clase en el typesNode
        self.built_in_types = {}#diccionario que continee los tipos bulit in que no se puede heredar de ellos, osea string, int y bool , porque de Object y de Io si se puede heredar. lo llena el metodo insert_built_in_types
        self.lca = {}#diccionario para hacer memoization con las querys de lca pedidas
        
        self.insert_built_in_types()
        self.built()
        
    def built(self):
        #metodo que va a contruir el grafo y dedecta errores de redifinicion de clases, herencia en tipos built in no permitida,ciclos de herencia, que no exista la clase Main con el metodo main y demas
        for clas in self.program_node.classes:
            if clas.name in self.types_nodes:
                
                #reportar error de que es esta redifiniendo una clase ya existe, puede seeer que sea una de las clases bulit in
                #todo ver como reportar el error y recuperarse de el
                mistake = "Existen dos definiciones de la clase " + str(clas.name) + " que no es permitido, tener en cuenta que existen clases built_in en Cool que no se pueden redefinir."
                raise SemanticAnalysisError([mistake])
            else:
                self.types_nodes[clas.name] = Classbook(clas)
        
        for name in self.types_nodes:
            current = self.types_nodes[name]
            if not current.parent.name in self.types_nodes:
                
                mistake = "La clase " + str(current.name) + " esta heredando de la clase padre " + str(current.parent.name) + " que no esta definida."
                #Reportar que estas heredando de alguien que no existe
                #todo ver como manejar el reportar el error
                raise SemanticAnalysisError([mistake])
            self.types_nodes[current.parent.name].add_child(current)
        
        visited = {}#diccionario que vamos a usar para hacer el bfs y comprobar que no existan ciclos
        visited["Object"] = True
        self.types_nodes["Object"].deph = 0
        pointer = 0
        cola = [self.types_nodes["Object"]]

        while pointer < len(cola):
            current = cola[pointer]
            current.check_redefinitions() # lo hago para chequear que las redifiniciones de esta clase esten bien. 
            pointer+=1
            for son in current.sons:
                if son.name in visited:
                    
                    mistake = "La herencia de la clase " + str(son.name) + " que hereda de " + str(current.name) + "genera un ciclo de herencia no permitido"
                    raise SemanticAnalysisError([mistake])
                else:
                    visited[son.name] = True
                    cola.append(son)
                    son.deph = current.deph +1
                    #current.add_child(son)
        if pointer != len(self.types_nodes):
            
            mistake = " Existe un ciclo de herencia no permitido debido a que la clase Object no es ancestro de todas las clases"
            raise SemanticAnalysisError([mistake])
            #reportar error de que se encontro un ciclo de herencia
            #todo ver como manejo detectar estos errores
            #Significa que no pudimos ver todos los nodos desde OBject por lo que hay ciclos
            
        for name in self.built_in_types:
            if name != "Object" and len(self.types_nodes[name].sons) != 0:
                
                mistake = "Se esta heredando de la clase built_in " + str(name) + " y esto no esta permitido"
                raise SemanticAnalysisError([mistake])
                #reportar que se heredo de uno de los tipos built in que no esta permitido
                #todo ver como manejar el reportar estos errores y recuperarse de ellos
                
        if not "Main" in self.types_nodes:
            mistake = "No existe una clase Main lo cual no esta permitido dado que para correr el codigo del programa se corre Main.main()"
            raise SemanticAnalysisError([mistake])
        if len(self.types_nodes["Main"].give_method("main")) > 1:
            mistake = "El metodo main de la clase Main no puede tomar parametros"
            raise SemanticAnalysisError([mistake])
    #TODO YET    
    def insert_built_in_types(self):
        #metodo donde voy a insertar los typesNodes de object, string y demas... en el types_nodes.
        pass
    
    def lowest_common_ancestor(self,classA,classB):
        #metodo que recibe dos clases y ddevuelve el LCA de estos.
        
        if isinstance(classA,ClassNode) and isinstance(classA,ClassNode):
            nameA = classA.name
            nameB = classB.name
            wantclasses = True
        else:
            nameA = classA
            nameB = classB
            wantclasses = False
        if self.types_nodes[nameA].deph > self.types_nodes[nameB].deph:
            #Aqui me aseguro que el que menor profundidad tenga sea A siempre
            temp = nameA
            nameA = nameB
            nameB = temp
        
        if (nameA,nameB) in self.lca:
            #si ya tengo guardado el resultado para esta query me ahorro calcularlo
            nameA = self.lca[(nameA,nameB)]
        else:
            A = nameA
            B = nameB
            #en caso de no tenerlo guardado lo calculo y despues lo guardo en lca como tup
            while nameA != nameB:
                if self.types_nodes[nameA].deph != self.types_nodes[nameB].deph:
                    nameB = self.types_nodes[nameB].parent.name
                else:
                    nameA = self.types_nodes[nameA].parent.name
                    nameB = self.types_nodes[nameB].parent.name
            self.lca[(A,B)] = nameA
        if wantclasses:
            #si me entraste las clases probablemente quierass las clases por lo que devuelvo una instancia de Ast.ClassNOde
            return self.types_nodes[nameA].classnode
        return nameA

    def conform(self,classA, classB):
        #Metodo que devuelve si la claseA se conforma a la claseB, osea si B es ancestro de A
        
        if self.lowest_common_ancestor(classA,classB) == classB:
            #Es tan simple como que si B es ancestro de A entonces su lca es igual a B necesariamente, es si y solo si.
            return True
        return False
    
    def class_exists (self,class_name):
        #metodo que devuelve si la clase class_name existe en el modulo
        return class_name in self.types_nodes
        
    def find_method_of(self,class_name, method_name, internal = False):
        #metodo que devuelve la signatura de class_name.method_name, return is ((name1,type1),(name2,type2)... (return,returntype))
        #Si no existe tal metodo en tal clase devuelve False
        
        if not class_name in self.types_nodes:
            return False
        return self.types_nodes[class_name].find_method(method_name,internal)

    def find_attr_of(self,class_name, attr_name,internal = False):
        #metodo que devuelve el type del atributo class_name.attr_name
        #si no existe tal atributo en la clase devuelve false
        
        if not attr_name in self.types_nodes[class_name]:
            return False
        return self.types_nodes[class_name].find_attr(attr_name,internal)


class Classbook():
    #Clase que va a facilitar trabajar con las signaturas de cada clase, digase la signatura de metodos y de atributos de estas clases. 
    def __init__(self, classNode):
        self.classNode = classNode
        self.methods = OrderedDict() #Diccionario de los metodos y su signatura que va a ser representada por una lista de tuplas [(name,type), (name,type)... (returnname,returntype)]
        self.attributes = OrderedDict() #dicionario de los atributos, de la forma (key,result) = (name,type)
        self.parent: 'Classbook' = None
        self.deph = 0
        self.name = classNode.name
        self.sons: List['Classbook'] = []
        self.built()

    def all_attributes(self, clean=True):
        plain = OrderedDict() if self.parent is None else self.parent.all_attributes(
            False)

        for attr in self.attributes.keys():
            plain[attr] = self.attributes[attr]

        return plain.values() if clean else plain

    def all_methods(self, clean=True):
        plain = OrderedDict() if self.parent is None else self.parent.all_methods(
            False)

        for method in self.methods.keys():
            plain[method.name] = self.methods[method]
        return plain.values() if clean else plain

    def built(self):
        #metodo que va a llenar los diccionarios de funciones y atributos de acuerdo al classNOde 
        wrongs = []
        for tuplex in self.classNode.attrs:
            if tuplex[0] in self.attributes:
                #reportar error de que esta redefinido el atributo dentro de la misma clase
                #todo ver como manejo el reportar este error
                mistake = "En la clase " + str(self.name) + " se redefine el atributo  con nombre " + str(tuplex[0]) + " que no esta permitido"
                wrongs.append(mistake)
            self.attributes[tuplex[0]] = tuplex[1]
        
        for method in self.classNode.methods:
            if method.name in self.methods:
                #reportar que se encontro una redefinicion dentro del propio metodo
                #todo ver como reporto el error
                mistake = "En la clase " + str(self.name ) + " se redefine el metodo con nombre " + str(method.name) + " y esto no esta permitido"
                wrongs.append(mistake)
                
            self.methods[method.name] = method.params + ("return",method.return_type)
        if len(wrongs) > 0:
            raise SemanticAnalysisError(wrongs)

    def give_method(self, func_name):
        #El busca local no en toda la jerarquia
        #Metodo que va a devolver, si existe la funcion, la signatura de esta, en caso de que no exista va a devolver false 
        if func_name in self.methods:
            return self.methods[func_name]
        return False

    def give_attribute(self, attr_name):
        #Busqueda local no en toda la jerarquia
        #Metodo que va a devolver la signatura(el tipo) de este atributo en caso de que exista, si no existe devuelve false
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        return False
    def find_attr(self,attr_name, internal = False):
        #busqueda del atributo en toda la jerarquia de clases, por todos los padres de la clase
        current = self
        while current.parent != None:
            if current.give_attribute(attr_name):
                if internal:
                    return (current.give_attribute(attr_name),current.name)
                return current.give_attribute(attr_name)
            current = current.parent
        if internal:
            return (current.give_attribute(attr_name),current.name)
        return current.give_attribute(attr_name)

    def find_method(self,method_name, internal = False):
        #metedo que devuelve la busqueda del method_name en toda la jerarquia hacia arriba para devolver la signatura, en caso de que no la encuentre return False
        current = self
        while current.parent != None:
            if current.give_method(method_name):
                if internal:
                    #es para el chequeo de redifiniciones usoo un flag para ver que tambien quiero el nombre de la clase para reportar errores
                    return (current.give_method(method_name), current.name)
                return current.give_method(method_name)
            current = current.parent
        if internal:
            return (current.give_method(method_name), current.name)
        return current.give_method(method_name)

    def add_child(self,son):
        #metodo para representar la jerarquia de clases y construirla.
        son.parent = self
        #son.deph = self.deph + 1
        self.sons.append(son)

    def check_redefinitions(self):
        #metodo que chequea si las redifiniciones en cuanto a la herencia en esta clase estan bien, osea que no este redifininedo ningun atributo de clases
        #superiores y que las redifiniciones de funciones tengan la misma signatura.
        #En caso de estar todo okey devuelve False, en caso de encontrar errores devuelve una lsita de strings con los problemas
        
        if self.parent == None:
            return False
        current = self.parent
        wrongs = []# lista que va a contener los strings de los errores que encontro
        for attr_name in self.attributes:
            find = current.find_attr(attr_name,internal = True)
            if find[0]:
                mistake = "Se encontro que el atributo = " + str(attr_name) + " en la clase " + str(self.name) + " esta haciendo una redifinicion no permitida del atributo con el mismo nombre de la ancestro con nombre " + str(find[1])
                wrongs.append(mistake)
                
        for method_name in self.methods:
            mine = self.methods[method_name]
            find = current.find_method(method_name,internal = True)
            if find[0]:
                
                if len(mine) != len(find):
                    mistake = "La signatura por la cantidad de parametros de la funcion con nombre " + str(method_name) + " en la clase " + str(self.name) + " no se corresponde con la redifinicion que se le esta haciendo al metodo con el mismo nombre de la clase ancestro " + str(find[1])
                    wrongs.append(mistake)
                else:
                    if find[1] == "IO":
                        #Aqui estamos viendo que de la clase IO no se puede redefinir los metodos, si se puede heredar pero no redefinir
                        mistake = "Se esta intentando redefinir un metodo de la clase IO y esto no esta permitido, si se puede heredar pero no redefinir"
                        wrongs.append(mistake)
                        continue
                    for i in range(len(find[0])):
                        if find[0][i][1] != mine[i][1]:
                            mistake = "En el metodo " + str(method_name) + " de la clase " + str(self.name) + " se hace una redifinicion incorrecta del metodo en la clase ancestro " + str(find[1]) + " debido a que cambia el tipo del parametro que tiene nombre en la clase que esta redifiniendo = " + str(find[0][i][0])
                            wrongs.append(mistake)
        if len(wrongs) > 0:
            raise SemanticAnalysisError(wrongs)
        return False
                            
class Scope:
    #clase que representa un scope, osea las variables que estan declaradas, tienen una estructura arborea para manejar las variables que ocultan nombres pasados.
    def __init__(self, types_graph, current_class, parent=None):
        self.locals = [] #Variables locales definidas en este scope
        self.types_graph = types_graph # Aqui types graph es una instancia de la clase homonima, que me da facilidades para manejar las clases, sus atributos, herencias, Lca y demas
        self.parent = parent #Referencia al scope padre
        self.current_class = current_class # nombre de la Clase actual donde esta comprendido el scope, necesario para el self type
        self.children = [] #Lista de scopes hijos de este scope
        self.index_at_parent = 0 if parent is None else len(parent.locals)

    def define_variable(self, vname, vtype):
        vinfo = VariableInfo(vname, vtype)
        self.locals.append(vinfo)
        return vinfo

    def create_child_scope(self):
        child_scope = Scope(self.types_graph, self.current_class)
        self.children.append(child_scope)
        return child_scope

    def is_defined(self, vname):
        return self.get_variable_info(vname) is not None
    
    def conform(self,classA,classB):
        #metodo para saber si dos clases se conforman, osea si B es ancestro de A.
        return self.types_graph.conform(classA,classB)
    def LCA(self,classA,classB):
        #metodo uqe devuelve el LCA entre las 2 clases, osea la clase mas cercana a ambos que sea ancestro comun de los 2.
        
        return self.types_graph.lowest_common_ancestor(classA,classB)
    def get_variable_info(self, vname):
        current = self
        top = len(self.locals)
        while current is not None:
            vinfo = Scope.find_variable_info(vname, current, top)
            if vinfo is not None:
                return vinfo
            top = current.index_at_parent
            current = current.parent
        return None

    def is_local(self, vname):
        return self.get_local_variable_info(vname) is not None

    def get_local_variable_info(self, vname):
        return Scope.find_variable_info(vname, self)

    @staticmethod
    def find_variable_info(vname, scope, top=None):
        if top is None:
            top = len(scope.locals)
        candidates = (vinfo for vinfo in itl.islice(scope.locals, top) if vinfo.name == vname)
        return next(candidates, None)
    
    def class_exits(self,class_name):
        #Metodo que devuelve si la clase con nombre class_name existe en el modulo de cool que estamos analizando
        return self.types_graph.class_exits(class_name)
    
    def find_method(self,class_name,method_name, internal = False):
        #Metodo que devuelve la signatura de la funcion de entrada en la clase de entrada, en caso de no existir devuelve false
        return self.types_graph.find_method(class_name,method_name,internal)
    
    def find_attr(self,class_name,attr_name, internal = False):
        #metodo que devuelve el tipo del atributo de entrada en la clase de entrada, en caso de no existir devuelve false
        return self.types_graph.find_attr(class_name,attr_name,internal)

class VariableInfo:
    def __init__(self, name, type = "Object"):
        self.name = name
        self.type: Union[Classbook, str] = type
        self.vmholder = None

    
    