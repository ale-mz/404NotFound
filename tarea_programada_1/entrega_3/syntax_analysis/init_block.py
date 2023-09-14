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
  # 'PROF',
  'STATUS',
  'POST',
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

t_STATUS = 'status'

t_POST = 'POST'

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

# # Define regex for PROF
# t_PROF = '[A-Za-z]+.[A-Za-z]+'
# Define /sbin/ip messages on console
def t_SBIN_IP_MSG(t):
  r'/sbin/ip([a-z ]+\d?[a-z ]+)'
  # r'(/sbin/ip route del|/sbin/ip addr del dev tun0 local|/sbin/ip link set dev tun0 up mtu 1500|/sbin/ip addr add dev tun0 local|/sbin/ip route add)'
  # r'/sbin/ip (route del|addr del dev tun0 local|link set dev tun0 up mtu 1500|addr add dev tun0 local|route add)'
  return t

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


# ########################################################################################################################################
# ########################################################################################################################################
# ########################################################################################################################################

def p_main_rule(p):
    '''
    main_rule : log_line main_rule
              | log_line
              | empty
    '''
    pass
# parsing rules
# Parsing rules

def p_log_line(p):
    '''
    log_line : date PLUGIN_MSG DIR VAR_SET VAR_VAL
              | date SBIN_IP_MSG IP IP_RNG
              | date TUN_TAP_MSG
              | date SBIN_IP_MSG IP PEER IP
              | date SIGTERM_MSG 
              | date OPEN_VPN_MSG MONTH DAY YEAR
              | date LIB_VER_MSG DAY MONTH YEAR LIB_VER_MSG
              | date SYS_MSG
              | date PLUGIN_MSG DIR SPECIAL_CHAR SPECIAL_CHAR DIR SPECIAL_CHAR FLAGS SPECIAL_CHAR VAR_SET VAR_VAL
              | date CRYPTO_MSG
              | date ROUTE_GATEWAY IP SLASH IP VAR_SET VAR_VAL VAR_SET VAR_VAL
              | date SBIN_IP_MSG DAY DAY
              | date SBIN_IP_MSG IP IP_RNG PEER IP
              | date IP_PROTOCOL
              | date CONN_MSG VAR_SET VAR_VAL VAR_SET VAR_VAL
              | date TCP_MSG 
              | date SYS_MSG SPECIAL_CHAR VAR_SET VAR_VAL VAR_SET VAR_VAL
              | date CONN_MSG VAR_SET IP VAR_SET VAR_VAL SPECIAL_CHAR VAR_SET VAR_VAL
              | date IFCONFIG_END
              | date SYS_MS VAR_SET VAR_VAL VAR_SET VAR_VAL
    '''
    pass

