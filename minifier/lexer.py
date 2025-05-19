import ply.lex as lex

# List of token names
tokens = [
    'NUMBER', 'STRING', 'IDENTIFIER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'LPAREN', 'RPAREN', 'COLON',
    'IF', 'DEF', 'PRINT'
]

# Regular expression rules for simple tokens
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_ASSIGN   = r'='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_COLON    = r':'

# Reserved words
reserved = {
    'if': 'IF',
    'def': 'DEF',
    'print': 'PRINT'
}

# Identifier and reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Ignore triple-quoted docstrings (both """...""" and '''...''')
def t_DOCSTRING(t):
    r'("""(.|\n)*?"""|\'\'\'(.|\n)*?\'\'\')'
    pass  # Do not return a token, effectively removing docstrings

# String literal (double quotes only)
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Number literal (integers only)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character {t.value[0]!r} at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
