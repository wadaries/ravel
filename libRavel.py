# new_add_flow_fun = """
# CREATE OR REPLACE FUNCTION add_flow_fun ()
# RETURNS TRIGGER
# AS $$
# f = TD["new"]["pid"]
# s = TD["new"]["sid"]
# n = TD["new"]["nid"]

# u = plpy.execute("select port from get_port (" +str (s)+") where nid = " +str (n))
# outport = str(u[0]['port'])
# v = plpy.execute("select port from get_port (" +str (s)+") where nid = " +str (f))
# inport = str (v[0]['port'])

# cmd1 = '/usr/bin/sudo /usr/bin/ovs-ofctl add-flow s' + str (s) + ' in_port=' + inport + ',actions=output:' + outport
# cmd2 = '/usr/bin/sudo /usr/bin/ovs-ofctl add-flow s' + str (s) + ' in_port=' + outport + ',actions=output:' + inport

# fo = open ('/home/mininet/ravel/log.txt', 'a')
# def logfunc(msg,f=fo):
#     f.write(msg+'\n')

# logfunc ('addflow')
# logfunc ('addflow')

# fo.flush ()

# return None;
# $$ LANGUAGE 'plpythonu' VOLATILE SECURITY DEFINER;
# """

# new_del_flow_fun = """ 
# CREATE OR REPLACE FUNCTION del_flow_fun ()
# RETURNS TRIGGER
# AS $$
# f = TD["old"]["pid"]
# s = TD["old"]["sid"]
# n = TD["old"]["nid"]

# u = plpy.execute("select port from get_port (" +str (s)+") where nid = " +str (n))
# outport = str(u[0]['port'])

# v = plpy.execute("select port from get_port (" +str (s)+") where nid = " +str (f))
# inport = str (v[0]['port'])

# cmd1 = '/usr/bin/sudo /usr/bin/ovs-ofctl del-flows s' + str (s) + ' in_port=' + inport
# cmd2 = '/usr/bin/sudo /usr/bin/ovs-ofctl del-flows s' + str (s) + ' in_port=' + outport

# fo = open ('/home/mininet/ravel/log.txt', 'a')
# def logfunc(msg,f=fo):
#     f.write(msg+'\n')

# logfunc ('delflow')

# logfunc ('delflow')

# fo.flush ()

# return None;
# $$ LANGUAGE 'plpythonu' VOLATILE SECURITY DEFINER;
# """

def select_dbname ():
    global monitor_mininet
    global switch_size
    global fanout_size
    global k_size

    while True:
        n = raw_input ('select topology type : \n \t\'t,\'y\'/\'n\'\'(toy w/o mininet monitor) \n \t\'i,/y/n\'(isp w/o mininet monitor) \n\t\'m,\'y\'/\'n\'\'(mininet) \n\t\'tree\',switch_size,fanout_size,\'y\'/\'n\' (tree w/o mininet monitor) \n\t\'f\',k_size (fat tree with k)\n')
        if n.strip ().split (',')[0] == 't':
            monitor_mininet = n.strip ().split (',')[1]
            return 'toy'
            break
        elif n.strip ().split (',')[0] == 'i':
            monitor_mininet = n.strip ().split (',')[1]
            return 'isp'
            break
        elif n.strip ().split (',')[0] == 'm':
            return 'mininet'
            break
        elif n.strip ().split (',')[0] == 'tree':
            switch_size = int (n.strip ().split (',')[1]) 
            fanout_size = int (n.strip ().split (',')[2])
            monitor_mininet = n.strip ().split (',')[3]
            return 'tree'
            break
        elif n.strip ().split (',')[0] == 'f':
            k_size = int (n.strip ().split (',')[1])
            return 'fattree'
            break
        else:
            print 'wrong topology type'


