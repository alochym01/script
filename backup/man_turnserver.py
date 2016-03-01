TURN(1)                                                                TURN(1)



GGEENNEERRAALL IINNFFOORRMMAATTIIOONN
       The  TTUURRNN  SSeerrvveerr project contains the source code of a TURN server and
       TURN client messaging library. Also, some extra programs provided,  for
       testing-only purposes.

       See the INSTALL file for the building instructions.

       After the build, you will have the following binary images:

       11..     _t_u_r_n_s_e_r_v_e_r: TTUURRNN SSeerrvveerr relay.  The compiled binary image of the
              TTUURRNN SSeerrvveerr program is located in bin/ sub-directory.

       22..     _t_u_r_n_a_d_m_i_n: TURN administration tool.  See  README.turnadmin  and
              _t_u_r_n_a_d_m_i_n man page.

       33..     turnutils_uclient.  See README.turnutils and _t_u_r_n_u_t_i_l_s man page.

       44..     turnutils_peer. See README.turnutils and _t_u_r_n_u_t_i_l_s man page.

       55..     turnutils_stunclient. See  README.turnutils  and  _t_u_r_n_u_t_i_l_s  man
              page.

       66..     turnutils_rfc5769check.  See  README.turnutils and _t_u_r_n_u_t_i_l_s man
              page.

       In the "examples/scripts" sub-directory, you will find the examples  of
       command  lines to be used to run the programs. The scripts are meant to
       be run from examples/ sub-directory, for example:

       $ cd examples $ ./scripts/secure_relay.sh

