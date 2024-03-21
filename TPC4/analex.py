import ply.lex as lex
import re

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'OPERATOR',
    'NUMBER',
    'COMMA',
    'ATTRIBUTE'
)

t_SELECT = r'(?i)select'
t_FROM = r'(?i)from'
t_WHERE = r'(?i)where'
t_OPERATOR = r'[<|>|=]+'
t_COMMA  = r','
t_ATTRIBUTE  = r'\w+'

def t_NUMBER(t):
    r'(\+|-)?\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Ilegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
lexer = lex.lex()

data = 'SELECT id, nome, salario FROM empregados WHERE salario>=820'

lexer.input(data)

while tok := lexer.token():
    print(tok)