def create_mininet_topo (dbname, username):
    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute ("SELECT * FROM switches;")
        cs = cur.fetchall ()
        switches = [s['sid'] for s in cs]

        # cur.execute ("SELECT * FROM hosts;")
        # cs = cur.fetchall ()
        # hosts = [h['hid'] for h in cs]

        cur.execute ("SELECT * FROM tp;")
        cs = cur.fetchall ()
        links = [[l['sid'],l['nid']] for l in cs]

        cur.execute ("SELECT * FROM uhosts;")
        cs = cur.fetchall ()
        hids = [h['hid'] for h in cs]
        u_hids = [h['u_hid'] for h in cs]
        host_dict = dict (zip (hids, u_hids))

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
    finally:
        if conn: conn.close()

    def nid_name (nid, s, h):
        if nid in s:
            outid = 's' + str (nid)
        elif nid in h.keys ():
            outid = 'h' + str (h[nid])
        else:
            print "nid_name wrong"
        return outid

    timestamp = str (datetime.datetime.now ()) .replace(" ", "-").replace (":","-").replace (".","-")
    # timestamp = ""
    filename = os.getcwd () + '/topo/'+ dbname + '_dtp.py'
    fo = open(filename, "w")
    fo.write ('"""' + timestamp)
    fo.write ('\n$ sudo mn --custom '+ filename + ' --topo mytopo --test pingall')
    fo.write ('\n$ sudo mn --custom '+ filename + ' --topo mytopo --mac --switch ovsk --controller remote\n')
    fo.write ('"""')

    fo.write ('\n')
    fo.write ("""
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
    """)

    for hid in host_dict.keys ():
        h = 'h' + str (host_dict [hid])
        fo.write ("""
        """ + h + """ = self.addHost('""" + h + """')""")
    fo.write ('\n')

    for sid in switches:
        s = 's' + str (sid)
        fo.write ("""
        """ + s + """ = self.addSwitch('""" + s + """')""")
    fo.write ('\n')
        
    for [nid1, nid2] in links:
        nname1 = nid_name (nid1, switches, host_dict)
        nname2 = nid_name (nid2, switches, host_dict)
        fo.write ("""
        self.addLink(""" + nname1 + "," + nname2+ """)""")

    fo.write ("""\n
topos = { 'mytopo': ( lambda: MyTopo() ) }
    """)
    fo.write ('\n')
    fo.close ()
    print "--------------------> create_mininet_topo successful"


def clean_db (dbname):
    try:
        conn = psycopg2.connect(database= "postgres", user= "mininet")
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()

        cur.execute ("drop database " + dbname)
        print "--------------------> clean_db successful"

    except psycopg2.DatabaseError, e:
        print "clean_db error"
        print 'Error %s' % e    

    finally:
        if conn: conn.close()

def create_db (dbname):
    try:
        conn = psycopg2.connect(database= 'postgres', user= 'mininet')
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()

        cur.execute ("SELECT datname FROM pg_database WHERE datistemplate = false;")
        c = cur.fetchall ()
        dblist = [c[i][0] for i in range (len (c))]
        if dbname not in dblist:
            cur.execute ("CREATE DATABASE " + dbname + ";")
        else:
            print "database " + dbname + " exists, skip"

        print "--------------------> create_db successful"
    except psycopg2.DatabaseError, e:
        print "create_db: unable to connect to database postgres, as user " + 'mininet'
        print 'Error %s' % e

    finally:
        if conn:
            conn.close()

def add_pgrouting_plpy_plsh_extension (dbname, username):

    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()

        cur.execute ("SELECT 1 FROM pg_catalog.pg_namespace n JOIN pg_catalog.pg_proc p ON pronamespace = n.oid WHERE proname = 'pgr_dijkstra';")
        c = cur.fetchall ()
        if c == []:
            cur.execute ("CREATE EXTENSION IF NOT EXISTS plpythonu;")
            cur.execute ("CREATE EXTENSION IF NOT EXISTS postgis;")
            cur.execute ("CREATE EXTENSION IF NOT EXISTS pgrouting;")
            cur.execute ("CREATE EXTENSION plsh;")

        print "--------------------> add_pgrouting_plpy_plsh_extension successful"
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn: conn.close()

def load_database (dbname, username):
    # print monitor_mininet, "before"
    def print_mn_manual (dbname):
        # print message, exit loop after user inputs 'y'
        filename = os.getcwd () + '/topo/'+ dbname + '_dtp.py'
        while True:
            cmd = 'please run (press y to not repeat the message)\n' + 'sudo mn --custom '+ filename + ' --topo mytopo --mac --switch ovsk --controller remote\n'
            n = raw_input(cmd)
            if n.strip () == 'y':
                break

    if dbname == 'toy' or dbname == 't':
        # load_topo3switch ('toy', username)
        load_topo3switch_new ('toy', username)
    elif dbname == 'isp' or dbname == 'i':
        load_ISP_topo_fewer_hosts ('isp', username)
    elif dbname == 'mininet' or dbname == 'm':
        load_topo3switch_new ('mininet', username)
    elif dbname == 'tree':
        load_tree (switch_size, fanout_size, dbname, username)
    elif dbname == 'fattree':
        load_fattree (k_size, dbname, username)

    create_mininet_topo (dbname, username)

    if monitor_mininet == 'y':
        print_mn_manual (dbname)
        load_pox_module (dbname, username)