RRUUNNNNIINNGG TTHHEE TTUURRNN SSEERRVVEERR
       Options note: _t_u_r_n_s_e_r_v_e_r has long and  short  option  names,  for  most
       options.   Some  options  have  only  long form, some options have only
       short  form.  Their  syntax  somewhat  different,  if  an  argument  is
       required:

       The short form must be used as this (for example):

         $ turnserver -L 12.34.56.78

       The long form equivalent must use the "=" character:

         $ turnserver --listening-ip=12.34.56.78

       If  this  is  a flag option (no argument required) then their usage are
       the same, for example:

        $ turnserver -a

       is equivalent to:

        $ turnserver --lt-cred-mech

       =====================================

   NNAAMMEE
        ttuurrnnsseerrvveerr -- aa TTUURRNN rreellaayy sseerrvveerr iimmpplleemmeennttaattiioonn..

   SSYYNNOOPPSSIISS
       $ _t_u_r_n_s_e_r_v_e_r [--nn | --cc <config-file> ] [_f_l_a_g_s] [ ----uusseerrddbb=<userdb-file> | ----ppssqqll--uusseerrddbb=<db-conn-string> | ----mmyyssqqll--uusseerrddbb=<db-conn-string>  | ----mmoonnggoo--uusseerrddbb=<db-conn-string>  | ----rreeddiiss--uusseerrddbb=<db-conn-string> ] [--zz | ----nnoo--aauutthh | --aa | ----lltt--ccrreedd--mmeecchh ] [_o_p_t_i_o_n_s]
       $ _t_u_r_n_s_e_r_v_e_r --hh


   DDEESSCCRRIIPPTTIIOONN
       CCoonnffiigg ffiillee sseettttiinnggss::

       --nn     Do not use configuration file, use only command line parameters.

       --cc     Configuration file name (default - turnserver.conf).  The format
              of  config  file   can   be   seen   in   the   supplied   exam-
              ples/etc/turnserver.conf example file. Long names of the _o_p_t_i_o_n_s
              are used as the configuration items names in the file. If not an
              absolute path is supplied, then the file is searched in the fol-
              lowing directories:

              ·  current directory

              ·  current directory etc/ sub-directory

              ·  upper directory level etc/

              ·  /etc/

              ·  /usr/local/etc/

              ·  installation directory /etc

       UUsseerr ddaattaabbaassee sseettttiinnggss::

       --bb,, ----ddbb,, ----uusseerrddbb
              SQLite user database file  name  (default  -  /var/db/turndb  or
              /usr/local/var/db/turndb or /var/lib/turn/turndb).

       --ee,, ----ppssqqll--uusseerrddbb
              User  database  connection string for PostgreSQL.  This database
              can be used for long-term  credentials  mechanism,  and  it  can
              store  the secret value for secret-based timed authentication in
              TURN RESP API.  The connection string format is like that:

              "host=<host>      dbname=<dbname>      user=<db-user>      pass-
              word=<db-user-password>  connect_timeout=<seconds>"  (for 8.x or
              newer Postgres).

              Or:

              "postgresql://username:password@hostname:port/databasename" (for
              9.x or newer Postgres).

              See the INSTALL file for more explanations and examples.

              Also, see http://www.PostgreSQL.org for full PostgreSQL documen-
              tation.

       --MM,, ----mmyyssqqll--uusseerrddbb
              User database connection string  for  MySQL  or  MariaDB.   This
              database can be used for long-term credentials mechanism, and it
              can store the secret value for secret-based timed authentication
              in TURN RESP API.  The connection string format is like that:

              "host=<host>      dbname=<dbname>      user=<db-user>      pass-
              word=<db-user-password> connect_timeout=<seconds>"

              See the INSTALL file for more explanations and examples.

              Also, see http://www.mysql.org or  http://mariadb.org  for  full
              MySQL documentation.

              Optional  connection string parameters for the secure communica-
              tions   (SSL):   ca,   capath,   cert,    key,    cipher    (see
              http://dev.mysql.com/doc/refman/5.1/en/ssl-options.html  for the
              command _o_p_t_i_o_n_s description).

       --JJ,, ----mmoonnggoo--uusseerrddbb
              User database connection string for MongoDB.  This database  can
              be  used  for  long-term credentials mechanism, and it can store
              the secret value for secret-based timed authentication  in  TURN
              RESP API.  The connection string format is like that:

              "mongodb://username:password@host:port/database?_o_p_t_i_o_n_s"

              See the INSTALL file for more explanations and examples.

              Also, see http://docs.mongodb.org/manual/ for full MongoDB docu-
              mentation.

       --NN,, ----rreeddiiss--uusseerrddbb
              User database connection string for Redis.  This database can be
              used  for  long-term credentials mechanism, and it can store the
              secret value for secret-based timed authentication in TURN  RESP
              API.  The connection string format is like that:

              "ip=<ip-addr>   dbname=<db-number>  password=<db-password>  con-
              nect_timeout=<seconds>"

              See the INSTALL file for more explanations and examples.

              Also, see http://redis.io for full Redis documentation.

       FFllaaggss::

       --vv,, ----vveerrbboossee
              Moderate verbose mode.

       --VV,, ----VVeerrbboossee
              Extra verbose mode, very annoying and not recommended.

       --oo,, ----ddaaeemmoonn
              Run server as daemon.

       --ff,, ----ffiinnggeerrpprriinntt
              Use fingerprints in the TURN messages. If  an  incoming  request
              contains a fingerprint, then TURN server will always add finger-
              prints to the  messages  in  this  session,  regardless  of  the
              per-server setting.

       --aa,, ----lltt--ccrreedd--mmeecchh
              Use  long-term  credentials  mechanism  (this  one  you need for
              WebRTC usage).

       --zz,, ----nnoo--aauutthh
              Do not use any credentials mechanism,  allow  anonymous  access.
              Opposite  to  --aa  and --AA _o_p_t_i_o_n_s. This is default option when no
              authentication-related _o_p_t_i_o_n_s are set.  By default, no  creden-
              tial mechanism is used - any user is allowed.

       ----uussee--aauutthh--sseeccrreett
              TURN  REST API flag.  Flag that sets a special WebRTC authoriza-
              tion option that is based upon authentication secret.  The  fea-
              ture  purpose  is to support "TTUURRNN SSeerrvveerr REST API" as described
              in the TURN REST API section below.  This option uses  timestamp
              as part of combined username: usercombo -> "timestamp:username",
              turn     user     ->     usercombo,     turn     password     ->
              bbaassee6644(hmac(input_buffer  =  usercombo,  key  = shared-secret)).
              This allows TURN credentials to be accounted for a specific user
              id.  If you don’t have a suitable id, the timestamp alone can be
              used.  This option is just turns on secret-based authentication.
              The  actual  value  of  the  secret  is defined either by option
              static-auth-secret, or can be found in the turn_secret table  in
              the database.

       ----ooaauutthh
              Support  oAuth  authentication,  as in the third-party STUN/TURN
              RFC 7635.

       ----ddhh556666
              Use 566 bits predefined DH TLS key. Default size of the  key  is
              1066.

       ----ddhh22006666
              Use  2066 bits predefined DH TLS key. Default size of the key is
              1066.

       ----nnoo--ssssllvv33
              Do not allow SSLv3 protocol.

       ----nnoo--ttllssvv11
              Do not allow TLSv1/DTLSv1 protocol.

       ----nnoo--ttllssvv11__11
              Do not allow TLSv1.1 protocol.

       ----nnoo--ttllssvv11__22
              Do not allow TLSv1.2/DTLSv1.2 protocol.

       ----nnoo--uuddpp
              Do not start UDP client listeners.

       ----nnoo--ttccpp
              Do not start TCP client listeners.

       ----nnoo--ttllss
              Do not start TLS client listeners.

       ----nnoo--ddttllss
              Do not start DTLS client listeners.

       ----nnoo--uuddpp--rreellaayy
              Do not allow UDP relay endpoints defined in RFC 5766,  use  only
              TCP relay endpoints as defined in RFC 6062.

       ----nnoo--ttccpp--rreellaayy
              Do  not  allow TCP relay endpoints defined in RFC 6062, use only
              UDP relay endpoints as defined in RFC 5766.

       ----ssttaallee--nnoonnccee
              Use extra security with nonce value having limited lifetime (600
              secs).

       ----nnoo--ssttddoouutt--lloogg
              Flag  to  prevent stdout log messages.  By default, all log mes-
              sages are going to both stdout and to the configured  log  file.
              With  this  option everything will be going to the log file only
              (unless the log file itself is stdout).

       ----ssyysslloogg
              With this flag, all log will be redirected  to  the  system  log
              (syslog).

       ----ssiimmppllee--lloogg
              This  flag means that no log file rollover will be used, and the
              log file name will be constructed as-is, without  PID  and  date
              appendage.   This option can be used, for example, together with
              the logrotate tool.

       ----sseeccuurree--ssttuunn
              Require authentication of the STUN Binding request.  By default,
              the  clients  are  allowed  anonymous access to the STUN Binding
              functionality.

       --SS,, ----ssttuunn--oonnllyy
              Run as STUN server only, all  TURN  requests  will  be  ignored.
              Option  to  suppress TURN functionality, only STUN requests will
              be processed.

       ----nnoo--ssttuunn
              Run as TURN server only, all  STUN  requests  will  be  ignored.
              Option  to  suppress STUN functionality, only TURN requests will
              be processed.

       ----nnoo--llooooppbbaacckk--ppeeeerrss
              Disallow peers on the loopback addresses (127.x.x.x and ::1).

       ----nnoo--mmuullttiiccaasstt--ppeeeerrss
              Disallow peers on well-known broadcast addresses (224.0.0.0  and
              above, and FFXX:*).

       ----mmoobbiilliittyy
              Mobility with ICE (MICE) specs support.

       ----nnoo--ccllii
              Turn  OFF the CLI support. By default it is always ON.  See also
              _o_p_t_i_o_n_s ----ccllii--iipp and ----ccllii--ppoorrtt.

       ----sseerrvveerr--rreellaayy
              Server relay. NON-STANDARD AND DANGEROUS OPTION.  Only for those
              applications  when  we  want  to  run server applications on the
              relay endpoints.  This  option  eliminates  the  IP  permissions
              check  on  the  packets  incoming  to  the relay endpoints.  See
              http://tools.ietf.org/search/rfc5766#section-17.2.3 .

       ----uuddpp--sseellff--bbaallaannccee
              (recommended for older Linuxes only) Automatically  balance  UDP
              traffic over auxiliary servers (if configured). The load balanc-
              ing is using the ALTERNATE-SERVER  mechanism.  The  TURN  client
              must  support 300 ALTERNATE-SERVER response for this functional-
              ity.

       ----cchheecckk--oorriiggiinn--ccoonnssiisstteennccyy
              The flag that sets the origin consistency check: across the ses-
              sion,  all  requests  must  have  the same main ORIGIN attribute
              value (if the ORIGIN was initially used by the session).

       --hh     Help.

       OOppttiioonnss wwiitthh rreeqquuiirreedd vvaalluueess::

       --dd,, ----lliisstteenniinngg--ddeevviiccee
              Listener interface device.  (NOT RECOMMENDED. Optional function-
              ality, Linux only).  The _t_u_r_n_s_e_r_v_e_r process must have root priv-
              ileges to bind the listening endpoint to a device. If _t_u_r_n_s_e_r_v_e_r
              must  run as a process without root privileges, then just do not
              use this setting.

       --LL,, ----lliisstteenniinngg--iipp
              Listener IP address of relay server.  Multiple listeners can  be
              specified,  for example: --LL ip1 --LL ip2 --LL ip3 If no IIPP(s) speci-
              fied, then all IPv4 and IPv6 system IPs will be used for listen-
              ing.   The  same  iipp(s)  can be used as both listening and relay
              iipp(s).

       --pp,, ----lliisstteenniinngg--ppoorrtt
              TURN listener port for UDP and TCP  listeners  (Default:  3478).
              Note:  actually,  TLS & DTLS sessions can connect to the "plain"
              TCP & UDP ppoorrtt(s), too - if allowed by configuration.

       ----ttllss--lliisstteenniinngg--ppoorrtt
              TURN listener port for TLS and DTLS listeners  (Default:  5349).
              Note:  actually,  "plain"  TCP & UDP sessions can connect to the
              TLS & DTLS ppoorrtt(s), too - if allowed by configuration. The  TURN
              server "automatically" recognizes the type of traffic. Actually,
              two listening endpoints (the "plain" one and the "tls" one)  are
              equivalent in terms of functionality; but we keep both endpoints
              to satisfy the RFC 5766 specs.  For secure TCP  connections,  we
              currently  support SSL version 3 and TLS versions 1.0, 1.1, 1.2.
              For secure UDP connections, we support DTLS version 1.

       ----aalltt--lliisstteenniinngg--ppoorrtt
              Alternative listening port for UDP and  TCP  listeners;  default
              (or zero) value means "listening port plus one".  This is needed
              for STUN CHANGE_REQUEST - in RFC 5780 sense or in old  RFC  3489
              sense  -  for  NAT behavior discovery). The TTUURRNN SSeerrvveerr supports
              CHANGE_REQUEST only if it is started with more than one  listen-
              ing   IP  address  of  the  same  family  (IPv4  or  IPv6).  The
              CHANGE_REQUEST is only supported by UDP protocol,  other  proto-
              cols are listening on that endpoint only for "symmetry".

       ----aalltt--ttllss--lliisstteenniinngg--ppoorrtt
              Alternative  listening port for TLS and DTLS protocols.  Default
              (or zero) value means "TLS listening port plus one".

       ----aauuxx--sseerrvveerr
              Auxiliary STUN/TURN server listening endpoint.  Aux servers have
              almost  full  TURN  and STUN functionality.  The (minor) limita-
              tions are:

              1)  Auxiliary servers do not have alternative ports and they  do
                  not support STUN RFC 5780 functionality (CHANGE REQUEST).

              2)  Auxiliary   servers   also   are  never  returning  ALTERNA-
                  TIVE-SERVER reply.

       Valid formats are 1.2.3.4:5555 for IPv4 and [1:2::3:4]:5555  for  IPv6.
       There may be multiple aux-server _o_p_t_i_o_n_s, each will be used for listen-
       ing to client requests.

       --ii,, ----rreellaayy--ddeevviiccee
              Relay interface  device  for  relay  sockets  (NOT  RECOMMENDED.
              Optional, Linux only).

       --EE,, ----rreellaayy--iipp
              Relay  address  (the local IP address that will be used to relay
              the packets to the peer). Multiple relay addresses may be  used:
              --EE  ip1 --EE ip2 --EE ip3 The same IIPP(s) can be used as both listen-
              ing IIPP(s) and relay IIPP(s).  If no relay  IIPP(s)  specified,  then
              the  _t_u_r_n_s_e_r_v_e_r  will  apply  the default policy: it will decide
              itself which relay addresses to be used, and it will  always  be
              using  the  client  socket IP address as the relay IP address of
              the TURN session (if the requested relay address family  is  the
              same as the family of the client socket).

       --XX,, ----eexxtteerrnnaall--iipp
              TTUURRNN  SSeerrvveerr  public/private  address  mapping, if the server is
              behind NAT.  In that situation, if a --XX  is  used  in  form  "--XX
              <ip>"  then  that ip will be reported as relay IP address of all
              allocations. This scenario works only in a simple case when  one
              single relay address is be used, and no CHANGE_REQUEST function-
              ality is required. That single relay address must be  mapped  by
              NAT  to  the  ’external’  IP.   The  "external-ip" value, if not
              empty, is  returned  in  XOR-RELAYED-ADDRESS  field.   For  that
              ’external’  IP,  NAT  must  forward ports directly (relayed port
              12345 must be always mapped to the same ’external’ port  12345).
              In  more complex case when more than one IP address is involved,
              that option must be used several times,  each  entry  must  have
              form "--XX <public-ip/private-ip>", to map all involved addresses.
              CHANGE_REQUEST (RFC5780 or RFC3489) NAT discovery STUN function-
              ality will work correctly, if the addresses are mapped properly,
              even when the TURN server itself is behind A NAT.   By  default,
              this value is empty, and no address mapping is used.

       --mm,, ----rreellaayy--tthhrreeaaddss
              Number  of  the  relay threads to handle the established connec-
              tions (in addition to authentication  thread  and  the  listener
              thread).   If  explicitly  set  to 0 then application runs relay
              process in a single thread, in the same thread with the listener
              process  (the  authentication  thread  will  still be a separate
              thread). If not set, then a default optimal  algorithm  will  be
              employed  (OS-dependent).  In  the  older  Linux systems (before
              Linux kernel 3.9), the number  of  UDP  threads  is  always  one
              threads per network listening endpoint - unless "--mm 0" or "--mm 1"
              is set.

       ----mmiinn--ppoorrtt
              Lower bound of the UDP port range for  relay  endpoints  alloca-
              tion.  Default value is 49152, according to RFC 5766.

       ----mmaaxx--ppoorrtt
              Upper  bound  of  the UDP port range for relay endpoints alloca-
              tion.  Default value is 65535, according to RFC 5766.

       --uu,, ----uusseerr
              Long-term security mechanism credentials user  account,  in  the
              column-separated  form username:key.  Multiple user accounts may
              used in the command line.  The key is either the user  password,
              or  the  key  is  generated  by _t_u_r_n_a_d_m_i_n command. In the second
              case, the key must be prepended with 0x  symbols.   The  key  is
              calculated  over  the  user  name,  the user realm, and the user
              password.  This setting may not be used with TURN REST API.

       --rr,, ----rreeaallmm
              The default realm to be used for the users when no explicit ori-
              gin/realm relationship was found in the database, or if the TURN
              server is not using any database (just  the  commands-line  set-
              tings  and the userdb file). Must be used with long-term creden-
              tials mechanism or with TURN REST API.

       --CC,, ----rreesstt--aappii--sseeppaarraattoorr
              This is the timestamp/username separator symbol  (character)  in
              TURN REST API. The default value is :.

       --qq,, ----uusseerr--qquuoottaa
              Per-user  allocations  quota:  how many concurrent allocations a
              user can create.  This  option  can  also  be  set  through  the
              database, for a particular realm.

       --QQ,, ----ttoottaall--qquuoottaa
              Total allocations quota: global limit on concurrent allocations.
              This option can also be set through the database, for a particu-
              lar realm.

       --ss,, ----mmaaxx--bbppss
              Max bytes-per-second bandwidth a TURN session is allowed to han-
              dle (input and output network streams are  treated  separately).
              Anything  above  that  limit  will  be dropped or temporary sup-
              pressed (within the available buffer limits).  This  option  can
              also be set through the database, for a particular realm.

       --BB,, ----bbppss--ccaappaacciittyy
              Maximum  server  capacity.  Total bytes-per-second bandwidth the
              TURN server is allowed to allocate for  the  sessions,  combined
              (input and output network streams are treated separately).

       ----ssttaattiicc--aauutthh--sseeccrreett
              Static  authentication secret value (a string) for TURN REST API
              only.  If not set, then the turn server  will  try  to  use  the
              dynamic   value  in  turn_secret  table  in  user  database  (if
              present). The database-stored value can be changed on-the-fly by
              a  separate  program, so this is why that other mode is dynamic.
              Multiple shared secrets can be used (both in the database and in
              the "static" fashion).

       ----sseerrvveerr--nnaammee
              Server  name  used  for  the oAuth authentication purposes.  The
              default value is the realm name.

       ----cceerrtt Certificate file, PEM format. Same file search rules applied  as
              for  the  configuration  file.  If  both  ----nnoo--ttllss and ----nnoo--ddttllss
              _o_p_t_i_o_n_s are  specified,  then  this  parameter  is  not  needed.
              Default value is turn_server_cert.pem.

       ----ppkkeeyy Private  key file, PEM format. Same file search rules applied as
              for the configuration  file.  If  both  ----nnoo--ttllss  and  ----nnoo--ddttllss
              _o_p_t_i_o_n_s  are  specified,  then  this  parameter  is  not needed.
              Default value is turn_server_pkey.pem.

       ----ppkkeeyy--ppwwdd
              If the private key file is encrypted, then this password  to  be
              used.

       ----cciipphheerr--lliisstt
              Allowed  OpenSSL  cipher list for TLS/DTLS connections.  Default
              value is "DEFAULT".

       ----CCAA--ffiillee
              CA file in OpenSSL format.  Forces TURN  server  to  verify  the
              client SSL certificates.  By default, no CA is set and no client
              certificate check is performed.

       ----eecc--ccuurrvvee--nnaammee
              Curve name for EC ciphers, if supported by OpenSSL library  (TLS
              and DTLS). The default value is prime256v1, if pre-OpenSSL 1.0.2
              is used. With OpenSSL 1.0.2+, an optimal curve will be automati-
              cally calculated, if not defined by this option.

       ----ddhh--ffiillee
              Use  custom DH TLS key, stored in PEM format in the file.  Flags
              ----ddhh556666 and ----ddhh22006666 are ignored when the DH key is taken from a
              file.

       --ll,, ----lloogg--ffiillee
              Option  to  set the full path name of the log file.  By default,
              the _t_u_r_n_s_e_r_v_e_r tries to open a log file in  /var/log/_t_u_r_n_s_e_r_v_e_r,
              /var/log, /var/tmp, /tmp and . (current) directories (which file
              open operation succeeds first that file will be used). With this
              option  you  can  set  the  definite log file name.  The special
              names are "stdout" and "-" - they will force everything  to  the
              stdout.  Also,  "syslog"  name will redirect everything into the
              system log (syslog), as if the option "----ssyysslloogg"  was  set.   In
              the  runtime, the logfile can be reset with the SIGHUP signal to
              the _t_u_r_n_s_e_r_v_e_r process.

       ----aalltteerrnnaattee--sseerrvveerr
              Option to set the "redirection" mode. The value of  this  option
              will  be  the  address  of  the  alternate  server for UDP & TCP
              service in form of <ip>[:<port>].  The  server  will  send  this
              value  in  the  attribute  ALTERNATE-SERVER,  with error 300, on
              ALLOCATE request, to the client.  Client will receive only  val-
              ues  with the same address family as the client network endpoint
              address family.  See RFC 5389 and RFC 5766 for  ALTERNATE-SERVER
              functionality  description.   The  client  must use the obtained
              value for subsequent TURN  communications.   If  more  than  one
              ----aalltteerrnnaattee--sseerrvveerr  _o_p_t_i_o_n_s are provided, then the functionality
              can be more accurately described as "load-balancing" than a mere
              "redirection".   If the port number is omitted, then the default
              port number 3478 for the UDP/TCP protocols will be used.   Colon
              (:) characters in IPv6 addresses may conflict with the syntax of
              the option. To alleviate this conflict, literal  IPv6  addresses
              are  enclosed  in  square brackets in such resource identifiers,
              for example: [2001:db8:85a3:8d3:1319:8a2e:370:7348]:3478 .  Mul-
              tiple  alternate  servers  can  be set. They will be used in the
              round-robin manner. All servers in the pool  are  considered  of
              equal weight and the load will be distributed equally. For exam-
              ple, if we have 4  alternate  servers,  then  each  server  will
              receive  25%  of  ALLOCATE  requests.  An  alternate TURN server
              address can be used more than one time with the alternate-server
              option, so this can emulate "weighting" of the servers.

       ----ttllss--aalltteerrnnaattee--sseerrvveerr
              Option to set alternative server for TLS & DTLS services in form
              of <ip>:<port>. If the port number is omitted, then the  default
              port  number  5349  for the TLS/DTLS protocols will be used. See
              the previous option for the functionality description.

       --OO,, ----rreeddiiss--ssttaattssddbb
              Redis status and statistics database connection string, if  used
              (default  -  empty, no Redis stats DB used). This database keeps
              allocations status information, and it can be also used for pub-
              lishing  and  delivering  traffic and allocation event notifica-
              tions.  This  database  option  can  be  used  independently  of
              ----rreeddiiss--uusseerrddbb  option,  and actually Redis can be used for sta-
              tus/statistics and SQLite or MySQL or MongoDB or PostgreSQL  can
              be  used  for  the user database.  The connection string has the
              same parameters as redis-userdb connection string.

       ----mmaaxx--aallllooccaattee--ttiimmeeoouutt
              Max time, in seconds, allowed for full allocation establishment.
              Default is 60 seconds.

       ----ddeenniieedd--ppeeeerr--iipp=<IPaddr[--IIPPaaddddrr]>

       ----aalllloowweedd--ppeeeerr--iipp=<IPaddr[--IIPPaaddddrr]> Options to ban or allow specific ip
       addresses or ranges of ip addresses. If an ip address is  specified  as
       both  allowed  and  denied,  then  the  ip  address is considered to be
       allowed. This is useful when you wish to ban a range of  ip  addresses,
       except for a few specific ips within that range.  This can be used when
       you do not want users of the turn server to be able to access  machines
       reachable  by  the turn server, but would otherwise be unreachable from
       the internet (e.g. when the turn server is sitting behind a  NAT).  The
       ’white"  and  "black" peer IP ranges can also be dynamically changed in
       the database.  The allowed/denied addresses (white/black  lists)  rules
       are very simple:

              1)  If there is no rule for an address, then it is allowed;

              2)  If  there is an "allowed" rule that fits the address then it
                  is allowed - no matter what;

              3)  If there is no "allowed" rule that fits the address, and  if
                  there  is  a "denied" rule that fits the address, then it is
                  denied.

       ----ppiiddffiillee
              File  name  to  store  the  pid  of  the  process.   Default  is
              /var/run/turnserver.pid   (if  superuser  account  is  used)  or
              /var/tmp/turnserver.pid .

       ----pprroocc--uusseerr
              User name to run the  process.  After  the  initialization,  the
              _t_u_r_n_s_e_r_v_e_r  process  will  make an attempt to change the current
              user ID to that user.

       ----pprroocc--ggrroouupp
              Group name to run the process.  After  the  initialization,  the
              _t_u_r_n_s_e_r_v_e_r  process  will  make an attempt to change the current
              group ID to that group.

       ----ccllii--iipp
              Local system IP address to be used for CLI management interface.
              The  _t_u_r_n_s_e_r_v_e_r process can be accessed for management with tel-
              net, at this IP address and on the CLI port (see the next param-
              eter).   Default value is 127.0.0.1. You can use telnet or putty
              (in telnet mode) to access the CLI management interface.

       ----ccllii--ppoorrtt
              CLI management interface listening port. Default is 5766.

       ----ccllii--ppaasssswwoorrdd
              CLI access password. Default is empty (no  password).   For  the
              security reasons, it is recommended to use the encrypted form of
              the password (see the --PP command in the _t_u_r_n_a_d_m_i_n utility).  The
              dollar signs in the encrypted form must be escaped.

       ----ccllii--mmaaxx--oouuttppuutt--sseessssiioonnss
              Maximum number of output sessions in ps CLI command.  This value
              can be changed on-the-fly in CLI. The default value is 256.

       ----nnee==[[11||22||33]]
              Set network engine type for the process (for internal purposes).

       ==================================

