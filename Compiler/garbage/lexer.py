import ply
import re
'''
the lexer module
'''
# todo Ray: fajarme con las prioridades de los literales y otros
# todo verificar que los tokens puedan tener _ en sus tokentype

reserved = {'class': 'CLASS', 'else': 'ELSE', 'fi': 'FI', 'if': 'IF',
            'in': 'IN', 'inherits': 'INHERITS', 'isvoid': 'ISVOID',
            'let': 'LET', 'loop': 'LOOP', 'pool': 'POOL', 'then': 'THEN',
            'while': 'WHILE', 'case': 'CASE', 'esac': 'ESAC', 'new': 'NEW',
            'of': 'OF', 'not': 'NOT'}

# bools = {'true': 'TRUE', 'false': 'FALSE'}

# specialID = {'SELF_TYPE': 'SELF_TYPE', 'self': 'SELF'}

# special symbol?
# DESTRUCTOR : ~
# ASSIGNAMENT : <-
# IMPLICATION : =>
# SPECIAL_CHAR : \t \v \r \n etc
tokens = ['INT', 'ID', 'TYPE_ID', 'SELF', 'SELF_TYPE', 'STRING', 'BOOL',
          'COMMENTS', 'DIV', 'STAR', 'MINUS', 'PLUS', 'SPECIAL_CHAR', 'POINT',
          'AT', 'DESTRUCTOR', 'LESS_EQUAL_THAN', 'LESS_THAN', 'EQUAL',
          'ASSIGNAMENT', 'TWO_POINTS', 'O_KEY', 'C_KEY', 'O_PAR', 'C_PAR',
          'POINT_AND_COMMA', 'COMMA', 'IMPLICATION', 'TRUE', 'FALSE'] + \
         list(reserved.values())

# todo verificar los espacios que pueden haber en el medio de estos operadores
# todo verificar que los literals no sean caracteres especiales
t_IMPLICATION = r'=>'
t_ASSIGNAMENT = r'<-'
t_LESS_EQUAL_THAN = r'<='
# literals?
t_COMMA = r','
t_POINT_AND_COMMA = r';'
t_C_KEY = r'\}'
t_O_KEY = r'\{'
t_TWO_POINTS = r':'
t_LESS_THAN = r'<'
t_EQUAL = r'='
t_DESTRUCTOR = r'~'
t_AT = r'@'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_DIV = r'/'
t_O_PAR  = r'\('
t_C_PAR  = r'\)'
t_POINT = r'\.'

# todo cambiar el nombre del id por objectid queda mas consistente con los
#  nombres, mas bonito
# el eof se pasa como el none
def t_ID(token):
    r'[a-z][A-Za-z0-9_]*'
    for key in reserved.keys():
        if re.fullmatch(token.value, key, re.I) is not None:
            token.type = reserved[key]
            return token
    # todo duda en cuanto usar re.I en el self
    if re.fullmatch(token.value, 'self', re.I) is not None:
        token.type = 'SELF'
        return token
    # todo verificar qie el re no halla que compilar el string, aunq me parece
    #  que si hay q hacerlo buscar
    elif re.fullmatch(token.value, 'true', re.I) is not None:
        token.type = 'TRUE'
        return token

    elif re.fullmatch(token.value, 'false', re.I) is not None:
        token.type = 'FALSE'
        return token

    return token

def t_TYPE_ID(token):
    r'[A-Z][A-Za-z0-9_]*'
    for key in reserved.keys():
        if re.fullmatch(token.value, key, re.I) is not None:
            token.type = reserved[key]
            return token
    # todo duda nuevamente en el uso del re.I en self_type
    if re.fullmatch(token.value, 'SELF_TYPE', re.I) is not None:
        token.type = 'SELF_TYPE'
        return token

    return token

# A este Codigo hay que arreglarle los tabuladores, recordar que estan puestos
# como 4 espacios y ##no /t

def t_INT(token):
    r'[1-9][0-9]*'
    token.value = int(token.value)
    return token

def t_COMMENTS(t):
    r'(\*(.|\n)*? \*)|(--.*)'
    pass
# una idea para trabajar los string, los comentarios y otros mas complicados es
# con los estados como esta ejemplificado en el pycoolc
def t_STRING(t):
    r'\"([^\n]|(\\\n)|(\\.))*?\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# todo review that, q pasa con los tabuladores, retornos de carro, etc
def t_SPECIAL_CHAR(t):
    r'\s' 

# todo es necesario un eof

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# todo ver si es buena idea agregar tokens para ignorar, o ver como es eso,
#  echarle un vistazo