def p_date(p):
    '''
    date : WEEK_DAY MONTH DAY CLOCK YEAR
          | WEEK_DAY MONTH DAY CLOCK
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error at:", p)

if __name__ == "__main__":
  # Build the lexer
  # file = open("vpn-logs-2020-modified-abb-revMM.txt")
  #  data = file.read()
  lexer = lex.lex()
  parser = yacc.yacc()

  log_data = '''
    Sun Sep 13 17:02:16 2020 PLUGIN_CALL: POST /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so/PLUGIN_CLIENT_DISCONNECT status=0
    Sun Sep 13 17:02:16 2020 PLUGIN_CALL: POST /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so/PLUGIN_CLIENT_DISCONNECT status=0
    Sun Sep 13 17:02:16 2020 PLUGIN_CALL: POST /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so/PLUGIN_CLIENT_DISCONNECT status=0
    Sun Sep 13 17:02:16 2020 PLUGIN_CALL: POST /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so/PLUGIN_CLIENT_DISCONNECT status=0
    Sun Sep 13 17:02:16 2020 PLUGIN_CALL: POST /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so/PLUGIN_CLIENT_DISCONNECT status=0
    Sun Sep 13 17:02:16 2020 /sbin/ip route del 192.168.68.0/24
    Sun Sep 13 17:02:16 2020 Closing TUN/TAP interface
    Sun Sep 13 17:02:16 2020 /sbin/ip addr del dev tun0 local 192.168.68.1 peer 192.168.68.2
    Sun Sep 13 17:02:16 2020 PLUGIN_CLOSE: /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so
    Sun Sep 13 17:02:16 2020 SIGTERM[hard,] received, process exiting
    Sun Sep 13 17:02:16 2020 OpenVPN 2.4.9 x86_64-redhat-linux-gnu [Fedora EPEL patched] [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Apr 24 2020
    Sun Sep 13 17:02:16 2020 library versions: OpenSSL 1.0.2k-fips  26 Jan 2017, LZO 2.06
    Sun Sep 13 17:02:16 2020 WARNING: --ifconfig-pool-persist will not work with --duplicate-cn
    Sun Sep 13 17:02:16 2020 PLUGIN_INIT: POST /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so '[/usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so] [auth/ldap.so]' intercepted=PLUGIN_AUTH_USER_PASS_VERIFY|PLUGIN_CLIENT_CONNECT|PLUGIN_CLIENT_DISCONNECT 
    Sun Sep 13 17:02:16 2020 Diffie-Hellman initialized with 2048 bit key
    Mon Sep 14 17:02:16 2020 ROUTE_GATEWAY 163.178.104.65/255.255.255.192 IFACE=eth1 HWADDR=00:0c:29:60:37:e5
    Sun Sep 13 17:02:16 2020 TUN/TAP device tun0 opened
    Sun Sep 13 17:02:16 2020 TUN/TAP TX queue length set to 100
    Sun Sep 13 17:02:16 2020 /sbin/ip link set dev tun0 up mtu 1500
    Sun Sep 13 17:02:16 2020 /sbin/ip addr add dev tun0 local 192.168.68.1 peer 192.168.68.2
    Sun Sep 13 17:02:16 2020 /sbin/ip route add 192.168.68.0/24 via 192.168.68.2
    Sun Sep 13 17:02:16 2020 Could not determine IPv4/IPv6 protocol. Using AF_INET
    Sun Sep 13 17:02:16 2020 Socket Buffers: R=[87380->87380] S=[16384->16384]
    Sun Sep 13 17:02:16 2020 Listening for incoming TCP connection on [AF_INET][undef]:443
    Sun Sep 13 17:02:16 2020 TCPv4_SERVER link local (bound): [AF_INET][undef]:443
    Sun Sep 13 17:02:16 2020 TCPv4_SERVER link remote: [AF_UNSPEC]
    Sun Sep 13 17:02:16 2020 MULTI: multi_init called, r=256 v=256
    Mon Sep 14 17:02:16 2020 IFCONFIG POOL: base=192.168.68.4 size=62, ipv6=0
    Sun Sep 13 17:02:16 2020 IFCONFIG POOL LIST
    Sun Sep 13 17:02:16 2020 MULTI: TCP INIT maxclients=1024 maxevents=1028
    Sun Sep 13 17:02:16 2020 Initialization Sequence Completed
    '''

  parser.parse(log_data)
  
  # Open file for analize
  # NOTE: Consider the path that you execute. Depending the terminal from
  #       what you are executing you should change this path
  # TODO: For the moment the file direction is hardcoded, but in future versions
  #       it should be a parameter reveiced via the UI

  # print(data)

  # # Give the lexer some input
  
  # tokens_output = open("tokens_output.txt", "w")
  # # Tokenize

  # lexer.input(log_data)
  # while True:
  #   tok = lexer.token()
  #   if not tok: 
  #     break      # No more input
  #   print(tok)

  #   # tokens_output.write(str(tok.value))
  #   tokens_output.write(f"{tok}\n")
  #   # tokens_output.write(f"{tok.type}: {tok.value}\n")
  # tokens_output.close()