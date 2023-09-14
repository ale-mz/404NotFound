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

# Define regex for Connection messages on console
def t_CONN_MSG(t):
  r'[A-Za-z _]+:'
  return t

# Define regex for connection pool assign
def t_POOL_RET(t):
  r'pool\sreturned'
  return t

# Define regex for route line head
def t_SENT_CNT(t):
  r'SENT\sCONTROL'
  return t

# Define regex for route flag
def t_ROUTE_FLAG(t):
  r'(PUSH_REPLY)?(,route)'
  return t

# Define regex for status of connection
def t_TOPOLOGY(t):
  r',topology[\w ,\-]+(?=\s)'
  return t

# Define regex for cypher flag on peer
def t_CIPHER(t):
  r'([A-Za-z ]+)?(cipher|Cipher)[\' \w\-]+'
  return t

# Define regex for message at the end of console
def t_IFCONFIG_END(t):
  r'[A-Z ]+LIST'
  return t

# Define regex for message at the end of a phase
def t_FASE_END(t):
  r'[A-Za-z ]+Completed'
  return t

### Connection Tokens ###
# Define regex for last part of username authentication
def t_CN_SET(t):
  r'\[CN\sSET\]'
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


# Parsing rules
precedence = (
    # WIP
    )

def p_file(t):
  'file : header init_head connection'
  pass

def p_header(t):
  'header : ROUTE_HEADER vpnip ROUTE_HEADER'


def p_vpnip(t):
  '''vpnip : VPN_IP IP vpnip
           | empty'''


def p_date(t):
  '''date : WEEK_DAY MONTH DAY CLOCK YEAR
          | YEAR '''

def p_init_head(t):
  'init_head : init_body init_end'
  pass

def p_init_body(t):
 '''init_body : software init_body
    | hardware init_body
    | network init_body
    | empty'''
 pass

def p_software(t):
  '''software : plugin
    | sbinit
    | tuntap'''
  pass

def p_plugin(t):
  ''' plugin : date PLUGIN_MSG DIR VAR_SET VAR_VAL
    | PLUGIN_MSG VAR_SET VAR_VAL
    | date PLUGIN_MSG
    | date PLUGIN_MSG DIR
    | date PLUGIN_MSG DIR SPECIAL_CHAR SPECIAL_CHAR DIR SPECIAL_CHAR FLAGS SPECIAL_CHAR VAR_SET VAR_VAL'''
  pass

def p_sbinit(t):
  '''sbinit : date SBIN_IP_MSG IP IP_RNG
    | date SBIN_IP_MSG IP IP_RNG PEER IP
    | date SBIN_IP_MSG IP PEER IP'''
  pass

def p_tuntap(t):
  'tuntap : date TUN_TAP_MSG'

def p_hardware(t):
  '''hardware : date SYS_MSG
    | date SIGTERM_MSG
    | date OPEN_VPN_MSG MONTH DAY YEAR
    | date LIB_VER_MSG DAY MONTH YEAR LIB_VER_MSG
    | date SYS_MSG VAR_SET VAR_VAL
    | date VAR_SET VAR_VAL'''
  pass
   
def p_network(t):
  '''network : date crypto
    | date ROUTE_GATEWAY IP SLASH IP VAR_SET VAR_VAL VAR_SET VAR_VAL
    | date IP_PROTOCOL
    | date CONN_MSG VAR_SET VAR_VAL VAR_SET VAR_VAL
    | date CONN_MSG VAR_SET IP VAR_SET VAR_VAL SPECIAL_CHAR VAR_SET VAR_VAL
    | date IFCONFIG_END'''
  pass

def p_connection(t):
  'connection : crypto conmutation routing crypto'
  pass

def p_start(t):
  'start : date TCP_MSG IP PORT'
  pass

def p_login(t):
  '''login : date IP PORT SYS_MSG IP PORT SPECIAL_CHAR VAR_SET VAR_VAL
    | date IP PORT plugin SYS_MSG DIR VAR_SET VAR_VAL
    | date IP PORT SYS_MSG SPECIAL_CHAR user SPECIAL_CHAR CN_SET'''
  pass

def p_crypto(t):
  '''crypto : date IP PORT CONN_MSG CRYPTO_MSG
    | date user SLASH IP PORT CONN_MSG CIPHER
    | CRYPTO_MSG
    | crypto login
    | start'''
  pass

def p_conmutation(t):
  '''conmutation : date IP PORT SPECIAL_CHAR user SPECIAL_CHAR PORT PEER IP PORT
    | date user SLASH IP PORT CONN_MSG POOL_RET ipversion
    | date user SLASH IP PORT PLUGIN_MSG DIR VAR_SET VAR_VAL
    | date user SLASH IP PORT CONN_MSG CONN_MSG DIR
    | date user user SLASH IP PORT CONN_MSG CONN_MSG IP SPECIAL_CHAR SPECIAL_CHAR user SLASH IP PORT
    | date user SLASH IP PORT SYS_MSG user SLASH IP PORT COLON IP'''
  pass

def p_route(t):
  '''route : ROUTE_FLAG VPN_IP route
    | IP ROUTE_FLAG VPN_IP route
    | empty'''
  pass

def p_routing(t):
  '''routing : date user SLASH IP PORT SYS_MSG
  | date user SLASH IP PORT SENT_CNT SPECIAL_CHAR user SPECIAL_CHAR COLON route TOPOLOGY IP IP SPECIAL_CHAR CIPHER SPECIAL_CHAR VAR_SET VAR_VAL'''
  pass

def p_connectionID(t):
  '''connection : date CARNET SLASH IP PORT
    | date PROF SLASH IP PORT'''
  t[0] = t[4]

def p_user(t):
  '''user : CARNET
    | PROF'''
  pass

def p_init_end(t):
  'init_end : date FASE_END'
  pass

def p_empty(t):
  'empty : '
  pass

def p_ipversion(t):
  'ipversion : VAR_SET IP VAR_SET VAR_VAL'
  t[0] = t[2]
  

 
# dictionary of names
names = { }

# parse
def p_error(t):
    print(f"Syntax error at '{t.value}'")
    print(t)


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

  # Give the lexer some input
  lexer.input(data)
  
  tokens_output = open("tokens_output.txt", "w")
  # Tokenize
  while True:
    tok = lexer.token()
    if not tok: 
      break      # No more input
    # tokens_output.write(str(tok.value))
    tokens_output.write(f"{tok}\n")
    # tokens_output.write(f"{tok.type}: {tok.value}\n")
  tokens_output.close()