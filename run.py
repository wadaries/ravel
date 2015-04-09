import sys
import time
import random
import os
import psycopg2
import psycopg2.extras
import subprocess
import datetime
from igraph import *

execfile("libRavel.py")
import libRavel

username = 'mininet'
sql_script1 = "/home/mininet/ravel/sql_scripts/base_and_routing.sql"
sql_script2 = "/home/mininet/ravel/sql_scripts/obs_app.sql"

def procedure ():

    dbname = get_dbname ()

    create_db (dbname)

    add_pgrouting_plpy_plsh_extension (dbname, username)

    load_schema (dbname, username, sql_script1)
    load_schema (dbname, username, sql_script2)

    load_database (dbname, username)

    create_mininet_topo (dbname, username)

    launch_mn_manual (dbname)

    while True:
        n = raw_input("Pick actions: 'e'(exit) / 'b'(batch test)")
        if n.strip() == 'e':
            t = raw_input("clean database? 'y'/'n'")
            if t.strip () == 'y':
                kill_pox_module ()
                clean_db (dbname)
                break
            elif t.strip () == 'n':
                kill_pox_module ()
                break
        elif n.strip () == 'b':
            print 'start batch_test ()'
            batch_test (dbname, username, 10, topo_flag=dbname)

if __name__ == '__main__':
    # load_database ("f", "random")
    procedure ()