def igraph_fattree (k):
    core_size = (k/2)**2
    agg_size = (k/2) *k
    eg_size = (k/2) *k
    host_size = (k/2)**2 *k

    # g = Graph(directed = True)    
    g = Graph()    

    g.add_vertices (core_size + agg_size + eg_size + host_size)
    g.vs['type'] = ['core'] * core_size + ['agg'] * agg_size + ['edge'] * eg_size + ['host'] * host_size

    for pod in range (0,k):
        agg_offset = core_size + k/2 * pod
        eg_offset = core_size + agg_size + k/2*pod
        host_offset = core_size + agg_size + eg_size + (k/2)**2 * pod

        for agg in range (0, k/2):
            core_offset = agg * k/2

            for core in range (0, k/2):
                g.add_edge (agg_offset + agg, core_offset + core)
                # connect core and aggregate routers

            for eg in range (0, k/2):
                g.add_edge (agg_offset + agg, eg_offset + eg)
                # connect aggregate and edge routers

        for eg in range (0, k/2):
            for h in range (0, k/2):
                g.add_edge (eg_offset + eg, host_offset + k/2*eg + h)
                # connect edge routers and hosts
    return g

def load_fattree (k, dbname, username):
    g = igraph_fattree (k)

    edges = g.get_edgelist ()

    conn = psycopg2.connect(database= dbname, user= username)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
    cur = conn.cursor()

    global switch_size
    switch_size = (k/2)**2 + (k/2) *k + (k/2) *k

    for i in range (switch_size):
        cur.execute ("insert into switches (sid) values (" +str (i) +")")

    for i in range (switch_size, switch_size + (k/2)**2 *k):
        cur.execute ("insert into hosts (hid) values (" + str (i) + ")")
        # cur.execute ("insert into tp (sid, nid, ishost,isactive) values (" + str (i) +','+ str (i+switch_size) + ", 1,1)")

    for e in edges:
        cur.execute ('insert into tp (sid, nid, isactive) values (' + str (e[0]) + ',' + str (e[1]) + ',1);' )

    conn.close ()
    print "--------------------> load_fattree successful"
    
def load_tree (switch_size, fanout_size, dbname, username):
    g = Graph.Tree(switch_size, fanout_size)
    edges = g.get_edgelist ()

    conn = psycopg2.connect(database= dbname, user= username)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
    cur = conn.cursor()

    for i in range (switch_size):
        cur.execute ("insert into switches (sid) values (" +str (i) +")")

        if g.degree (i) == 1:
            cur.execute ("insert into hosts (hid) values (" + str (i + switch_size) + ")")
            cur.execute ("insert into tp (sid, nid, ishost,isactive) values (" + str (i) +','+ str (i+switch_size) + ", 1,1)")

    for e in edges:
        cur.execute ('insert into tp (sid, nid, ishost, isactive) values (' + str (e[0]) + ',' + str (e[1]) + ',0,1);' )

    conn.close ()
    print "--------------------> load_tree successful"


def load_ISP_topo_fewer_hosts (dbname, username):
    def init_topology (cursor):
        ISP_edges_file = os.getcwd () + '/ISP_topo/4755_edges.txt'
        ISP_nodes_file = os.getcwd () + '/ISP_topo/4755_nodes.txt'

        f = open (ISP_edges_file, "r").readlines ()# [:10]

        for edge in f:
            ed = edge[:-1].split()
            try:
                cursor.execute("""INSERT INTO tp(sid, nid, isactive) VALUES (%s, %s,1);""", (int(ed[0]), int(ed[1])))
            except psycopg2.DatabaseError, e:
                print "Unable to insert into topology table: %s" % str(e)

        f = open (ISP_nodes_file, "r").readlines ()
        for node in f:
            nd = node[:-1]
            try:
                cursor.execute ("""INSERT INTO switches VALUES (%s);""", ([int (nd)]))
            except psycopg2.DatabaseError, e:
                print "Unable to insert into switches table: %s" % str(e)

        f = ['60\n','34\n','112\n','141\n','193\n','238\n','28\n','89\n','91\n','253\n','472\n']
        for node in f:
            nd = node[:-1]
            try:
                cursor.execute ("""INSERT INTO hosts VALUES (%s);""", ([int (nd)+1000]))
                cursor.execute ("""INSERT INTO tp(sid, nid, isactive) VALUES (%s, %s,1);""",(int(nd)+1000,int(nd)))
            except psycopg2.DatabaseError, e:
                print "Unable to insert into hosts table: %s" % str(e)
        print "Initialize topology table with edges in " + ISP_edges_file

    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()
        init_topology (cur)

        print "--------------------> load_ISP_topo_fewer_hosts successful"

    except psycopg2.DatabaseError, e:
        print "Unable to connect to database " + dbname + ", as user " + username
        print 'Error %s' % e    

    finally:
        if conn: conn.close()    