LLOOAADD BBAALLAANNCCEE AANNDD PPEERRFFOORRMMAANNCCEE TTUUNNIINNGG
       This topic is covered in the wiki page:

       https://github.com/coturn/coturn/wiki/turn_performance_and_load_balance

       ===================================

WWEEBBRRTTCC UUSSAAGGEE
       This is a set of notes for the WebRTC users:

       1)  WebRTC uses long-term authentication mechanism, so you have to  use
           --aa  option  (or ----lltt--ccrreedd--mmeecchh). WebRTC relaying will not work with
           anonymous access. With --aa option, do not forget to set the  default
           realm  (--rr option). You will also have to set up the user accounts,
           for that you have a number of _o_p_t_i_o_n_s:

               a) command-line options (-u).

               b) a database table (SQLite or PostgreSQL or MySQL or MongoDB). You will have to
               set keys with turnadmin utility (see docs and wiki for turnadmin).
               You cannot use open passwords in the database.

               c) Redis key/value pair(s), if Redis is used. You key use either keys or
               open passwords with Redis; see turndb/testredisdbsetup.sh file.

               d) You also can use the TURN REST API. You will need shared secret(s) set
               either  through the command line option, or through the config file, or through
               the database table or Redis key/value pairs.


       2)  Usually WebRTC uses fingerprinting (--ff).

       3)  --vv option may be nice to see the connected clients.

       4)  --XX is needed if you are running your TURN server behind a NAT.

       5)  ----mmiinn--ppoorrtt and ----mmaaxx--ppoorrtt may be needed if you want  to  limit  the
           relay endpoints ports number range.

       ===================================

