# Import ply library
import ply.lex as lex

# Define tokens to identify
tokens = (
  'CARNET',
  'PROF',
  'IP',
  'CLOCK',
  'PLUGIN_MSG',
  'AF_FLAG',
  'ACT_FLAG',
  'CH_MSG',
  'CIPH_MSG',
  'NET_NAME',
  'BIT_MSG',
  'PUSH_MSG',
  'FOLDER_DIR',
  'IPV4_TKN',
  'IPV6_TKN',
  'MONTH_DATE',
  'WEEK_DAY',
  'PORT',
  'YEAR',
  'MONTH',
  'REG_NUM',
  'BASIC_DIV'
)

def t_FOLDER_DIR(t):
  r'/([\w\d._-]+/)+'
  return t

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

def t_CLOCK(t):
  r'([01]\d|2[0-3])(:[0-5]\d){2}'
  return t

# Define regex for plugins messages
def t_PLUGIN_MSG(t):
  r'PLUGIN_[A-Z]+:\s[A-Z]*'
  return t

# Define regex for AF_X messages
def t_AF_FLAG(t):
  r'\[AF_[A-Z]+\]'
  return t

# Define regex for actions flags
def t_ACT_FLAG(t):
  r'([A-Za-z]+)(_[a-z]+)?:(([A-za-z\s]+):)?'
  return t

# Define regex for channel messages
def t_CH_MSG(t):
  r'([A-z]([a-z])+(\s))+(Channel:)'
  return t

# Define regex for cipher messages
def t_CIPH_MSG(t):
  r'(C|c)ipher[\w\s\'-]*(key|RSA)'
  return t

# Define regex for all net names
def t_NET_NAME(t):
  r'::[\w\d-]+::'
  return t

# Define regex for bit messages
def t_BIT_MSG(t):
  r'(B|b)it(\sRSA|\skey)'
  return t

# Define regex for Push messages
def t_PUSH_MSG(t):
  r'(PUSH:[\w\s\'-]+|PUSH_REPLY,)'
  return t

# Define regex token for IPv4 Simbol
def t_IPV4_TKN(t):
  r'(I|i)(P|p)v4(=)?'
  return t

# Define regex token for IPv6 Simbol
def t_IPV6_TKN(t):
  r'(I|i)(P|p)v6(=)?'
  return t

# Define regex for log Months
def t_MONTH_DATE(t):
  r'Jan|Feb|Ma(r|y)|A(pr|ug)|Ju(n|l)|Sep|Oct|Nov|Dec'
  return t

# Define regex for log week day
def t_WEEK_DAY(t):
  r'Mon|Tue|Wed|Thu|Fri|S(at|un)'
  return t

# Define regex for Port
def t_PORT(t):
  r':(\d){5}'
  return t

# define regex for Years
def t_YEAR(t):
  r'(\d){4}'
  return t

# Define regex for Months
def t_MONTH(t):
  r'(\d){2}'
  return t

# Define regex for Day dates (2 digit number)
def t_REG_NUM(t):
  r'(\d)+'
  return t

def t_BASIC_DIV(t):
  r'\/'
  return t

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
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