def load_topo3switch_new (dbname, username):
    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()
        cur.execute ("""
        TRUNCATE TABLE tp cascade;
        TRUNCATE TABLE cf cascade;
        TRUNCATE TABLE tm cascade;
        INSERT INTO switches(sid) VALUES (1),(2),(3);
        INSERT INTO hosts(hid) VALUES (4),(5),(6);
        INSERT INTO tp(sid, nid, ishost, isactive) VALUES (1,4,1,1), (2,5,1,1), (3,6,1,1);
        INSERT INTO tp(sid, nid, ishost, isactive) VALUES (1,2,0,1), (2,3,0,1), (3,1,0,1);
""")
        print "--------------------> load_topo3switch successful"
    except psycopg2.DatabaseError, e:
        print "Unable to connect to database " + dbname + ", as user " + username
        print 'Error %s' % e

    finally:
        if conn: conn.close()

def load_topo3switch (dbname, username):
    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()
        cur.execute ("""
        TRUNCATE TABLE tp cascade;
        TRUNCATE TABLE cf cascade;
        TRUNCATE TABLE tm cascade;
        INSERT INTO switches(sid) VALUES (4),(5),(6);
        INSERT INTO hosts(hid) VALUES (1),(2),(3);
        INSERT INTO tp(sid, nid) VALUES (1,4), (2,5), (3,6);
        INSERT INTO tp(sid, nid) VALUES (4,5), (5,6), (6,4);
""")

        print "--------------------> load_topo3switch successful"
    except psycopg2.DatabaseError, e:
        print "Unable to connect to database " + dbname + ", as user " + username
        print 'Error %s' % e    

    finally:
        if conn: conn.close()

def load_schema (dbname, username, sql_script):
    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()

        dbscript  = open (sql_script,'r').read()
        cur.execute(dbscript)

        print "--------------------> load_schema successful"
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn: conn.close()

def batch_test (dbname, username, rounds, flag):
    conn = psycopg2.connect(database= dbname, user= username)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute ("SELECT * FROM hosts;")
    cs = cur.fetchall ()
    hosts = [h['hid'] for h in cs]
    # print hosts

    if dbname == 'fattree':
        logdestfile = dbname + str (k_size) + '_' + flag + '_' + str (rounds)

    logfile = os.getcwd ()+'/log.txt'

    open(logfile, 'w').close()
    f = open(logfile, 'a')
    f.write ("--------------------> " + flag + ' with rounds ' + str (rounds) + '\n')
    f.write ("--------------------> batch_test begins\n\n")
    f.flush ()

    def routing_one_round (cur=cur, hosts=hosts, f=f):
        indices = random.sample(range(len(hosts)), 2)
        [h1,h2] = [hosts[i] for i in sorted(indices)]

        t1 = time.time ()
        cur.execute ("INSERT INTO tm values (1,%s,%s,1);",([int (h1),int (h2)]))
        t2 = time.time ()
        f.write ("INSERT INTO tm values (1," + str (h1) + "," + str (h2)+",1)(ms):" + str ((t2-t1)*1000) + '\n')
        f.flush ()

        t1 = time.time ()
        cur.execute ("DELETE FROM tm WHERE fid = 1;")
        t2 = time.time ()
        f.write ("DELETE FROM tm WHERE fid = 1(ms):" + str ((t2-t1)*1000) + '\n')
        f.flush ()

    if flag == 'routing':

        for i in range (0,rounds):
            print "round " + str (i)
            f.write ("round " + str (i) + '\n')
            f.flush ()
            routing_one_round ()
            f.write ('\n')

    f.write ("--------------------> batch_test ends\n")
    f.close ()
    logdest = os.getcwd () + '/data/' + logdestfile + '.log'
    # logdest = os.getcwd () + '/data/log_' + str (datetime.datetime.now ()) .replace(" ", "-").replace (":","-").replace (".","-")
    os.system ("cp "+ logfile + ' ' + logdest)

    print "--------------------> batch_test successful"
    conn.close()

