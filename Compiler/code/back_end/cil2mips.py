from code.front_end.cil_ast import *
#from our_ast import *
import code.utils.visitor as visitor

class MipsGenerator:

    def __init__(self, program_cil_node , types):
        self.program_cil_node = program_cil_node
        self.mains = []
        self.instructions = [] #lista de strings que va a contener las instrucciones en linea.

        self.super_nodes = {} #diccionario de (line, method_name) que va a marcar que en la line hay un super_node, despues de generar todo el codigo tengo que ir a estas posiciones y poner los numeros correctos a estos super_label de acuerdo a la posicion real que tienen los label de estas funciones en el codigo generado de mips

        self.methods_line = {} #diccionario de (label_de_method, line) para marcar que la funcion con nombre label_method esta en line de las instrucciones mips

        self.comments = {} #dicciorario de (line,comment) para poner que en line hay un comment para poner en la generacion de codigo, esto para hacer mas claro el debugeo despues

        self.number = 0 #numero unico que utilizo para desambiguar en nombres y label al pedirlo con el metodo give_unic_number este lo aumenta en 1 y retorna garantizando dar un numero distinto siempre

        self.label = {} # es un diccionario de (label,line) que me dice en que linea de codigo esta cada label que ponga.

        self.global_controler = None

        self.int_constants = {} # es un diccionario de string a int, de nombre de la variable globla que va a estar en la punto data, de esto se encarga el add_constant de llenarla para despues poder en la punto data poner todo su contenido

        self.twopower31 = "mips_constant_1" # Aqui guardo el nombre en especial de la variable 2**31 para el caso del not que me hace falata, parche un poco cochino pero bueno

        self.types = types#Esta es la estructura que voy a utilizar para hacer el dinamic dispatch
        self.types.get_attrs()# Estos metodos son los que ponen los valores que quiero que tengan en los diccionarios correspondientes de esta clase
        self.types.get_methods()
        self.global_controler = Global_Variables_Controler()

    def __show__(self):

        print("Vamos a mostrar los contenidos del Mips Generator:")
        print("Empezamos por el global controler")
        self.global_controler.__show__()
        print("Ya terminamos de mostrar el global controler")
        print("Tiene " + str(len(self.methods_line)) + " funciones mapeadas a su posicion en la linea de codigo en el self.instruccion, vamos a listarlar")
        for m in self.methods_line:
            print(m + "  :  " + str(self.methods_line[m]))

        print("Su numero unico actualmente es " + str(self.number))
        print("Vamos a listar las instrucciones :::")
        print("Tiene " + str(len(self.instructions)) + " instrucciones")
        for i in range(len(self.instructions)):
            print("Line = " + str(i+1) + "-> " + self.instructions[i])

    def generate(self):

        #metodo que pone a correr la generacion de codigo que va a llenar el self.instructions que va a contener la lista de instrucciones que va a representar el codigo en cil que es respuesta
        self.add_constant_att_dot_data(2**31) # Aqui pongo como la primera variable en la punto data y por tanto con el nombre + 1
        #print("**********-----***********")
        #print(type(self.program_cil_node))
        #print(self.program_cil_node)
        self.visit(self.program_cil_node,None)

    def add_constant_att_dot_data(self, value):
        #metodo que agrega una variable statica al .data como un valor numerico igual a value, devuelve un string con su nombre, garantiza nombres unicos
        #todo yet
        #este metodo tambien registra la variable al global_controler para que se pueda mover como es devido

        unic_var_name = "mips_constant_" + str(self.give_unic_number())
        self.global_controler.register_global_var(unic_var_name, value)#registro el nombre de la variable en el global controler para que el sepa como acceder a esta memoria
        self.int_constants[unic_var_name] = value
        return unic_var_name

    def give_unic_number(self):
        #metodo que voy a utilizar para desambiguar en nombres al pedirle un numero unico al final que va aumentando de 1 en 1
        self.number += 1
        return self.number

    @visitor.on('node')
    def visit(self, node, local_controler: "Local_Fp_Controler"):
        #Aqui pongo a correr la sobrecarga sobre el parametro 'node' para utilizar el patron visitor.
        pass

    @visitor.when(ProgramNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #todo ver que aqui hay que poner la referencia al self.global_controler correctamente, no muy dificil.
        #self.global_controler = Global_Variables_Controler()
        #print("LLamado al visitor de progtam")
        for data in node.dotdata:
            #Por los strings en .data los registro en el global controler
            self.global_controler.register_global_str(data.vname,data.value)

        #Voy a registrar a la punto data los 2 strings especiales que comunican el abort y el except
        self.abort_message_name = "mips_abort_message_of_mine"
        abort_value = "\"Se salio de la ejecucion debido a un abort de object\""
        self.except_message_name = "mips_except_message_of_mine"
        except_value = "\"Runtime Error, debido a algun error\""
        self.global_controler.register_global_str(self.abort_message_name,abort_value)#los registro
        self.global_controler.register_global_str(self.except_message_name, except_value)#los registro


        # Aqui voy a encapsular toda la seccion de .text
        func_lines = [".text"] # La primera del codigo es .text
        func_names = []#Aqui van a estar las funcioens en orden en que se expandieron, y por tanto en el orden en que se encuentran en las instructions
        for func in node.dotcode:
            func_names.append(func.fname)
            func_lines += self.visit(func,None)#Aqui voy concatenando el resultado de las lineas de cada fnucion

        data_lines = [".data"]
        data_lines += self.global_controler.give_dot_data_text()# Aqui el carga todo el codigo de la punto data, que al antes ya haber corrido los visitores en las funciones las constantes de int ya estan registradas.
        #print("*************VAMOS ahora a poner las instruccionesssssss en el visitor de program")
        self.instructions = data_lines + func_lines # Ya aqui tengo las instrucciones
        #Ahora vamos a manejar el tema de los super_setattr que tienen que guardar la linea de codigo en que estan las funciones en la virtual_table
        super_set_positions = []#Aqui voy a guardar la posicion en las istrucciones en que estan los super_setaattr, con esto voy a sustituir por el codigo que correspode
        count = 0
        #print(self.instructions)
        #print("DONNNEEEE!!!!!!!!!!!!!!!!!!!")
        for i in range(len(self.instructions)):
            #print("instruccion en [i ] = " + str(i) + " es " + str(self.instructions[i]))
            if isinstance(self.instructions[i], tuple):
                #Si es un super setar que es el unico que seria una tupla,que vienen de 3 en 3 las ignoro y guardo la posicion para despues llamar a do_super_set_attr
                super_set_positions.append(i)
                i+=2
            else:
                #Si no es un super_setattr voy a buscar las posiciones en que estan las funciones para mapearlas.
                if self.instructions[i][0] == '.' and self.instructions[i][1] == 'g':
                    #La unica instruccion que comienza con .g es global, despues de esta instruccion 2 pos mas arriba esta el label de la funcion, lo guardo
                    self.methods_line[func_names[count]] = i + 3 # Aqui ver que como las instrucciones comienzan en 0 y 2 lineas despues del global esta la etiqueta de la funcion
                    count+=1
        for index in super_set_positions:
            if isinstance(self.instructions[index],tuple):
                self.do_super_set_attr(self.instructions[index][0], self.instructions[index][1],index) # LLamar en la tupla en 0 tiene el CilNode SuperSetAttr y en 1 la referencia al local_controler que tenia en el momento en que se llamo

    @visitor.when(TypeNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #creo qu no hace falta
        return []

    @visitor.when(AttrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):#No sirve no hay que hacerlo
        #no sirve para nada
        return []

#    @visitor.when(MethodNode, local_controler: "Local_Fp_Controler"):
#    def visit(self,node):
#        #en teoria no me hace falta
#        pass

    @visitor.when(DataNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #sencillo tambien, es guardar los strings con el .ascii y reportar los nombres al global_controler
        #tener en cuenta poner los 2 strings constantes con los nombres unicos y fijos. Ver bien como hacer eso. Para cuando se haga abort o se haga exception escribirlos
        #utilizando un print node.
        #return (node.vname, node.value) # En este caso voy a retornar la tupla con el nombre de la variabe y el valor.

        #Creo que no hace falta, simplemete voy a recorrer la lista de nodos de este tipo capturando la tupla de vname, value para registrarlos en el global_controler.
        return []

    @visitor.when(FunctionNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #es bastante simple crear el local_controler con los params y los locals, y el resultado es prefix + body + suffix
        params = [(p_node.destaddr) for p_node in node.params] # Aqui obtengola lista con los nombre de todos los parametros
        locals = [(l_node.destaddr) for l_node in node.localvars]
        print("--------------------------- estamos en la funcion con nombre " + str(node.fname) + " ---------------------------------")
        t_local_controler = Local_Fp_Controler(params,locals,self.global_controler) # Aqui instancio al local controler
        lin00 = "    " # linea en blanco para mas claridad en el codigo de separacion entre las funciones
        line0 = ".globl   " + str(node.fname)
        line1 = ".ent     " + str(node.fname)
        line2 = str(node.fname) + ":"
        #print("creo los globl y demas cositas")
        #print("##########################**********************##################*********************######################*******************")
        #t_local_controler.__show__()
        #print("##########################**********************##################*********************######################*******************")
        begin_lines = [lin00,line0,line1,line2]
        body_lines = []
        #print("Vamos a llamar a las instrucciones")
        #print(node.instructions)
        for instruc in node.instructions:
            #print(instruc)
            #print(type(instruc))
            #print(body_lines)
            current_to_add = self.visit(instruc, t_local_controler)
            if current_to_add == None:
                print("EStamos haciendo print a un current vacio, osea hay una funcion que tiene cuerpo vacio, raro revisar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                continue
        #        print("CAAAAAAOOOOOOOTTTIIIIIICCCOOOOOOOOOOOOO**************************!!!!!!!!!!!!!!!!!!!!!!!!!")
        #   print("el visitor me dijo que va a agregar lo sigueitne ((@($*(#*(*$")
        #   print(current_to_add)
            body_lines += current_to_add
        prefix_lines = t_local_controler.give_prefix_of_calling()
        entry = False
        if node.fname == "main":
            entry = True
        sufix_lines = t_local_controler.give_suffix_of_calling(entry) # Caso de ponerle que no haga el jr
        #print("YA cree los fijos de los sufijos y prefijos--------------")
        if node.fname == "main":
            #Si es la primera funcion tengo que hacer exit al final
            f_line1 = "li $v0, 10"
            f_line2 = "syscall"
            f_line3 = ".end " + str(node.fname)
            final_lines = [f_line1,f_line2,f_line3]
        else:
            #EN caso de no ser la primera funcion solo tengo que poner el .end con el nombre de la funcion
            f_line1 = ".end " + str(node.fname)
            final_lines = [f_line1]
        #El resultado es igual a las begin lines que son las de declaracion del metodo y demas, + prefix_lines que son las lineas de liberarr espacio en la pila para los
        #locales y guardar los registros y demas, las lineas del cuerpo de la funcion, las lineas de sufijo que son las que restauran los registros y ponen la pila en su posicion inicial y luego las lineas
        #finales que lo que hacen es poner el .end y en caso de ser la primera funcion hacer el exit.
        return begin_lines + prefix_lines + body_lines + sufix_lines + final_lines

    @visitor.when(ParamNode)#No me hace fatla
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #es para tener el nombre nada mas y pasarselo como constructor al local_controler
        return []

    @visitor.when(LocalNode)#No me hace falta
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #es para saber el nombre nada mas y pasarselo al constructor del local_controler
        return []

    @visitor.when(InstructionNode)#No me hace falta
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Todo ver bien que es esto
        #no me hace falta hacerlo
        return []

    @visitor.when(AssignNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #basicamente pongo la variable source en t0 y depues pongo t0 en el destino
        #print("Estamos en un assing node que me estan pasando como parametros dest " +  str(node.destaddr) + " y tiene source = " + str(node.source))
        lines = []
        if isinstance(node.source,int):
            #si es de tipo int, sugnifica que es una constante, la pongo en la registro en la punto data con el valor pedido y la cargo a a t0
            constant_name = self.add_constant_att_dot_data(node.source)
        #    print("el nombre de la constante es " + str(constant_name))
        #    print("antes " + str(lines))
            lines += local_controler.load_var("$t0" , constant_name)
        #    print("despues " + str(lines))
        else:
            #si es un string significa que es una variable que esta en la pila o la memoria estatica, por lo que el load_var va a saber copiar su contenido a t0
            if not isinstance(node.source,str):
                print("Me estan pasando un bicho raro que seraaa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(type(node.source))
                print(node.source.__class__)
            if not local_controler.is_local(node.source):
                print("Me estan pasando una variable que no tengo que se llama " + str(node.source)+  " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                local_controler.__show__()
                print(type(node.source))
                print(node.source.__class__)
            lines += local_controler.load_var("$t0", node.source)
        lines += local_controler.save_var("$t0", node.destaddr) #Ya en t0 esta el valor pedido por lo que simplemente la pongo su valor en donde va.
        #print(lines)
        return lines

    @visitor.when(ArithmeticNode)#no es necesario
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        return []

    @visitor.when(PlusNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #print("nodo suma con dest,slef,srigth = " + str(node.destaddr) + " " + str(node.sleft) + " " + str(node.sright))
        lines = []
        lines += local_controler.load_var("$t0",node.sleft)
        lines += local_controler.load_var("$t1", node.sright)
        lines += ["addu $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(MinusNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #print("nodo rest con dest,slef,srigth = " + str(node.destaddr) + " " + str(node.sleft) + " " + str(node.sright))
        lines = []
        lines += local_controler.load_var("$t0", node.sleft)
        lines += local_controler.load_var("$t1", node.sright)
        lines += ["subu $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(StarNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #print("nodo mul con dest,slef,srigth = " + str(node.destaddr) + " " + str(node.sleft) + " " + str(node.sright))
        lines = []
        lines += local_controler.load_var("$t0", node.sleft)
        lines += local_controler.load_var("$t1", node.sright)
        lines += ["mul $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(DivNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):

        #print("nodo div con dest,slef,srigth = " + str(node.destaddr) + " " + str(node.sleft) + " " + str(node.sright))
        lines = []
        lines += local_controler.load_var("$t0", node.sleft)
        lines += local_controler.load_var("$t1", node.sright)
        lines += ["div $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(TypeAttrInsNode)#no es necesario
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        return []

    @visitor.when(GetAttrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Aqui tengo que desambiguar porque si el offset es una variable o una constante, la unica diferencia es que tengo que cargar la variable o no.
        #print("Nodo getattr con typeadd, attoffset,dest = " + str(node.typeaddr) + " " + str(node.attroffset) + " " + str(node.destattr))
        lines = []
        lines += local_controler.load_var("$t0", node.typeaddr)
        if isinstance(node.attroffset, int):
            #caso en que el offset es una constante, la cargamos a $t1 con un move
            constant_offset = self.add_constant_att_dot_data(node.attroffset)#aqui registro una variable a la punto data como una variable que contiene este valor, el metodo me devuelve el

            lines += local_controler.load_var("$t1" , constant_offset) # en esta linea guardo el offset en t1

        else:
            lines += local_controler.load_var("$t1" , node.attroffset)
        lines += ["sll $t1, $t1, 2"] #se quierre multiplicar el offset por 4 # TODO REVISAR  BIEN si estoy haciendo el shift left adecuadamente, que en teoria si, si hago shift left con 2 estoy multiplicando por 4
        lines += ["addu $t1, $t1 , $t0"]  # en esta al sumar el offset ccon la direccion del objeto obtengo en t1 la direccion a la cual se va a cargar la palabra
        lines += ["lw $t2, 0($t1)"] # en esta linea cargo a t2 el valor del get
        lines += local_controler.save_var("$t2", node.destattr) #En esta linea guardo el valor de t2 que tiene el get en el destino.
        return lines

    @visitor.when(SetAttrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #TODO ver si funciona la forma en que lo estoy viendo de que siempre los get y los set esperan poner y guardar algo que esta en la pila o en la punto data,(que podria dar bateo pues estoy utilizando el local de guardar o cargar para poner o quitar segun corresponda) que creo que si esta bien. Revisar
        # Aqui tengo que desambiguar porque si el offset es una variable o una constante, la unica diferencia es que tengo que cargar la variable o no.
        #print("Nodo setattr con typeadd, attoffset,dest = " + str(node.typeaddr) + " " + str(node.attroffset) + " " + str(node.destattr))
        lines = []
        lines += local_controler.load_var("$t0", node.typeaddr)
        if isinstance(node.attroffset, int):
            # caso en que el offset es una constante, la cargamos a $t1 con un move
            constant_offset = self.add_constant_att_dot_data(node.attroffset)  # aqui registro una variable a la punto data como una variable que contiene este valor, el metodo me devuelve el
            lines += local_controler.load_var("$t1", constant_offset)  # en esta linea guardo el offset en t1
        else:
            lines += local_controler.load_var("$t1", node.attroffset)
        lines += ["sll $t1, $t1, 2"]  # se quierre multiplicar el offset por 4 # TODO REVISAR  BIEN si estoy haciendo el shift left adecuadamente, que en teoria si, si hago shift left con 2 estoy multiplicando por 4
        lines += ["addu $t1, $t1 , $t0"]  # en esta al sumar el offset ccon la direccion del objeto obtengo en t1 la direccion a la cual se va a cargar la palabra
        if isinstance(node.destattr,int):
            constant_name = self.add_constant_att_dot_data(node.destattr)
            lines+= ["lw $t2, " + str(constant_name)]#Si lo que hay que setear es un int entonces lo cargo directamente a la punto data, y despues lo pongo en $t2
        else:
            lines += local_controler.load_var("$t2",node.destattr) # aqui cargo en t2 lo que quiero setiar
        lines += ["sw  $t2, 0($t1)"] #Aqui pongo lo que esta en t2,que es lo que  quiero setiar en la direccion resultante de sumar el offset mas la direccion que esta en t1.
        return lines

    def do_super_set_attr(self,super_node ,local_controler, index):
        #Este metodo se va a encargar de cambiar el self.instructions en las posiciones empezando en index
        #print("super.type = " + str(super_node.type))
        #print("las keys + " + str(self.types.methods[super_node.type].keys()) )
        #print("EL index es = " + str(index))
        #print(type(super_node))
        #print(super_node)
        offset = self.types.methods[super_node.type][super_node.method_name][1] * 4 # Aqui tengo el offset donde quiero hacer set

        lines = []
        lines += local_controler.load_var("$t0", super_node.vtable)# cargo la direccion de la virtual table
        #method_line = self.methods_line[super_node.fname] # Aqui cargo como constante la linea de codigo donde esta la funcion que quiere guardar el super_set
        lines += ["la $t1, " + super_node.fname] # pongo el valor de la linea de codigo mips en t1
        lines += ["sw $t1, " + str(offset) + "($t0)"]#guardo el valor de la linea de mips en

        #Ya aqui tengo en lines las 3 lineas de codigo que son el setattr
        for i in range(index,index + 3):
            self.instructions[i] = lines[i-index]


    @visitor.when(ArrayIndexInsNode)#NO me hace falta
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #todo ver que es esto
        return []

    @visitor.when(GetIndexNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Esencialmente lo mismo que el gettattr solo que el offset no lo tengo que multiplicar por 4 al querer trabajar con bytes, y a la hora de trabajar con la memoria lo hago con lb, sb y no lw sw.
        #print("Nodo getindex con arrayaddr,offset,dest = " + str(node.arrayaddr) + " " + str(node.offset) + " " + str(node.destaddr))
        lines = []
        lines += local_controler.load_var("$t0", node.arrayaddr)
        if isinstance(node.offset, int):
            # caso en que el offset es una constante, la cargamos a $t1 con un move
            constant_offset = self.add_constant_att_dot_data(node.offset)  # aqui registro una variable a la punto data como una variable que contiene este valor, el metodo me devuelve el

            lines += local_controler.load_var("$t1", constant_offset)  # en esta linea guardo el offset en t1

        else:
            lines += local_controler.load_var("$t1", node.offset)
        lines += ["addu $t1, $t1 , $t0"]  # en esta al sumar el offset ccon la direccion del objeto obtengo en t1 la direccion a la cual se va a cargar la palabra
        lines += ["li $t2, 0"] # puse esto aqui por que no me queda claro que el lb funcione y ponga en cero el resto de los bytes.
        lines += ["lb $t2, 0($t1)"]  # en esta linea cargo a t2 el valor del get,#tener en cuenta que en este caso lo hago cargando un byte
        #TODO revisar que lb funcione como espero, osea que carge el byte pero que t2 se vuelva la
        lines += local_controler.save_var("$t2",node.destaddr)  # En esta linea guardo el valor de t2 que tiene el get en el destino.
        return lines

    @visitor.when(SetIndexNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Lo mismo trabajar con bytes y word, osea no multiplico por 4 el offset y ademas
        #print("Nodo setindex con arrayaddr,offset,dest = " + str(node.arrayaddr) + " " + str(node.offset) + " " + str(node.destaddr))
        lines = []
        lines += local_controler.load_var("$t0", node.arrayaddr)
        if isinstance(node.offset, int):
            # caso en que el offset es una constante, la cargamos a $t1 con un move
            constant_offset = self.add_constant_att_dot_data(node.offset)  # aqui registro una variable a la punto data como una variable que contiene este valor, el metodo me devuelve el
            lines += local_controler.load_var("$t1", constant_offset)  # en esta linea guardo el offset en t1
        else:
            #Caso en que el offset ya esta en una variable en la pila o estatica en .data
            lines += local_controler.load_var("$t1", node.offset)
        lines += ["addu $t1, $t1 , $t0"]  # en esta al sumar el offset ccon la direccion del objeto obtengo en t1 la direccion a la cual se va a cargar la palabra
        lines += local_controler.load_var("$t2", node.destaddr)  # aqui cargo en t2 lo que quiero setiar
        lines += ["sb  $t2, 0($t1)"]  # Aqui pongo lo que esta en t2,que es lo que  quiero setiar en la direccion resultante de sumar el offset mas la direccion que esta en t1.
        return lines

    @visitor.when(AllocateNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Tener en cuenta que se quiere el tamano que me pasa el node por 4, al ser word, la cantidad de bytes es por 4.
        lines = []
        lines += ["move $t5, $a0"]# tener en cuenta aqui que hago lo de guardar a0 porque lo modifico y es una variable que contiene potencialmente un parametro.
        #print("Allocate el tipesize que me pasaron es = " +  str(node.typesize))
        if isinstance(node.typesize,int):
            #si es un int es que es una constante lo cargo
            const_name = self.add_constant_att_dot_data(node.typesize)
        #    print("En el allocate, agrege el tipo a la lista de variables globales statics")
            lines += local_controler.load_var("$a0" , const_name)# procedimiento de agregar la constante a la punto data y despues cargarla a ao
        else:
            #si es stirng es que es una variable por lo que el local_cintrloer sabe que hacer con el para cargarlo a a0
        #    print("El nombre que me pasaron es = " + str(node.typesize))
            lines += local_controler.load_var("$a0", node.typesize)#guardo en a0 el tamano pedido para despues multiplicarlo por 4
        lines += ["sll $a0, $a0, 2"] # lo multiplicamos por 4
        lines += ["li $v0, 9"] # pongo en v0 la instruccion que quiero para hacer llamada a system, que en este caso es la 9.
        lines += ["syscall"] # llamo a la funcion que me pone automaticamente en v0 el valor pedido
        lines += local_controler.save_var("$v0" , node.destaddr) # En esta linea pongo en el destino el puntero que contiene el allocate.
        lines += ["move $a0, $t5"]
        return lines

    @visitor.when(ArrayNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Esencialmente lo mismo que el allocate solo que si se pide en cantidad de bytes y no en cantidad de word, por lo que no multiplico por 4. Lo demas es lo mismo
        lines = []
        #print("array node con length,desta = " + str(node.length) + " " + str(node.destaddr))
        lines += ["move $t5, $a0"] # again hago esto porque a0 lo modifico aqui y potencialmente contiene el primer parametro de la funcion actual
        if isinstance(node.length,int):
            #similar si es un int, la reporto como variable en la punto data y la cargo despeus
            const_name = self.add_constant_att_dot_data(node.length)
            lines += local_controler.load_var("$a0", const_name)
        else:
            #Si es una variable ya el local sabe ponerla en a0
            lines += local_controler.load_var("$a0",node.length)  # guardo en a0 el tamano pedido para despues multiplicarlo por 4
        lines += ["li $v0, 9"]  # pongo en v0 la instruccion que quiero para hacer llamada a system, que en este caso es la 9.
        lines += ["syscall"]  # llamo a la funcion que me pone automaticamente en v0 el valor pedido
        lines += local_controler.save_var("$v0",node.destaddr)  # En esta linea pongo en el destino el puntero que contiene el allocate.
        lines += ["move $a0, $t5 "]
        return lines

    @visitor.when(TypeOfNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #creo que no se usa, hay que ver
        return []

    @visitor.when(LabelNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #simplemente pongo el label y ya
        line1 = str(node.label) + ":" # ver bien si aqui ya el string que el me da viene con el : para ver si lo tengo que poner o no. no deberia venir con los 2 puntos, ver
        return [line1]

    @visitor.when(GotoNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #aparentemente el node.label es una instancia de LabelNode por lo que para acceder al label tengo que hacer node.label.label, revisar bien
        line1 = "j " + str(node.label.label) # aqui lo mismo ver si el label viene con los 2 puntos o no.
        return [line1]

    @visitor.when(IfNode) #aparentemente no hay if.
    def visit(self,node, local_controler):
        #ver si es necesario, que supongo que si lo es, sencillo, con label y expandir el codigo entre los labels
        lines = []
        lines += local_controler.load_var("$t0", node.cond)
        lines += ["bnez $t0, " + str(node.label.label)]
        return lines

    @visitor.when(StaticCallNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Esta creo que es un simple jal para guardar el ra
        #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #print("Llamada al staticCallNode con args, methodaddr,dest = " + str(node.args) + " " + str(node.methodaddr) + " " + str(node.destaddr))
        args = node.args
        lines = [] # lista de lineas de codigo
        #lines += "move $s0, $a0"#Aqui estoy guardando los ax, pues en el llamado a otra funcion estos parametros se borran y no se quiere que esto pase
        #lines += "move $s1, $a1"
        #lines += "move $s2, $a2"
        #lines += "move $s3, $a3"

        for i in range(len(args)):
            if i <= 3:
                lines += local_controler.load_var(("$a" + str(i)), args[i])
        if len(args) > 4:
            for i in range(4,len(args)):
                index = i-4
                lines += local_controler.load_var(("$t" + str(index)),args[i])
        if len(args) > 4:
            many = (len(args) - 4)*4 # aqui tengo la cantidad de bytes que voy a mover la pila para pasar el resto de los argumentos
            subu_line = "subu $sp, $sp" + str(many)
            lines += [subu_line]
            for i in range(4,len(args)):
                offset = (i - 4)*4
                #lines += local_controler.load_var("$t0", args[i]) #TODO ver aqui hay un bateo, porque estoy cargando una variable local sin tener en cuenta que ya modifique la pila por lo que los offset no van a set iguales
                index = i-4
                lines += ["sw $t" + str(index) + ", "  +  +str(offset) + "($sp)"]
        self.mains.append(node.methodaddr)
        lines += ["jal " + str(node.methodaddr)] #ver que al llamar se supone que la funcion en el return ponga en v0 el valor de retorno
        lines += local_controler.save_var("$v0",node.destaddr) # cargo el valor de retorno que esta en v0 en la variable que me piden la guarde.

        if len(args) > 4:
            lines += ["addu $sp, $sp, " + str(many)]
        #lines += "move $a0, $s0"#Cargo el valor de los
        #lines += "move $a1, $s1"
        #lines += "move $a2, $s2"
        #lines += "move $a3, $s3"
        return lines


    @visitor.when(DinamicCallNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Es un jal igual pero antes, tengo que hacer getattr en el virtual table para sacar la funcion cual es y despues hacer jal, revisar si se puede hacer jal a un numero
        #print("LLamada a dinamic_callNode con dest,args,typeaddr,instance,offset = " + str(node.destaddr) + " " + str(node.args) + " " + str(node.typeaddr) + " " + str(node.instance) + " " + str(node.offset) )
        args = node.args
        lines = []  # lista de lineas de codigo

        #lines += "move $s0, $a0"
        #lines += "move $s1, $a1"
        #lines += "move $s2, $a2"
        #lines += "move $s3, $a3"

        for i in range(len(args)):
            if i <= 3:
                lines += local_controler.load_var(("$a" + str(i)), args[i])

        if len(args) > 4:
            for i in range(4, len(args)):
                index = i - 4
                lines += local_controler.load_var(("$t" + str(index)), args[i])

        if len(args) > 4:
            many = (len(args) - 4) * 4  # aqui tengo la cantidad de bytes que voy a mover la pila para pasar el resto de los argumentos
            subu_line = "subu $sp, $sp" + str(many)
            lines += [subu_line]
            for i in range(4, len(args)):
                offset = (i - 4) * 4
                #lines += local_controler.load_var("$t0", args[i])
                index = i-4
                lines += ["sw $t" + str(index) + ", " + str(offset) + "($sp)"]

        offset = self.types.methods[node.typeaddr][node.offset][1] * 4  # en tiempo de compilacion esto es una constante, que debe ser menor que 2**16 por tanto la voy a tomar como offset, la virtual table no debe tener mas de esa cantidad de metodos.
        lines += local_controler.load_var("$t0",node.instance)  # Aqui cargo en t0 la direccion del objeto al cual se le esta haciendo el llamado a la funcion  en memoria
        lines += ["lw $t1, 4($t0)"]  # Aqui cargo en $t1 la direccion de la virtual table, qeu esta en los segundos 4 bytes.
        lines += ["lw $t2," + str(offset) + "($t1)"]  # En esta linea cargo la direccion que esta en la virtual table(t1) con el offset constante ya encontrado y lo guardo en t2.

        lines += ["jalr $t2"] # Salto a la instruccion cuya direccion esta en t2
        lines += local_controler.save_var("$v0" , node.destaddr)
        #lines += [line1,line2,line3,line4,line5]

        if len(args) > 4:
            lines += ["addu $sp, $sp, " + str(many)]
        #lines += "move $a0, $s0"
        #lines += "move $a1, $s1"
        #lines += "move $a2, $s2"
        #lines += "move $a3, $s3"
        return lines

    @visitor.when(ReturnNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #print("Llamada a return con dest = " + str(node.addr)  )
        line1 = local_controler.load_var("$v0",node.addr)
        return line1

    @visitor.when(LoadNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #ver que es esto, cargar algo que esta en la punto data.
        #print("llamada a loadNOde con array,destaddr = " + str(node.array) + " " + str(node.destaddr))
        lines = []
        lines += local_controler.load_var( "$t0", node.array)
        lines += local_controler.save_var("$t0" , node.destaddr)
        return lines

    @visitor.when(StrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #creo que esto  no servia
        return []

    @visitor.when(ReadStrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #es con las instrucciones de systema, tener en cuenta que hay que desambiguar entre la de Int, y la String, que son funciones de sistema distintas,
        lines = []
        #lines += ["move $t5, $a0"]
        #lines += ["move $t6, $a1"]
        lines += local_controler.load_var("$a0", node.destaddr)
        lines += ["li $a1, 1024"]
        lines += ["li $v0, 8"]
        lines += ["syscall"]
        lines += ["move $t6, $a0"] # capturo en t6 el puntero al string
        lines += ["jal function_length_at_String"]
        lines += ["subu $a2, $v0, 1"] # lenggth -1
        lines += ["li $a1, 0"] #index = 0
        lines += ["move $a0, $t6"] # puntero igual al string
        lines += ["jal function_substr_at_String"]
        lines += local_controler.save_var("$v0", node.destaddr) # Ya aqui esta en $v0 el substring y por tanto el result
        #lines += ["move $a0, $t5"]
        #lines += ["move $a1, $t6"]
        return lines

    @visitor.when(PrintStrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #instrucciones de sistema tener en cuenta la desambiguacion de esto
        #print("Estamos llamando a un PrintStr")
        lines = []
        lines += ["move $t5, $a0"]
        lines += local_controler.load_var("$a0" , node.straddr)
        lines += ["li $v0 , 4"]
        lines += ["syscall"]
        lines += ["move $a0, $t5"]
        return lines

    @visitor.when(ReadIntNode)
    def visit(self, node, local_controler: "Local_Fp_Controler"):
        # es con las instrucciones de systema, tener en cuenta que hay que desambiguar entre la de Int, y la String, que son funciones de sistema distintas,
        lines = []
        lines += ["li $v0 , 5"]
        lines += ["syscall"]
        lines += local_controler.save_var("$v0", node.destaddr)
        return lines

    @visitor.when(PrintIntNode)
    def visit(self, node, local_controler: "Local_Fp_Controler"):
        # instrucciones de sistema tener en cuenta la desambiguacion de esto
        lines = []
        lines += ["move $t5, $a0"]
        lines += local_controler.load_var("$a0", node.straddr)
        lines += ["li $v0 , 1"]
        lines += ["syscall"]
        lines += ["move $a0, $t5"]
        return lines

    @visitor.when(LessOrEqualThanNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):

        lines = []
        lines += local_controler.load_var("$t0", node.sraddr1)
        lines += local_controler.load_var("$t1", node.sraddr2)
        lines += ["sle $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(LessThanNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        lines = []
        lines += local_controler.load_var("$t0", node.sraddr1)
        lines += local_controler.load_var("$t1", node.sraddr2)
        lines += ["slt $t2, $t0, $t1"] #TODO ver como manejar el tema de los valores negativos, de momento pongo comparacion con signo aqui, ver si asi esta bien.
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(GreatherThanNode)
    def visit(self,node,local_controler: "Local_Fp_Controler"):
        #En este caso es un less_than_node lo que cambiando las variables
        less_than_node = LessThanNode(node.destaddr,node.sraddr2,node.sraddr1)
        return self.visit(less_than_node, local_controler)

    @visitor.when(EqualNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):

        #print(str(node.sraddr1))
        #print(str(node.sraddr2))
        #print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        lines = []
        lines += local_controler.load_var("$t0", node.sraddr1)
        lines += local_controler.load_var("$t1", node.sraddr2)
        lines += ["seq $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(GreatherOrEqualThanNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        lines = []
        lines += local_controler.load_var("$t0", node.sraddr1)
        lines += local_controler.load_var("$t1", node.sraddr2)
        lines += ["sge $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(AndNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        lines = []
        lines += local_controler.load_var("$t0", node.sraddr1)
        lines += local_controler.load_var("$t1", node.sraddr2)
        lines += ["and $t2, $t0, $t1"]
        lines += local_controler.save_var("$t2", node.destaddr)
        return lines

    @visitor.when(NotNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #todo ver si lo utilizamos nada en bools osea que se quiere que si es 1 devolver 0 y si es 0 devolver 1.
        #este caso solo se utiliza con los bools por lo que el efecto esperado es que si hay un 0 se vuelva un 1 y biceversa.
        lines = []
        lines += local_controler.load_var("$t0", node.sraddr)
        #lines += ["not $t0, $t0"]
        lines += ["li $t1, 0"]
        lines += ["seq $t2, $t1, $t0"]
        #lines +=local_controler.load_var("$t1", self.twopower31)#cargo en t1 el valor que esta en la punto data con nombre guardado en el self, que es igual a 2**31
        #lines += ["subu $t2, $t0, $t1"]#Ver que si lo niego y le resto 1111111111111111111x es como negar x. que es lo que se quiere en este caso
        lines += local_controler.save_var("$t2" , node.destaddr)
        return lines

    @visitor.when(NegationNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #todo revisar que este nodo sea el de poner el valor negativo,osea complemento2 negar y sumar 1
        lines = []
        lines += local_controler.load_var("$t0", node.sraddr)
        lines += ["neg $t1, $t0"]
        lines += ["addi $t1, $t1, 1"]
        lines += local_controler.save_var("$t1" , node.destaddr)
        return lines

    @visitor.when(SuperSetAttrNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Ver como manejo el tema de marcar estas posiciones especificas, probablemente poniendole una propiedad especial a algunos elementos de la lista de string que es la respuesta para despeus recorrerla y poner la direccion correcta
        #Aqui lo que voy a hacer es que voy a devolver 3 tuplas con el nodo y el local_controler, esto me va a servir despues para llamar al metodo
        #self.do_super_set_attr() que se va a encargar de poner las 3 lineas correctas que le corresponden, esto lo hago porque no se el valor al cual voy a
        #a setiar hasta que todas las instrucciones esten ya puestas para saber que linea tienen en mi codigo las funciones
        #print("*********************************************************************************************************")
        #print("Tenemos el SuperSet en type,method,f_name,vtable " + str(node.type) + " " + str(node.fname) + " " + str(node.method_name) + " " + str(node.vtable))
        return [(node,local_controler), (node,local_controler), (node,local_controler)]

    @visitor.when(AbortNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Puede ser con un llamado de sistema o con un jump a un label al final de todo el codigo, menos elegante esta ultima
        #todo ver la diferencia de abort y exception node.

        #en esencia se va a traducir a printear el mensaje especial de abort antes y despues utilizar la llamada a sistema de exit
        lines = []
        print_message_lines = PrintStrNode(self.abort_message_name) # recordar que hay que poner estos nombres en el self
        f_lines = self.visit(print_message_lines, local_controler)#obtengo las lineas de codigos necesarias para hacer el print de este mensaje de abort
        lines  += ["li $v0 , 10"]
        lines += ["syscall"]
        return f_lines + lines

    @visitor.when(ExceptNode)
    def visit(self,node, local_controler: "Local_Fp_Controler"):
        #Debe ser un trap para reventarse, debe ser simple
        # en esencia se va a traducir a printear el mensaje especial de abort antes y despues utilizar la llamada a sistema de exit
        lines = []
        print_message_lines = PrintStrNode(self.except_message_name)  # recordar que hay que poner estos nombres en el self
        f_lines = self.visit(print_message_lines, local_controler) # Aqui obtengo las lineas de codigos necesarias para imprimir el mensaje de excepcion por runtime error.
        lines += ["li $v0 , 10"]
        lines += ["syscall"]
        return f_lines + lines


class Local_Fp_Controler:

    #clase que voy a utilizar para controlar la parte de acceder a las variables locales dentro de un metodo, que es mediante el fp register y un offset determinado, ese offset es el que se encarga de manejar.
    #Las primeras 4 variables registradas van a ser accesibles a traves de los registros a0-a3, las demas van a ser accedidas a travez del fp con un determinado offset que es lo que se determina utilizando el diccionario.
    #Voy a asumir que siempre se modifica el registro fp y el registro ra, por lo que siempre lo voy a pushiar a la pila para despues recuperarlos al final, de esta forma me evito tener que desambiguar
    def __init__(self, params, locals, global_controler):
        #El constructor va a recibir una lista con todos los nombres de las variables que son parametros y las que son Locals (= [locals + internals])

        #tenemos una referencia al global_controler que solo hace falta tener uno ya que este basta para tener las vars de la .Data

        #Voy a guardar en memoria de la forma:
        #...
        #->Param7
        #->Param6
        #->Param5 Aqui va a estar apuntando fp.
        #->Localn
        #->Localn-1
        #.
        #.
        #.
        #->Local1
        #->$ra
        #->fp Aqui va a estar apuntando sp.

        self.param_offset = {} # diccionario que tiene para parametro cual es su offset en el scope local, para poder acceder a ellas de la forma lw t0 (offset)fp.
        self.local_offset = {} # diccionario que tiene para cada local cual es su offset, de esta forma puedo acceder a ellas de la forma (offset)sp

        self.global_controler = global_controler #referencia al global controler que tiene todas la variables globales, osea las que estan en la .Data

        self.first_for_params = {} # diccionario que va a tener los primeros 4 parametros y sus posiciones para saber que cargarlos a ellos a traves de los registros a0-a3

        self.frame = (len(locals) + 2 + 4)*4 # Aqui esta el tamanno del frame de esta funcion en cantidad de bytes, osea ya multiplicado por 4 = a la cantidad de locales + los 2 unicos registros que guardo siempre que son fp y ra.
        i = 0
        for param in params:
            if i <= 3:
                # llenando los primeros 4 parametros el diccionario con su posicion para saber que acceder a ellos es a travez de ai con i = first_for_params[param]
                self.first_for_params[param] = i
                i += 1
            else:
                #Si no es de los primeros 4 parametros lo registro para saber su offset despues
                self.register_param(param)

        for local in locals:
            self.register_local(local)

    def __show__(self):
        print("Vamos a listar los datos del local controler")
        print("primero su global controler es ----")
        self.global_controler.__show__()

        print("***************Vamos a listar ahora los datos de este local controler ******************")
        print("Tiene fram igual a " + str(self.frame))
        print("Vamos a printear la variabls en el first_for, que tiene " + str(self.first_for_params))
        print("Tiene " + str(len(self.param_offset) ) + " variables en sus params offset, vamos a listarlos :")
        for f in self.first_for_params:
            print(str(f) + " : " + " $s" + str(self.first_for_params[f]))

        for x in self.param_offset:
            print(str(x) + " : " + str(self.param_offset[x]))

        print("Tiene " + str(len(self.local_offset) ) + " variables en su local offset, vmaaos a listarlar")
        for l in self.local_offset:
            print(str(l) + " : " + str(self.local_offset[l]))

        print("Terminamos de mostrar las cosas de este local controler")

    def load_var(self,register_name, var_name):
        #Metodo que devuelve el string necesario para cargar la var_name en el register_name, osea un lw t0 (offset)fp
        if isinstance(var_name,int):
            result = "li " + str(register_name) + ", " + str(var_name) + "   # nos pidieron poner la variable de tipo int igual a = " + str(var_name)
            return [result]

        if var_name in self.first_for_params:
            #si es uno de los primeros parametros esta en uno de los registros a0-a3, la busco alli.
            result = "move " + str(register_name) + ", " + "$s" + str(self.first_for_params[var_name]) + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]

        if var_name in self.param_offset:
            #si es una variable param la buscon con el registro fp y su offseet ya guardado
            result = "lw " + str(register_name) + ", " + str(self.param_offset[var_name]) + "($fp)" + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]

        if var_name in self.local_offset:
            #si es una variable local la busco con el registro sp y su offset
            result = "lw " + str(register_name) + ", " + str(self.local_offset[var_name]) + "($sp)" + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]

        if self.global_controler.is_global(var_name):
            #si es una variable global ya el global sabra como buscarla
            return self.global_controler.load_var(register_name,var_name)

        print("En la generacion de mips se pidioo hacer load a una variable que no existe en el scope de la funcion, algo raro revisar.....!!!!!")
        print("***** se pidio la variable con nombre " + str(var_name))
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Me voy a printear a verr que bola")
        self.__show__()
        #no deberia llegar aqui nunca,,

    def save_var(self,register_name,var_name):
        #metodo que me devuelve el string necesario para escribir el contenido de la variable var_name en el registro t0, osea un sw.
        if isinstance(var_name,int):
            result1 = "li $t8, " + str(var_name) + "   # ,esta linea y la siguiente son parte de lo mismo nos pidieron poner la variable con nombre " + str(var_name)
            result2 = "mov " + str(register_name) + ", $t8" + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result1,result2]

        if var_name in self.first_for_params:
            #si es uno de los primeros parametros la muevo del registro ai con i el indice correcto con respecto al parametro que es.
            result = "move " + "$s" + str(self.first_for_params[var_name]) + ", " + str(register_name) + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]

        if var_name in self.param_offset:
            #si la variable es un parametro la busco con el fp y el offset que le tengo guardado
            result = "sw " + str(register_name) + ", " + str(self.param_offset[var_name]) + "($fp)" + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]

        if var_name in self.local_offset:
            #si la variable es local la busco con el $sp y el offset que le tengo guardado
            result = "sw " + str(register_name) + ", " + str(self.local_offset[var_name]) + "($sp)" + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]

        if self.global_controler.is_global(var_name):
            #por ultimo caso si la variable es global devuelvo el string que devuelva esta clase cuando le piden save.
            return self.global_controler.save_var(register_name,var_name)

        print("En la generacion de mips se pidioo hacer load a una variable que no existe en el scope de la funcion, algo raro revisar.....!!!!!")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        #no deberia llegar aqui nunca

    def is_local(self,var_name):
        #metodo que devuelve si la var_name esta en el el diccionario de variables locales, osea si es local o un parametro
        return (var_name in self.param_offset or var_name in self.local_offset or var_name in self.first_for_params)

    def register_param(self,var_name):
        #metodo que registra para cada parametro cual es su offset en el Local para poder acceder a ella como corresponde usando el fp.
        offset = len(self.param_offset)*4
        self.param_offset[var_name] = offset

    def register_local(self,var_name):
        #va a ser similar a l metodo anterior lo que tiene en cuenta que el offset de estas esta despues de todos los params, de los 2 registros que siempre guardo fp y rc.
        offset = (len(self.local_offset))*4 + 8 + 16 # recordar que sumo mas 8 pues los 2 unicos registros que siempre guardo estan primero que todos los locals
        self.local_offset[var_name] = offset

    def give_prefix_of_calling(self):
        #metodo que devuelve la lista de strings necesario como prefijo de llamar a una funcion, la parte de salvar los registros
        line1 = "subu $sp, $sp, " + str(self.frame)
        line2 = "sw $fp, 0($sp)"
        line3 = "sw $ra, 4($sp)"
        line4 = "sw $s0 8($sp)"
        line5 = "sw $s1 12($sp)"
        line6 = "sw $s2 16($sp)"
        line7 = "sw $s3 20($sp)"
        lines = []
        lines += ["move $s0, $a0"]
        lines += ["move $s1, $a1"]
        lines += ["move $s2, $a2"]
        lines += ["move $s3, $a3"]

        line8 = "addu $fp, $sp, " + str(self.frame)
        return [line1,line2,line3,line4,line5,line6,line7,line8] + lines

    def give_suffix_of_calling(self, entry = False):
        #metodo que devuelve la lista de instrucciones necesarias para preservar los valores que utilizamos en la pila y arreglar el sp y demas.
        lines = []
        lines += ["lw $fp, 0($sp)"]
        lines += ["lw $ra, 4($sp)"]
        lines += ["lw $s0 8($sp)"]
        lines += ["lw $s1 12($sp)"]
        lines += ["lw $s2 16($sp)"]
        lines += ["lw $s3 20($sp)"]
        lines += ["addu $sp, $sp, " + str(self.frame)]
        if entry== False:
            lines += ["jr $ra"]
        return lines

class Global_Variables_Controler():

    #TODO Ver que cuando lo que estan ccarando en la punto data es un array lo tengo que cargar con la no con lw.

    #Clase que se va a encargar de devolver las instrucciones de cargar las variables globales a registros pedidos
    def __init__(self):
        self.var_names = {} #diccionario que tiene las variables globales y sus direcciones en memoria. lo utilizo para cargar
        self.str_names = {} # diccionario que tiene todos los str declarados en la .data, me hace falta diferenciar pues con estos tengo que hacer la, sa en vez de lw, sw

    def __show__(self):
        print("Vamos a mostrar los atributos del global_controler")
        print("Tiene " + str(len(self.var_names)) + " variables numericas, vamos a listarlas:")
        for x in self.var_names:
            print(str(x) + " : " + str(self.var_names[x]))

        print("Tiene " + str(len(self.str_names)) + " variables de strings, vamos a listarlos:")
        for s in self.str_names:
            print(str(s) + " : " + str(self.str_names[s]))


    def register_global_var(self,var_name,value):
        #metodo que registra a a la variable var_name como global al ponerla en el diccionario
        self.var_names[var_name] = value

    def register_global_str(self,var_name,value):
        self.str_names[var_name] = value

    def give_dot_data_text(self):
        #metodo que devuelve el contenido de la punto data.
        lines = []
        #Vamos a poner primero los strings
        for str_var in self.str_names:
            lines += [str(str_var) + ":   .asciiz   " + self.str_names[str_var]]

        #Ahora para poner las constantes numericas
        for int_var in self.var_names:
            lines += [str(int_var) + " :  .word   " + str(self.var_names[int_var])]

        return lines

    def is_global(self,var_name):
        #metodo que devuelve si el var_name es global, osea si esta registrado
        return (var_name in self.var_names or var_name in self.str_names)

    def load_var(self,register_name,var_name):
        #metodo que devuelve el string necesario para cargar la variable var_name al register_name de la forma lw t0 var_name

        if var_name in self.str_names:
            # en este caso para que quieres cargar el valro del string, el valor del string es la direccion que tiene var_name no los bytes de var_name que como tal serian los char.
            result = "la " + str(register_name) + ", " + var_name + "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result]
        result = "lw " + str(register_name) + ", " + var_name + "   # nos pidieron poner la variable con nombre " + str(var_name)
        return [result]

    def save_var(self,register_name, var_name):
        #metodo que devuelve el string de la instruccion que guarda el registro en la variable var_name
        if var_name in self.str_names:
            #Si quieren salvar el valor del string tenemos que cargar primero la direccion a $t7 y despues lo ponemos en el registro pedido
            result1 = "la $t8, " + str(var_name) + "   , esta linea y la siguiente son parte del mismo save# nos pidieron poner la variable con nombre " + str(var_name)
            result2 = "move " + str(register_name) + ", $t8"+ "   # nos pidieron poner la variable con nombre " + str(var_name)
            return [result1,result2]
        result = "sw " + str(register_name) + ", " + var_name
        return [result]

