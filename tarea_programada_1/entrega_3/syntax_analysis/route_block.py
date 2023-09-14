# Import ply library
import ply.lex as lex
import ply.yacc as yacc

tokens = (
  'IP',           # General Tokens
  'WEEK_DAY',
  'MONTH',
  'DAY',
  'CLOCK',
  'YEAR',
  'DIR',
  'PEER',
  'IP_RNG',
  'PORT',
  'CARNET',
  'PROF',
  'PLUGIN_MSG',   # Body Tokens
  'VAR_SET',
  'VAR_VAL',
  'SYS_MSG',
  'FLAGS',
  'TCP_MSG',
  'ROUTE_HEADER', # Header Tokens
  'VPN_IP',
  'SBIN_IP_MSG',  # Initialization Tokens
  'TUN_TAP_MSG',
  'SIGTERM_MSG',
  'OPEN_VPN_MSG',
  'LIB_VER_MSG',
  'CRYPTO_MSG',
  'ROUTE_GATEWAY',
  'IP_PROTOCOL',
  'CONN_MSG',
  'IFCONFIG_END',
  'FASE_END',
  'CN_SET',       # Connection Tokens
  'POOL_RET',
  'SENT_CNT',
  'ROUTE_FLAG',
  'TOPOLOGY',
  'CIPHER',
  'SPECIAL_CHAR', # Special Tokens
  'SLASH',
  'COLON'
)

### General Tokens ###
# Define regex for IP tokens
t_IP = """(([0-2]([5][0-5]|[0-4][0-9])|[01]?[0-9]?[0-9])
  [\.]){3}([0-2]([5][0-5]|[0-4][0-9])|([01]?[0-9]?[0-9]))"""

# Define regex for week day tokens
t_WEEK_DAY = 'Sun|Mon|Tue|Wed|Thu|Fri|Sat'

# Define regex for months tokens
t_MONTH = 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dic'

# Define regex for day tokens
t_DAY = '[0-2][0-9]|3[01]'

# Define regex for clock tokens
t_CLOCK = '([01][0-9]|2[0-7]):([0-5][0-9]):([0-5][0-9])'

# Define regex for year tokens
t_YEAR = '(19([4-9][0-9]))|20[0-9][0-9]'

# Define regex for directories
t_DIR = '/([A-Za-z][\w._-]+/?)+'

# Define regex for peer connections stablished
t_PEER = '(peer(-id\s\d)?|via)|(Peer[\]A-Za-z \[_]+)'

# Define regex for IP Range
t_IP_RNG = '\/\d{2}\s'

# Define regex for PORT IP
t_PORT = '(?<=\d)(:\d{5})|(:\d{4})'

# Define regex for CARNET
t_CARNET = '[\w]\d{5}'

# Define regex for PROF
t_PROF = '[A-Za-z]+.[A-Za-z]+'

### Body Tokens###
# Define regex for plugin messages display with their action
def t_PLUGIN_MSG(t):
  r'PLUGIN_([A-Z]+):([A-Z ]+)?'
  return t


# Define tokens for route header
def t_ROUTE_HEADER(t):
  r'<\/?route-identifiers>'
  return t

# Define regex for specified variable set action
def t_VAR_SET(t):
  r'[\w]+='
  return t

# Define regex for specified value assign to variable
def t_VAR_VAL(t):
  r'(?<==)[\w_|:\)\]\[\->\(]+(\s[\(a-z\d\)]+)?(?!(\d{3}\.))(?=(\s|,))'
  return t

# Define regex for system messages display
def t_SYS_MSG(t):
  r'[A-Z]+:[A-Za-z\-_ \/]+(:[ A-Z\'_]+)?(?=(\s|,))(?!(=|\w))'
  return t

# Define regex for flags or text between squared brackets no recognized
def t_FLAGS(t):
  r'\[[A-Za-z_\/\.]+\]'
  return t

# Define regex for TCP messages
def t_TCP_MSG(t):
  r'([A-Za-z ]+)?TCP[\w _\)\(:]+([\]A-Za-z _\[]+)?(:\d{3})?'
  return t

### Header Tokens ###
# Define tokens for VPN IP
def t_VPN_IP(t):
  r'::[a-z\-\d]+::'
  return t

### Initialization Tokens ###

# Define /sbin/ip messages on console
def t_SBIN_IP_MSG(t):
  r'/sbin/ip([a-z ]+\d?[a-z ]+)'
  return t

# Define TUN/TAP messages on console
def t_TUN_TAP_MSG(t):
  r'([A-Za-z ]+)?TUN/TAP[\w ]+'
  return t

# Define SIGTERM messages on console
def t_SIGTERM_MSG(t):
  r'SIGTERM[a-z\], \[]+'
  return t

# Define OPEN_VPN messagges on console
def t_OPEN_VPN_MSG(t):
  r'OpenVPN\s[\d\.?]+[ a-z\d\-_]+(\[.+\] )+[a-z ]+'
  return t

# Define regex for Library Version message on console
def t_LIB_VER_MSG(t):
  r'(library\sversions:[ A-Za-z]+ (\d.?)+[a-z\- ]+)|(,\sLZO\s(\d\.?)+)'
  return t

# Define regex for cryto messages on console
def t_CRYPTO_MSG(t):
  r'(Diffie[\w\- ]+)|([\w \-\.,\/]+ bit\s(RSA))'
  return t

# Define regex for Route Gateway head line
def t_ROUTE_GATEWAY(t):
  r'ROUTE_GATEWAY'
  return t

# Define regex for IP protocol definition
def t_IP_PROTOCOL(t):
  r'[\w -//]+protocol\.[\w _]+'
  return t

### Special Tokens ###
# Define regex for undetermined characters
def t_SPECIAL_CHAR(t):
  r'[\[\]\',\->\)\(]'
  return t

# Define regex for slash
t_SLASH = r'\/'

# Define regex for colon
t_COLON = r':(?=(\s|\'))'

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = '\t  '

# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# ########################################################################################################################################
# ########################################################################################################################################

# Parsing rules

def p_route_identifiers(p):
    'route_identifiers : ROUTE_HEADER key_value_list ROUTE_HEADER'
    p[0] = p[2]

def p_key_value_list(p):
    'key_value_list : key_value_list key_value'
    p[0] = p[1] + [p[2]]

def p_key_value_list_single(p):
    'key_value_list : key_value'
    p[0] = [p[1]]

def p_key_value(p):
    'key_value : VPN_IP IP'
    p[0] = (p[1], p[2])

def p_error(p):
    print("Syntax error at:", p)

if __name__ == "__main__":
  # Build the lexer
  file = open("vpn-logs-2020-modified-abb-revMM.txt")
  data = file.read()
  lexer = lex.lex()
  parser = yacc.yacc()
  parser.parse(data)
  
  # Open file for analize
  # NOTE: Consider the path that you execute. Depending the terminal from
  #       what you are executing you should change this path
  # TODO: For the moment the file direction is hardcoded, but in future versions
  #       it should be a parameter reveiced via the UI

  # print(data)

  # # Give the lexer some input
  # lexer.input(data)
  
  # tokens_output = open("tokens_output.txt", "w")
  # # Tokenize
  # while True:
  #   tok = lexer.token()
  #   if not tok: 
  #     break      # No more input
  #   # tokens_output.write(str(tok.value))
  #   tokens_output.write(f"{tok}\n")
  #   # tokens_output.write(f"{tok.type}: {tok.value}\n")
  # tokens_output.close()