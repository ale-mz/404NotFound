# Import ply library
import ply.lex as lex

# Define tokens to identify
tokens = (
  'CARNET',
  'PROF',
  'IP'
)

def t_CARNET(t):
  r'[a-z,A-Z]\d{5}'
  return t

def t_PROF(t):
  r'anom.[a-z]+'
  return t

def t_IP(t):
  r"""(([0-2]([5][0-5]|[0-4][0-9])|[01]?[0-9]?[0-9])
      [\.]){3}([0-2]([5][0-5]|[0-4][0-9])|([01]?[0-9]?[0-9]))"""
  return t

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Open file for analize
# NOTE: Consider the path that you execute. Depending the terminal from
#       what you are executing you should change this path
file = open("vpn-logs-2020-modified-abb-revMM.txt")

data = file.read()
# print(data)

# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
  tok = lexer.token()
  if not tok: 
    break      # No more input
  print(tok)