TTUURRNN RREESSTT AAPPII
       In WebRTC, the browser obtains the TURN connection information from the
       web server. This information is a secure information - because it  con-
       tains  the  necessary TURN credentials. As these credentials are trans-
       mitted over the public networks, we have a potential security breach.

       If we have to transmit a valuable information over the public  network,
       then  this information has to have a limited lifetime. Then the guy who
       obtains this information without permission will  be  able  to  perform
       only limited damage.

       This is how the idea of TURN REST API - time-limited TURN credentials -
       appeared. This security mechanism is based upon the  long-term  creden-
       tials  mechanism.  The main idea of the REST API is that the web server
       provides the credentials to the client, but those  credentials  can  be
       used  only  limited  time  by  an application that has to create a TURN
       server connection.

       The "classic" long-term credentials mechanism (LTCM) is described here:

       http://tools.ietf.org/html/rfc5389#section-10.2

       http://tools.ietf.org/html/rfc5389#section-15.4

       For  authentication,  each  user must know two things: the username and
       the password. Optionally, the user must supply  the  ORIGIN  value,  so
       that  the  server can figure out the realm to be used for the user. The
       nonce and the realm values are supplied by the TURN server. But LTCM is
       not  saying  anything about the nature and about the persistence of the
       username and of the password; and this is used by the REST API.

       In the TURN REST API, there is no persistent  passwords  for  users.  A
       user has just the username. The password is always temporary, and it is
       generated by the web server  on-demand,  when  the  user  accesses  the
       WebRTC page. And, actually, a temporary one-time session only, username
       is provided to the user, too.

       The temporary user is generated as:

       temporary-username="timestamp" + ":" + "username"

       where username is the persistent user name, and the timestamp format is
       just  seconds  sinse  1970  -  the  same  value  as ttiimmee(NULL) function
       returns.

       The temporary password is obtained as HMAC-SHA1 function over the  tem-
       porary  username,  with  shared  secret  as  the HMAC key, and then the
       result is encoded:

       temporary-password  =   bbaassee6644__eennccooddee(hmac-sha1(shared-secret,   tempo-
       rary-username))

       Both  the  TURN  server and the web server know the same shared secret.
       How the shared secret is distributed among  the  involved  entities  is
       left to the WebRTC deployment details - this is beyond the scope of the
       TURN REST API.

       So, a timestamp is used for the  temporary  password  calculation,  and
       this  timestamp  can  be  retrieved  from  the temporary username. This
       information is valuable, but only temporary, while the timestamp is not
       expired.  Without knowledge of the shared secret, a new temporary pass-
       word cannot be generated.

       This is all  formally  described  in  Justin’s  Uberti  TURN  REST  API
       document that can be obtained following the link "TURN REST API" in the
       TTUURRNN SSeerrvveerr project’s page https://github.com/coturn/coturn/.

       Once the temporary username and password are  obtained  by  the  client
       (browser)  application,  then the rest is just ’classic" long-term cre-
       dentials mechanism.  For  developers,  we  are  going  to  describe  it
       step-by-step below:

              ·  a new TURN client sends a request command to the TURN server.
                 Optionally, it adds the ORIGIN field to it.

              ·  TURN server sees that this is a new client and the message is
                 not authenticated.

              ·  the  TURN  server generates a random nonce string, and return
                 the error 401 to the client, with nonce and  realm  included.
                 If the ORIGIN field was present in the client request, it may
                 affect the realm  value  that  the  server  chooses  for  the
                 client.

              ·  the client sees the 401 error and it extracts two values from
                 the error response: the nonce and the realm.

              ·  the client uses username, realm and  password  to  produce  a
                 key:

                       key = MD5(username ":" realm ":" SASLprep(password))
              (SASLprep is described here: http://tools.ietf.org/html/rfc4013)

              ·  the client forms a new  request,  adds  username,  realm  and
                 nonce  to  the  request. Then, the client calculates and adds
                 the integrity field to the request.  This  is  the  trickiest
                 part  of  the process, and it is described in the end of sec-
                 tion 15.4: http://tools.ietf.org/html/rfc5389#section-15.4

              ·  the client, optionally, adds the fingerprint field. This  may
                 be  also a tricky procedure, described in section 15.5 of the
                 same document.  WebRTC usually uses fingerprinted  TURN  mes-
                 sages.

              ·  the TURN server receives the request, reads the username.

              ·  then  the  TURN server checks that the nonce and the realm in
                 the request are the valid ones.

              ·  then the TURN server calculates the key.

              ·  then the TURN server calculates the integrity field.

              ·  then the TURN server compares the calculated integrity  field
                 with  the  received  one  -  they  must  be  the same. If the
                 integrity fields differ, then the request is rejected.

       In subsequent communications, the client may go with exactly  the  same
       sequence,  but  for  optimization  usually  the  client, having already
       information about realm and nonce, pre-calculates the integrity  string
       for  each  request, so that the 401 error response becomes unnecessary.
       The TURN server may use "----ssttaallee--nnoonnccee" option for extra  security:  in
       some  time,  the  nonce  expires  and  the client will obtain 438 error
       response with the new nonce, and the client will have  to  start  using
       the new nonce.

       In  subsequent  communications,  the  sever  and the client will always
       assume the same password - the original password  becomes  the  session
       parameter  and is never expiring. So the password is not changing while
       the session is valid and unexpired. So,  if  the  session  is  properly
       maintained,  it  may  go  forever,  even  if the user password has been
       already changed (in the database). The session simply is using the  old
       password.  Once  the  session got disconnected, the client will have to
       use the new password to re-connect (if the password has been  changed).

       An example when a new shared secret is generated every hour by the TURN
       server box and then supplied to the web server, remotely,  is  provided
       in the script examples/scripts/restapi/shared_secret_maintainer.pl .

       A  very important thing is that the nonce must be totally random and it
       must be different for different clients and different sessions.

       ===================================

DDAATTAABBAASSEESS
       For the user database, the _t_u_r_n_s_e_r_v_e_r has the following _o_p_t_i_o_n_s:

       1)  Users can be set in the command line, with multiple  --uu  or  ----uusseerr
           _o_p_t_i_o_n_s.   Obviously,  only  a  few  users can be set that way, and
           their credentials are fixed for the _t_u_r_n_s_e_r_v_e_r process lifetime.

       2)  Users can be stored in SQLite DB. The default SQLite database  file
           is      /var/db/turndb      or      /usr/local/var/db/turndb     or
           /var/lib/turn/turndb.

       3)  Users can be stored in PostgreSQL database, if the  _t_u_r_n_s_e_r_v_e_r  was
           compiled  with PostgreSQL support. Each time _t_u_r_n_s_e_r_v_e_r checks user
           credentials, it reads the database (asynchronously, of  course,  so
           that the current flow of packets is not delayed in any way), so any
           change in the  database  content  is  immediately  visible  by  the
           _t_u_r_n_s_e_r_v_e_r.  This  is the way if you need the best scalability. The
           schema for the database can  be  found  in  schema.sql  file.   For
           long-term  credentials,  you  have to set the "keys" for the users;
           the "keys" are generated by the _t_u_r_n_a_d_m_i_n utility. For the key gen-
           eration,  you  need username, password and the realm.  All users in
           the database must use the same realm value; if down  the  road  you
           will decide to change the realm name, then you will have to re-gen-
           erate all user keys (that can be done in a batch script).  See  the
           file turndb/testsqldbsetup.sql as an example.

       4)  The same is true for MySQL database. The same schema file is appli-
           cable.  The same considerations are applicable.

       5)  The same is true for the Redis database, but the Redis database has
           aa  different schema - it can be found (in the form of explanation)
           in schema.userdb.redis.  Also, in Redis you can store  both  "keys"
           and  open  passwords  (for long term credentials) - the "open pass-
           word" option is less secure but more  convenient  for  low-security
           environments.   See the file turndb/testredisdbsetup.sh as an exam-
           ple.

       6)  If a database is used, then users  can  be  divided  into  multiple
           independent  realms. Each realm can be administered separately, and
           each realm can have its own set of users and  its  own  performance
           _o_p_t_i_o_n_s (max-bps, user-quota, total-quota).

       7)  If  you  use  MongoDB, the database will be setup for you automati-
           cally.

       8)  Of course, the _t_u_r_n_s_e_r_v_e_r can be  used  in  non-secure  mode,  when
           users  are  allowed  to establish sessions anonymously. But in most
           cases (like WebRTC) that will not work.

       For the status and statistics database, there are two choices:

       1)  The simplest choice is not to use it. Do  not  set  ----rreeddiiss--ssttaattssddbb
           option, and this functionality will be simply ignored.

       2)  If  you choose to use it, then set the ----rreeddiiss--ssttaattssddbb option. This
           may be the same database as in ----rreeddiiss--uusseerrddbb option, or it may  be
           a  different  database.  You may want to use different database for
           security or  convenience  reasons.  Also,  you  can  use  different
           database  management systems for the user database and for the sts-
           tus and statistics database. For example, you can use MySQL as  the
           user database, and you can use redis for the statistics. Or you can
           use Redis for both.

       So, we have 6 choices for the user management, and 2  choices  for  the
       statistics  management. These two are totally independent. So, you have
       overall 6*2=12 ways to handle persistent information,  choose  any  for
       your convenience.

       You  do  not  have  to handle the database information "manually" - the
       _t_u_r_n_a_d_m_i_n program can handle everything for  you.  For  PostgreSQL  and
       MySQL  you  will  just have to create an empty database with schema.sql
       SQL script. With Redis, you do not have to do even that - just run _t_u_r_-
       _n_a_d_m_i_n  and  it will set the users for you (see the _t_u_r_n_a_d_m_i_n manuals).
       If you are using SQLite, then the _t_u_r_n_s_e_r_v_e_r or _t_u_r_n_a_d_m_i_n will initial-
       ize  the empty database, for you, when started. The TURN server instal-
       lation process creates an empty  initialized  SQLite  database  in  the
       default   location   (/var/db/turndb   or  /usr/local/var/db/turndb  or
       /var/lib/turn/turndb, depending on the system).

       =================================

