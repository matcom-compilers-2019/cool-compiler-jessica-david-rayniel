from code.front_end import lexer


class Comparer:

    def __init__(self):
        pass

    def token_comparer(self, first_token_list, second_token_list, mapper):
        assert len(first_token_list) == len(second_token_list)

        for token1, token2 in first_token_list, second_token_list:
            if mapper[token1[0]] != token2[0] or token1[1] != token2[1]:
                print(f'token distinto: {token1}, {token2}')


if __name__ == '__main__':
    my_mapper = {
        'ID': 'ID', 'TYPE': 'TYPE_ID', 'INTEGER': 'INT', 'STRING': 'STRING',
        'BOOLEAN': 'BOOL', 'LPAREN': 'O_PAR', 'RPAREN': 'C_PAR',
        'LBRACE': 'O_KEY', 'RBRACE': 'C_KEY', 'COLON': 'TWO_POINTS',
        'COMMA': 'COMMA', 'DOT': 'POINT', 'SEMICOLON': 'POINT_AND_COMMA',
        'AT': 'AT', 'PLUS': 'PLUS', 'MINUS': 'MINUS', 'MULTIPLY': 'STAR',
        'DIVIDE': 'DIV', 'EQ': 'EQUAL', 'LT': 'LESS_THAN',
        'LTEQ': 'LESS_EQUAL_THAN', 'ASSIGN': 'ASSIGNAMENT',
        'INT_COMP': 'DESTRUCTOR', 'NOT': 'NOT', 'ARROW': 'IMPLICATION',
        'case': 'CASE', 'class': 'CLASS', 'else': 'ELSE', 'esac': 'ESAC',
        'fi': 'FI', 'if': 'IF', 'in': 'IN', 'inherits': 'INHERITS',
        'isvoid': 'ISVOID', 'let': 'LET', 'loop': 'LOOP', 'new': 'NEW',
        'of': 'OF', 'pool': 'POOL', 'self': 'SELF', 'then': 'THEN',
        'while': 'WHILE'
    }

    # region test1


    # endregion


    # region test2


    # enregion


    # region test3


    # endregion

