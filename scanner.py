import ply.lex as lex

# List of token names. This is always required
tokens = [
    'NUMBER',
    'SUM',
    'SUB',
    'MUL',
    'DIV',
    'MOD',
    'EQUAL',
    'LPAREN',
    'RPAREN',
    'PRINT',
    'INPUT',
    'WHILE',
    'FOR',
    'IF',
    'ELSE',
    'STRINGVARIBABLE',
    'INTEGERVARIBABLE',
    'STRING',
    'LESSEQUAL',
    'GREATEQUAL',
    'LESS',
    'GREATER',
    'RIGHT_CURLY',
    'LEFT_CURLY',
    'COLON',
]

# Regular expression rules for simple tokens
t_SUM = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_PRINT = r'print'
t_INPUT = r'input'
t_WHILE = r'while'
t_FOR = r'for'
t_IF = r'if'
t_ELSE = r'else'
t_LESSEQUAL = r'\<='
t_GREATEQUAL = r'\>='
t_LESS = r'\<'
t_GREATER = r'\>'
t_RIGHT_CURLY = r'\}'
t_LEFT_CURLY = r'\{'
t_COLON = r'\:'

# A regular expression rule with some action code


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_INTEGERVARIBABLE(t):
    r'n_.[a-zA-z][a-zA-z]+'
    return t

def t_STRINGVARIBABLE(t):
    r's_.[a-zA-z][a-zA-z]+'
    return t



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def main(code):

    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input
    lexer.input(code)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)




if __name__ == '__main__':
    with open('code.nib', 'r') as inp:
        main(inp.read())
