from __future__ import division
import os

gnuplot_script = '''
reset

set termoption dash

set style line 80 lt -1 lc rgb "#808080"
set style line 81 lt 0  # dashed
set style line 81 lt rgb "#808080"
set grid back linestyle 81
set border 3 back linestyle 80

set style line 1 lt rgb "#A00000" lw 1 pt 1 ps 1
set style line 2 lt rgb "#00A000" lw 1 pt 6 ps 1
set style line 3 lt rgb "#5060D0" lw 1 pt 2 ps 1
set style line 4 lt rgb "#F25900" lw 1 pt 9 ps 1

set style line 11 lt -1 lc rgb "#A00000" lw 3 
set style line 12 lt -1 lc rgb "#00A000" lw 3
set style line 13 lt -1 lc rgb "#5060D0" lw 3
set style line 14 lt 1 lc rgb "#F25900" lw 3

set key top left

set xtics nomirror
set ytics nomirror'''

def get_k (logfile):
    t = logfile.split ('/')[-1] # .split ('.').split ('_')
    t2 = str (t.split ('_')[0][7:]) 
    return t2

def parse_log (logfile, keytext):

    s = []

    f = open(logfile, "r")
    for l in f.readlines():
        if l[0] == '#':
            pass
        else: 
            e = l.split ('----')
            if e[1] == keytext:
                if len (e[0]) != 0:
                    # s.append ([e[1], len (e[0]), float (e[2][:-1])/len (e[0])])
                    s.append (float (e[2][:-1])/len (e[0]))
                elif len (e[0]) == 0:
                    # s.append ([e[1], 0, float (e[2][:-1])])
                    s.append (float (e[2][:-1]))
    return s

def gen_dat (topo, logfile, keytext, dir_name):

    xlabel = keytext
    nametext = xlabel.replace (' ', '_').replace (':', '').replace ('(','_').replace (')','_').replace ('+','_').replace ('*','_')

    # pltfile = os.getcwd () + '/' + topo + '/' + nametext + '.plt'
    # pdffile = os.getcwd () + '/' + topo + '/pdf/' + nametext + '.pdf'
    datfile = dir_name + nametext + '.dat'

    # print logfile[0]
    o0 = sorted (parse_log (logfile[0], keytext))
    # print o0
    o1 = sorted (parse_log (logfile[1], keytext)) 
    o2 = sorted (parse_log (logfile[2], keytext))

    l0 = len (o0)
    l1 = len (o1)
    l2 = len (o2)
    l = max ([l0,l1,l2])

    def t_o (i, li, o):
        if i < li:
            return o[i]
        else:
            return o[li-1]

    f = open (datfile, "wr")
    # print 'datfile: ' + datfile
    # print 'len is: ' + str (len (o0))
    
    for i in range (0,l):
        line = str ((i+1)/l0) + '\t' + str (t_o (i, l0, o0) ) + '\t' + str ((i+1)/l1)+'\t' + str (t_o (i, l1, o1)) + '\t' +str ((i+1)/l2)+'\t' + str (t_o (i, l2, o2)) + '\n'
        f.write (line)
        f.flush ()
    f.close ()

#     for k in keytext2:
#         print "plot " + k
#         plot ('tenant', log4, k)

class rPlot ():

    tenantlist = ['rt*tenant: route ins', 'lb*tenant: check max load', '(lb+rt)*tenant: re-balance', 'lb*tenant: re-balance', 'acl*tenant: check violation', 'acl*tenant: fix violation', 'acl+rt*tenant: fix violation', '(acl+lb+rt)*tenant: route ins']

    key_tenant = tenantlist
    
    def __init__ (self, loglist, keylist):
        self.log_file_list = loglist
        self.key_list = keylist
        self.sub_dir = '/media/sf_share/ravel_plot/'
        self.dat_dir = '/media/sf_share/ravel_plot/'
        self.plt_dir = '/media/sf_share/ravel_plot/'
        self.pdf_dir = '/media/sf_share/ravel_plot/'

    def add_log (self,filename):
        self.log_file_list.append (self.sub_dir + filename)

    def add_key (self,key):
        self.key_list.append (key)

    def parse_log (self):
        s = parse_log (self.log_file_list[0], self.key_list[0])
        return s

    def gen_dat (self):
        for key in self.key_list:
            gen_dat ('primitive', self.log_file_list, key, self.dat_dir)

class rPlot_primitive (rPlot):

    def __init__ (self, subdir):

        lblist = ['lb: check max load', 'lb: re-balance (absolute)', 'lb+rt: re-balance (absolute)', 'lb+rt: re-balance (per rule)']
        acllist = ['acl: check violation', 'acl: fix violation', 'acl+rt: fix violation (absolute)', 'acl+rt: fix violation (per rule)']
        rtlist = ['rt: route ins']
        link = ['rt: linkdown', 'rt: linkup']
        acllbrt = ['acl+lb+rt: route ins']

        key_primitive = lblist + acllist + link + acllbrt + rtlist

        rPlot.__init__ (self, [], key_primitive)
        self.dat_dir += subdir + '/dat/'
        self.sub_dir += subdir + '/'

class rPlot_tenant (rPlot):
    def __init__ (self):

        rPlot.__init__ (rPlot.key_tenant)



#     pf = open(pltfile, "wr")
#     pf.write (gnuplot_script)
#     pf.write ('''
# # set ylabel "CDF"
# # set xlabel "Per-update overhead (ms)"
# # set title "''' +keytext+ '''"
# set xlabel "''' +xlabel+ '''"
# set yrange [0:1]

# set output "''' + pdffile + '''"
# set terminal pdfcairo size 2,2 font "Gill Sans,9" linewidth 2 rounded fontscale 1 
# # default 5 by 3 (inches)

# set logscale x
# plot "'''+ nametext +'''.dat" using 2:1 title "k='''+ get_k (logfile[0])+'''" with lp ls 11,\
#  '' using 4:3 title "k='''+get_k (logfile[1])+ '''" with lp ls 12,\
#  '' using 6:5 title "k='''+get_k (logfile[2])+ '''" with lp ls 13
# ''')

#     pf.flush ()
#     pf.close ()