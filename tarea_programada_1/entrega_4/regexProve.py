# Import ply library
import ply.lex as lex
import ply.yacc as yacc

# Table with conections
listcon = []

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
t_PROF = '[A-Za-z]+\.[A-Za-z]+'

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
  r'\[(([\w]+_[\w]+)|([\w]+\/[\w]+.[\w]+))\]'
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
  r'/sbin/ip([a-z ]+\d?[a-z ]+)([\d]+(?=\s))?'
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
  r'[A-Za-z][\w -//]+protocol\.[\w _]+'
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

###############################################################################
###############################################################################

## Eliminate after
caught_tokens = []

def p_file(t):
  'file : header init listcon'
  print("All file consumed\n")
  for i in range(len(listcon)):
    print(listcon[i])
  pass

def p_header(t):
  'header : ROUTE_HEADER vpnip ROUTE_HEADER'
  print("Header complete\n")
  pass

def p_vpnip(t):
  '''vpnip : VPN_IP IP vpnip
           | empty'''
  pass
  
def p_init(t):
  'init : initbody FASE_END'
  print("Initialization Complete\n")
  pass

def p_initbody(t):
  '''initbody : date software initbody
              | date network initbody
              | date hardware initbody
              | empty'''
  pass

def p_software(t):
  '''software : plugin
              | SYS_MSG SPECIAL_CHAR VAR_SET VAR_VAL VAR_SET VAR_VAL'''
  pass

def p_network(t):
  '''network : sbinit
             | tuntap
             | CRYPTO_MSG
             | ROUTE_GATEWAY IP SLASH IP VAR_SET VAR_VAL VAR_SET VAR_VAL
             | IP_PROTOCOL
             | CONN_MSG VAR_SET VAR_VAL VAR_SET VAR_VAL
             | CONN_MSG VAR_SET IP VAR_SET VAR_VAL SPECIAL_CHAR VAR_SET VAR_VAL
             | IFCONFIG_END
             | CONN_MSG
             | TCP_MSG
             | SYS_MSG VAR_SET VAR_VAL VAR_SET VAR_VAL'''
  pass

def p_hardware(t):
  '''hardware : SYS_MSG
              | SIGTERM_MSG
              | OPEN_VPN_MSG MONTH DAY YEAR
              | LIB_VER_MSG DAY MONTH YEAR LIB_VER_MSG
              | SYS_MSG VAR_SET VAR_VAL
              | VAR_SET VAR_VAL'''
  pass

def p_sbinit(t):
  ''' sbinit : SBIN_IP_MSG IP IP_RNG
             | SBIN_IP_MSG IP IP_RNG PEER IP
             | SBIN_IP_MSG IP PEER IP
             | SBIN_IP_MSG
             | empty'''
  pass

def p_plugin(t):
  ''' plugin : PLUGIN_MSG DIR VAR_SET VAR_VAL
              | PLUGIN_MSG DIR SPECIAL_CHAR SPECIAL_CHAR DIR SPECIAL_CHAR FLAGS SPECIAL_CHAR VAR_SET VAR_VAL
              | PLUGIN_MSG DIR
              | PLUGIN_MSG
              | IP PORT PLUGIN_MSG DIR VAR_SET VAR_VAL'''
  pass
   
def p_tuntap(t):
 'tuntap : TUN_TAP_MSG'
 pass

def p_listconnections(t):
  '''listcon : listcon conection
             | conection'''
  ("All connections detected\n")
  
def p_conection(t):
  'conection : start coninit login peering conline end'
  connection = [t[3][0], t[3][1], t[5]]
  listcon.append(connection)


def p_start(t):
  'start : date TCP_MSG IP PORT'

def p_coninit(t):
  '''coninit : coninit conmsg
           | conmsg'''
  
def p_conmsg(t):
  '''conmsg : date IP PORT SYS_MSG FLAGS IP PORT SPECIAL_CHAR VAR_SET VAR_VAL
              | date plugin
              | date IP PORT SYS_MSG SPECIAL_CHAR user SPECIAL_CHAR CN_SET
              | date IP PORT CONN_MSG CRYPTO_MSG'''
  
def p_login(t):
  'login : date IP PORT SPECIAL_CHAR user SPECIAL_CHAR PEER IP PORT'
  t[0] = (t[2],t[5])

  
def p_peering(t):
  '''peering : peering peermsg
             | peermsg'''
  
def p_peermsg(t):
  '''peermsg : peercon CONN_MSG POOL_RET VAR_SET IP SPECIAL_CHAR VAR_SET VAR_VAL
             | peercon plugin
             | peercon CONN_MSG CONN_MSG DIR
             | peercon CONN_MSG CONN_MSG IP SPECIAL_CHAR SPECIAL_CHAR user SLASH IP PORT
             | peercon SYS_MSG user SLASH IP PORT COLON IP
             | peercon SYS_MSG'''
  
def p_conline(t):
  '''conline : routehead routing routend'''
  t[0] = t[2]

def p_routhead(t):
  'routehead : peercon SENT_CNT SPECIAL_CHAR user SPECIAL_CHAR COLON SPECIAL_CHAR'

def p_routend(t):
  'routend : TOPOLOGY IP IP SPECIAL_CHAR PEER SPECIAL_CHAR CIPHER SPECIAL_CHAR VAR_SET VAR_VAL'
  
def p_routing(t):
  '''routing : routing route
             | route'''
  if len(t) == 3:
    t[0] = t[1] + t[2]
  else :
    t[0] = t[1]

def p_route(t):
  '''route : ROUTE_FLAG VPN_IP IP
           | ROUTE_FLAG VPN_IP'''
  if len(t) == 4:
    t[0] = t[1] + t[2] + t[3]
  else :
    t[0] = t[1] + t[2]
  
def p_end(t):
  '''end : endmsg endmsg endmsg'''
  
def p_endmsg(t):
  '''endmsg : peercon CONN_MSG CIPHER'''
  
def p_peercon(t):
  'peercon : date user SLASH IP PORT'

def p_date(t):
  '''date : WEEK_DAY MONTH DAY CLOCK YEAR'''
  pass

def p_user(t):
  '''user : CARNET
          | PROF'''
  t[0] = t[1]
  pass

  
def p_empty(t):
  'empty :'
  pass

#dictionary of names
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