AALLPPNN
       The server supports ALPNs "stun.turn"  and  "stun.nat-discovery",  when
       compiled with OpenSSL 1.0.2 or newer. If the server receives a TLS/DTLS
       ClientHello message that contains one or both of those ALPNs, then  the
       server chooses the first stun.* label and sends it back (in the Server-
       Hello) in the ALPN extension field. If no stun.* label is  found,  then
       the  server does not include the ALPN information into the ServerHello.

       =================================

LLIIBBRRAARRIIEESS
       In the lib/ sub-directory the build process  will  create  TURN  client
       messaging  library.   In  the  include/  sub-directory,  the  necessary
       include files will be placed.  The C++ wrapper for the messaging  func-
       tionality  is  located  in TurnMsgLib.h header.  An example of C++ code
       can be found in stunclient.c file.

       =================================

DDOOCCSS
       After installation, run the command:

       $ man _t_u_r_n_s_e_r_v_e_r

       or in the project root directory:

       $ man --MM man _t_u_r_n_s_e_r_v_e_r

       to see the man page.

       In the docs/html subdirectory of the original archive  tree,  you  will
       find  the  client library reference. After the installation, it will be
       placed in PREFIX/share/doc/_t_u_r_n_s_e_r_v_e_r/html.

       =================================

LLOOGGSS
       When the TTUURRNN SSeerrvveerr starts, it makes efforts  to  create  a  log  file
       turn_<pid>.log in the following directories:

              ·  /var/log

              ·  /log/

              ·  /var/tmp

              ·  /tmp

              ·  current directory

       If  all efforts failed (due to the system permission settings) then all
       log messages are sent only to the standard output of the process.

       This behavior can be controlled by ----lloogg--ffiillee, ----ssyysslloogg  and  ----nnoo--ssttdd--
       oouutt--lloogg _o_p_t_i_o_n_s.

       =================================