def load_pox_module (dbname,username):
    cmd = "/home/mininet/pox/pox.py pox.openflow.discovery pox.samples.pretty_log pox.host_tracker db --dbname=" + str (dbname) + " --username=" + str (username)
    # cmd = "/home/mininet/pox/pox.py pox.openflow.discovery pox.samples.pretty_log pox.forwarding.l3_learning pox.host_tracker db"
    os.system (cmd + " &")
    print "--------------------> load_pox_module successful: Fan's db.py running in the background"

def kill_pox_module ():
    cmd = "pkill -f '/home/mininet/pox/pox.py pox.openflow.discovery pox.samples.pretty_log pox.host_tracker db'"
    # cmd = "pkill -f '/home/mininet/pox/pox.py pox.openflow.discovery pox.samples.pretty_log pox.forwarding.l3_learning pox.host_tracker db'"
    os.system (cmd)
    print "--------------------> kill pox module that populates mininet events to database"


def create_tenant (dbname, username):
    conn = psycopg2.connect(database= dbname, user= username)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute ("SELECT * FROM uhosts;")
    cs = cur.fetchall ()
    hosts = [int (s['u_hid']) for s in cs]

    # cur.execute ("SELECT count(*) FROM switches;")
    # cs = cur.fetchall ()
    # ct = int (cs[0][0]) 
    n = raw_input("select tenant size (1 - " + str (len (hosts) -1) + "): ")
    selected_hosts = [ hosts[i] for i in random.sample(xrange(len(hosts)), int (n)) ]
    print selected_hosts

    cur.execute (""" 

DROP TABLE IF EXISTS tenant_hosts CASCADE;
CREATE UNLOGGED TABLE tenant_hosts (
       hid	integer,
       PRIMARY key (hid)
);

CREATE OR REPLACE VIEW tenant_policy AS (
       SELECT DISTINCT host1, host2 FROM utm
       WHERE host1 IN (SELECT * FROM tenant_hosts)
       	     AND host2 IN (SELECT * FROM tenant_hosts)
);

CREATE OR REPLACE FUNCTION tenant_policy_ins_fun() RETURNS TRIGGER AS
$$
plpy.notice ("tenant_policy_ins_fun")

h1 = TD["new"]["host1"]
h2 = TD["new"]["host2"]

hs = plpy.execute ("SELECT hid FROM tenant_hosts;")
hosts = [h['hid'] for h in hs]

if (h1 in hosts) & (h2 in hosts):
   plpy.execute ("INSERT INTO utm values ((select max (counts) +1 from clock), " +str (h1)+ "," + str (h2) + ");")

return None;
$$
LANGUAGE 'plpythonu' VOLATILE SECURITY DEFINER;

CREATE TRIGGER tenant_policy_ins_trigger
     INSTEAD OF INSERT ON tenant_policy
     FOR EACH ROW
   EXECUTE PROCEDURE tenant_policy_ins_fun();

CREATE OR REPLACE RULE tenant_policy_del AS
       ON DELETE TO tenant_policy
       DO INSTEAD
       DELETE FROM utm WHERE host1 = OLD.host1 AND host2 = OLD.host2;

""")

    for h in selected_hosts:
        cur.execute ("insert into tenant_hosts values (" + str (h) + ");")

    print '--------------------> create tenant, interact with \'tenant_hosts\' and \'tenant_policy\''

    conn.close()

def perform_test (dbname, username):
    
    while True:
        n = raw_input("select test actions: \n\t'e'(exit) \n\t'b'(batch test) \n\t't'(dc tenant)\n")
        if n.strip() == 'e':
            t = raw_input("clean database? ('y'/'n'): ")
            if t.strip () == 'y':
                kill_pox_module ()
                clean_db (dbname)
                break
            elif t.strip () == 'n':
                kill_pox_module ()
                break
        elif n.strip () == 'b':
            print 'start batch_test ()'
            print 'flag = routing'
            batch_test (dbname, username, 10, flag='routing')

        elif n.strip () == 't':
            print 'play with dc tenant'
            create_tenant (dbname, username)
