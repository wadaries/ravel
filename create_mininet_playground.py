import sys
import time
import random
import os
import psycopg2
import psycopg2.extras
import subprocess
import datetime

def create_mininet_topo (dbname, username):
    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute ("SELECT * FROM switches;")
        cs = cur.fetchall ()
        switches = [s['sid'] for s in cs]
        # print switches

        cur.execute ("SELECT * FROM hosts;")
        cs = cur.fetchall ()
        hosts = [h['hid'] for h in cs]
        # print hosts

        cur.execute ("SELECT * FROM tp;")
        cs = cur.fetchall ()
        links = [[l['sid'],l['nid']] for l in cs]
        # print links

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
    finally:
        if conn: conn.close()

    def nid_name (nid, s, h):
        if nid in s:
            outid = 's' + str (nid)
        if nid in h:
            outid = 'h' + str (nid)
        return outid

    timestamp = str (datetime.datetime.now ()) .replace(" ", "-").replace (":","-").replace (".","-")
    # timestamp = ""
    filename = os.getcwd () + '/dtp.py'
    fo = open(filename, "w")
    fo.write ('"""' + timestamp)
    fo.write ('\n$ sudo mn --custom ~/ravel/dtp.py --topo mytopo --test pingall')
    fo.write ('\n$ sudo mn --custom ~/ravel/dtp.py --topo mytopo --mac --switch ovsk --controller remote\n')
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

    for hid in hosts:
        h = 'h' + str (hid)
        fo.write ("""
        """ + h + """ = self.addHost('""" + h + """')""")
    fo.write ('\n')

    for sid in switches:
        s = 's' + str (sid)
        fo.write ("""
        """ + s + """ = self.addSwitch('""" + s + """')""")
    fo.write ('\n')
        
    for [nid1, nid2] in links:
        nname1 = nid_name (nid1, switches, hosts)
        nname2 = nid_name (nid2, switches, hosts)
        fo.write ("""
        self.addLink(""" + nname1 + "," + nname2+ """)""")

    fo.write ("""\n
topos = { 'mytopo': ( lambda: MyTopo() ) }
    """)
    fo.write ('\n')
    fo.close ()
    print "-------------------->create_mininet_topo successful"


def clean_db (dbname):
    try:
        conn = psycopg2.connect(database= "postgres", user= "mininet")
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()

        cur.execute ("drop database " + dbname)
        print "clean_db successful"

    except psycopg2.DatabaseError, e:
        print "Unable to connect to database " + dbname 
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

        print "-------------------->create_db successful"
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

        print "-------------------->add_pgrouting_plpy_plsh_extension successful"
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn: conn.close()

def load_ISP_topo_fewer_hosts (dbname, username):
    def init_topology (cursor):
        ISP_edges_file = os.getcwd () + '/ISP_topo/4755_edges.txt'
        ISP_nodes_file = os.getcwd () + '/ISP_topo/4755_nodes.txt'

        f = open (ISP_edges_file, "r").readlines ()# [:10]

        for edge in f:
            ed = edge[:-1].split()
            try:
                cursor.execute("""INSERT INTO tp(sid, nid) VALUES (%s, %s);""", (int(ed[0]), int(ed[1])))
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
                cursor.execute ("""INSERT INTO tp(sid, nid) VALUES (%s, %s);""",(int(nd)+1000,int(nd)))
            except psycopg2.DatabaseError, e:
                print "Unable to insert into hosts table: %s" % str(e)
        print "Initialize topology table with edges in " + ISP_edges_file + "\n"

    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor()
        init_topology (cur)

        print "-------------------->load_ISP_topo_fewer_hosts successful"

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

        print "-------------------->load_topo3switch successful"
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

        print "-------------------->load_schema successful"
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn: conn.close()

def batch_test (dbname, username):
    try:
        conn = psycopg2.connect(database= dbname, user= username)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute ("SELECT * FROM hosts;")
        cs = cur.fetchall ()
        hosts = [h['hid'] for h in cs]
        # print hosts

        logfile = os.getcwd ()+'/log.txt'
        open(logfile, 'w').close()
        f = open(logfile, 'a')
        f.write ("-------------------->batch_test begins\n")
        f.flush ()

        def one_round (cur=cur, hosts=hosts, f=f):
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
            # logfunc ('add-flow s' + str (s) + '(ms): ' + str ((t2-t1)*1000))
            # cursor.execute ("""INSERT INTO switches VALUES (%s);""", ([int (nd)]))

        one_round ()

        f.write ("-------------------->batch_test ends\n")
        f.close ()
        logdest = os.getcwd () + '/data/log_' + str (datetime.datetime.now ()) .replace(" ", "-").replace (":","-").replace (".","-")
        os.system ("cp "+ logfile + ' ' + logdest)
        
        print "-------------------->batch_test successful"
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn: conn.close()

if __name__ == '__main__':

    dbname = raw_input ('Input database name: ')
    username = 'mininet'
    sql_script = "/home/mininet/ravel/mininet_playground.sql"

    create_db (dbname)

    add_pgrouting_plpy_plsh_extension (dbname, username)

    load_schema (dbname, username, sql_script)

    topo_flag = raw_input ('Topology options (isp/toy): ')
    if topo_flag == 'toy':
        load_topo3switch (dbname, username)
    elif topo_flag == 'isp':
        load_ISP_topo_fewer_hosts (dbname, username)
    else:
        print 'wrong topology type\n'

    if (topo_flag == 'toy' or topo_flag == 'isp'):
        create_mininet_topo (dbname, username)

    batch_test (dbname, username)

    del_flag = raw_input ('Clean the added database (y/n): ')
    if del_flag == 'y':
        clean_db (dbname)