HHTTTTPPSS MMAANNAAGGEEMMEENNTT IINNTTEERRFFAACCEE
       The  _t_u_r_n_s_e_r_v_e_r  process provides an HTTPS Web access as statistics and
       basic management interface. The _t_u_r_n_s_e_r_v_e_r listens  to  incoming  HTTPS
       admin connections on the same ports as the main TURN/STUN listener. The
       Web admin pages are basic and self-explanatory.

       To make the HTTPS interface active, the database table admin_user  must
       be  populated  with  the  admin user aaccccoouunntt(s). An admin user can be a
       superuser (if not assigned to a particular realm) or a restricted  user
       (if  assigned  to a realm). The restricted admin users can perform only
       limited actions, within their corresponding realms.

       =================================

TTEELLNNEETT CCLLII
       The _t_u_r_n_s_e_r_v_e_r process provides a telnet CLI access as  statistics  and
       basic  management interface. By default, the _t_u_r_n_s_e_r_v_e_r starts a telnet
       CLI listener on IP 127.0.0.1 and port 5766. That can be changed by  the
       command-cline  _o_p_t_i_o_n_s  of  the  _t_u_r_n_s_e_r_v_e_r  process  (see ----ccllii--iipp and
       ----ccllii--ppoorrtt _o_p_t_i_o_n_s). The full list of telnet CLI commands  is  provided
       in "help" command output in the telnet CLI.

       =================================

