import ply.yacc as yacc
from lexer import tokens, lexer

class PythonParser:
    # Declare tokens (required by PLY)
    tokens = tokens
    
    # Define precedence rules (recommended for arithmetic)
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    def __init__(self):
        self.parser = yacc.yacc(module=self)

    def parse(self, code, lexer=None):
        return self.parser.parse(code, lexer=lexer)

    # Start symbol
    def p_program(self, p):
        '''program : statement_list'''
        p[0] = ('program', p[1])

    # Statement list: one or more statements
    def p_statement_list(self, p):
        '''statement_list : statement_list statement
                         | statement'''
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    # Statements can be simple or compound
    def p_statement(self, p):
        '''statement : simple_statement
                     | compound_statement'''
        p[0] = p[1]

    # Simple statements: assignment or expression (like print call)
    def p_simple_statement(self, p):
        '''simple_statement : assignment_statement
                            | expression_statement'''
        p[0] = p[1]

    # Assignment: IDENTIFIER = expression
    def p_assignment_statement(self, p):
        '''assignment_statement : IDENTIFIER ASSIGN expression'''
        p[0] = ('assign', p[1], p[3])

    # Expression statement (e.g. print function call)
    def p_expression_statement(self, p):
        '''expression_statement : expression'''
        p[0] = ('expr', p[1])

    # Combined expression rule (merged the two original ones)
    def p_expression(self, p):
        '''expression : expression PLUS term
                     | expression MINUS term
                     | PRINT LPAREN expression RPAREN
                     | term'''
        if len(p) == 2:
            p[0] = p[1]
        elif p[1] == 'print':
            p[0] = ('print', p[3])
        else:
            p[0] = (p[2], p[1], p[3])

    # Terms support multiplication and division
    def p_term(self, p):
        '''term : term TIMES factor
                | term DIVIDE factor
                | factor'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = (p[2], p[1], p[3])

    # Factors: number, string, identifier, or parenthesized expression
    def p_factor(self, p):
        '''factor : NUMBER
                  | STRING
                  | IDENTIFIER
                  | LPAREN expression RPAREN'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    # Compound statements: if or function definition
    def p_compound_statement(self, p):
        '''compound_statement : if_statement
                             | function_definition'''
        p[0] = p[1]

    # If statement: if expression : statement_list
    def p_if_statement(self, p):
        '''if_statement : IF expression COLON statement_list'''
        p[0] = ('if', p[2], p[4])

    # Function definition: def IDENTIFIER() : statement_list
    def p_function_definition(self, p):
        '''function_definition : DEF IDENTIFIER LPAREN RPAREN COLON statement_list'''
        p[0] = ('function_def', p[2], p[6])

    # Error handling rule
    def p_error(self, p):
        if p:
            print(f"Syntax error at token {p.type}, value {p.value}")
        else:
            print("Syntax error at EOF")


# ... all your class code ...

# Create a global parser instance to be imported elsewhere
parser = PythonParser()

if __name__ == '__main__':
    code = '''
def greet():
    name = "Alice"
    print("Hello " + name)
    if name:
        print("Welcome!")
'''
    ast = parser.parse(code)
    print(ast)