CCLLUUSSTTEERRSS
       TTUURRNN  SSeerrvveerr can be a part of the cluster installation. But, to support
       the "even port"  functionality  (RTP/RTCP  streams  pairs)  the  client
       requests from a particular IP must be delivered to the same TTUURRNN SSeerrvveerr
       instance, so it requires some networking setup massaging for the  clus-
       ter.  The  reason  is  that the RTP and RTCP relaying endpoints must be
       allocated on the same relay IP. It would be possible to design a scheme
       with  the  application-level  requests  forwarding  (and we may do that
       later) but it would affect the performance.

       =================================

FFIILLEESS
       /etc/turnserver.conf

       /var/db/turndb

       /usr/local/var/db/turndb

       /var/lib/turn/turndb

       /usr/local/etc/turnserver.conf

       =================================

DDIIRREECCTTOORRIIEESS
       /usr/local/share/_t_u_r_n_s_e_r_v_e_r

       /usr/local/share/doc/_t_u_r_n_s_e_r_v_e_r

       /usr/local/share/examples/_t_u_r_n_s_e_r_v_e_r

       =================================

SSTTAANNDDAARRDDSS
       obsolete STUN RFC 3489

       new STUN RFC 5389

       TURN RFC 5766

       TURN-TCP extension RFC 6062

       TURN IPv6 extension RFC 6156

       STUN/TURN test vectors RFC 5769

       STUN NAT behavior discovery RFC 5780

       =================================

SSEEEE AALLSSOO
       _t_u_r_n_a_d_m_i_n, _t_u_r_n_u_t_i_l_s

       ======================================

   WWEEBB RREESSOOUURRCCEESS
       project page:

       https://github.com/coturn/coturn/

       Wiki page:

       https://github.com/coturn/coturn/wiki

       forum:

       https://groups.google.com/forum/?from-
       groups=#!forum/turn-server-project-rfc5766-turn-server

       ======================================

   AAUUTTHHOORRSS
       Oleg Moskalenko <mom040267@gmail.com>

       Gabor Kovesdan http://kovesdan.org/

       Daniel Pocock http://danielpocock.com/

       John Selbie (jselbie@gmail.com)

       Lee Sylvester <lee@designrealm.co.uk>

       Erik Johnston <erikj@openmarket.com>

       Roman Lisagor <roman@demonware.net>

       Vladimir Tsanev <tsachev@gmail.com>

       Po-sheng Lin <personlin118@gmail.com>

       Peter Dunkley <peter.dunkley@acision.com>

       Mutsutoshi Yoshimoto <mutsutoshi.yoshimoto@mixi.co.jp>

       Federico Pinna <fpinna@vivocha.com>

       Bradley T. Hughes <bradleythughes@fastmail.fm>



                               01 September 2015                       TURN(1)
