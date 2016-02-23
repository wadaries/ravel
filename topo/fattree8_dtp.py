"""2015-08-31-17-19-47-938274
$ sudo mn --custom /home/mininet/ravel/topo/fattree8_dtp.py --topo mytopo --test pingall
$ sudo mn --custom /home/mininet/ravel/topo/fattree8_dtp.py --topo mytopo --mac --switch ovsk --controller remote
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
    
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')
        h17 = self.addHost('h17')
        h18 = self.addHost('h18')
        h19 = self.addHost('h19')
        h20 = self.addHost('h20')
        h21 = self.addHost('h21')
        h22 = self.addHost('h22')
        h23 = self.addHost('h23')
        h24 = self.addHost('h24')
        h25 = self.addHost('h25')
        h26 = self.addHost('h26')
        h27 = self.addHost('h27')
        h28 = self.addHost('h28')
        h29 = self.addHost('h29')
        h30 = self.addHost('h30')
        h31 = self.addHost('h31')
        h32 = self.addHost('h32')
        h33 = self.addHost('h33')
        h34 = self.addHost('h34')
        h35 = self.addHost('h35')
        h36 = self.addHost('h36')
        h37 = self.addHost('h37')
        h38 = self.addHost('h38')
        h39 = self.addHost('h39')
        h40 = self.addHost('h40')
        h41 = self.addHost('h41')
        h42 = self.addHost('h42')
        h43 = self.addHost('h43')
        h44 = self.addHost('h44')
        h45 = self.addHost('h45')
        h46 = self.addHost('h46')
        h47 = self.addHost('h47')
        h48 = self.addHost('h48')
        h49 = self.addHost('h49')
        h50 = self.addHost('h50')
        h51 = self.addHost('h51')
        h52 = self.addHost('h52')
        h53 = self.addHost('h53')
        h54 = self.addHost('h54')
        h55 = self.addHost('h55')
        h56 = self.addHost('h56')
        h57 = self.addHost('h57')
        h58 = self.addHost('h58')
        h59 = self.addHost('h59')
        h60 = self.addHost('h60')
        h61 = self.addHost('h61')
        h62 = self.addHost('h62')
        h63 = self.addHost('h63')
        h64 = self.addHost('h64')
        h65 = self.addHost('h65')
        h66 = self.addHost('h66')
        h67 = self.addHost('h67')
        h68 = self.addHost('h68')
        h69 = self.addHost('h69')
        h70 = self.addHost('h70')
        h71 = self.addHost('h71')
        h72 = self.addHost('h72')
        h73 = self.addHost('h73')
        h74 = self.addHost('h74')
        h75 = self.addHost('h75')
        h76 = self.addHost('h76')
        h77 = self.addHost('h77')
        h78 = self.addHost('h78')
        h79 = self.addHost('h79')
        h80 = self.addHost('h80')
        h81 = self.addHost('h81')
        h82 = self.addHost('h82')
        h83 = self.addHost('h83')
        h84 = self.addHost('h84')
        h85 = self.addHost('h85')
        h86 = self.addHost('h86')
        h87 = self.addHost('h87')
        h88 = self.addHost('h88')
        h89 = self.addHost('h89')
        h90 = self.addHost('h90')
        h91 = self.addHost('h91')
        h92 = self.addHost('h92')
        h93 = self.addHost('h93')
        h94 = self.addHost('h94')
        h95 = self.addHost('h95')
        h96 = self.addHost('h96')
        h97 = self.addHost('h97')
        h98 = self.addHost('h98')
        h99 = self.addHost('h99')
        h100 = self.addHost('h100')
        h101 = self.addHost('h101')
        h102 = self.addHost('h102')
        h103 = self.addHost('h103')
        h104 = self.addHost('h104')
        h105 = self.addHost('h105')
        h106 = self.addHost('h106')
        h107 = self.addHost('h107')
        h108 = self.addHost('h108')
        h109 = self.addHost('h109')
        h110 = self.addHost('h110')
        h111 = self.addHost('h111')
        h112 = self.addHost('h112')
        h113 = self.addHost('h113')
        h114 = self.addHost('h114')
        h115 = self.addHost('h115')
        h116 = self.addHost('h116')
        h117 = self.addHost('h117')
        h118 = self.addHost('h118')
        h119 = self.addHost('h119')
        h120 = self.addHost('h120')
        h121 = self.addHost('h121')
        h122 = self.addHost('h122')
        h123 = self.addHost('h123')
        h124 = self.addHost('h124')
        h125 = self.addHost('h125')
        h126 = self.addHost('h126')
        h127 = self.addHost('h127')
        h128 = self.addHost('h128')

        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')
        s16 = self.addSwitch('s16')
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')
        s19 = self.addSwitch('s19')
        s20 = self.addSwitch('s20')
        s21 = self.addSwitch('s21')
        s22 = self.addSwitch('s22')
        s23 = self.addSwitch('s23')
        s24 = self.addSwitch('s24')
        s25 = self.addSwitch('s25')
        s26 = self.addSwitch('s26')
        s27 = self.addSwitch('s27')
        s28 = self.addSwitch('s28')
        s29 = self.addSwitch('s29')
        s30 = self.addSwitch('s30')
        s31 = self.addSwitch('s31')
        s32 = self.addSwitch('s32')
        s33 = self.addSwitch('s33')
        s34 = self.addSwitch('s34')
        s35 = self.addSwitch('s35')
        s36 = self.addSwitch('s36')
        s37 = self.addSwitch('s37')
        s38 = self.addSwitch('s38')
        s39 = self.addSwitch('s39')
        s40 = self.addSwitch('s40')
        s41 = self.addSwitch('s41')
        s42 = self.addSwitch('s42')
        s43 = self.addSwitch('s43')
        s44 = self.addSwitch('s44')
        s45 = self.addSwitch('s45')
        s46 = self.addSwitch('s46')
        s47 = self.addSwitch('s47')
        s48 = self.addSwitch('s48')
        s49 = self.addSwitch('s49')
        s50 = self.addSwitch('s50')
        s51 = self.addSwitch('s51')
        s52 = self.addSwitch('s52')
        s53 = self.addSwitch('s53')
        s54 = self.addSwitch('s54')
        s55 = self.addSwitch('s55')
        s56 = self.addSwitch('s56')
        s57 = self.addSwitch('s57')
        s58 = self.addSwitch('s58')
        s59 = self.addSwitch('s59')
        s60 = self.addSwitch('s60')
        s61 = self.addSwitch('s61')
        s62 = self.addSwitch('s62')
        s63 = self.addSwitch('s63')
        s64 = self.addSwitch('s64')
        s65 = self.addSwitch('s65')
        s66 = self.addSwitch('s66')
        s67 = self.addSwitch('s67')
        s68 = self.addSwitch('s68')
        s69 = self.addSwitch('s69')
        s70 = self.addSwitch('s70')
        s71 = self.addSwitch('s71')
        s72 = self.addSwitch('s72')
        s73 = self.addSwitch('s73')
        s74 = self.addSwitch('s74')
        s75 = self.addSwitch('s75')
        s76 = self.addSwitch('s76')
        s77 = self.addSwitch('s77')
        s78 = self.addSwitch('s78')
        s79 = self.addSwitch('s79')

        self.addLink(s0,s16)
        self.addLink(s1,s16)
        self.addLink(s2,s16)
        self.addLink(s3,s16)
        self.addLink(s16,s48)
        self.addLink(s16,s49)
        self.addLink(s16,s50)
        self.addLink(s16,s51)
        self.addLink(s4,s17)
        self.addLink(s5,s17)
        self.addLink(s6,s17)
        self.addLink(s7,s17)
        self.addLink(s17,s48)
        self.addLink(s17,s49)
        self.addLink(s17,s50)
        self.addLink(s17,s51)
        self.addLink(s8,s18)
        self.addLink(s9,s18)
        self.addLink(s10,s18)
        self.addLink(s11,s18)
        self.addLink(s18,s48)
        self.addLink(s18,s49)
        self.addLink(s18,s50)
        self.addLink(s18,s51)
        self.addLink(s12,s19)
        self.addLink(s13,s19)
        self.addLink(s14,s19)
        self.addLink(s15,s19)
        self.addLink(s19,s48)
        self.addLink(s19,s49)
        self.addLink(s19,s50)
        self.addLink(s19,s51)
        self.addLink(s48,h1)
        self.addLink(s48,h2)
        self.addLink(s48,h3)
        self.addLink(s48,h4)
        self.addLink(s49,h5)
        self.addLink(s49,h6)
        self.addLink(s49,h7)
        self.addLink(s49,h8)
        self.addLink(s50,h9)
        self.addLink(s50,h10)
        self.addLink(s50,h11)
        self.addLink(s50,h12)
        self.addLink(s51,h13)
        self.addLink(s51,h14)
        self.addLink(s51,h15)
        self.addLink(s51,h16)
        self.addLink(s0,s20)
        self.addLink(s1,s20)
        self.addLink(s2,s20)
        self.addLink(s3,s20)
        self.addLink(s20,s52)
        self.addLink(s20,s53)
        self.addLink(s20,s54)
        self.addLink(s20,s55)
        self.addLink(s4,s21)
        self.addLink(s5,s21)
        self.addLink(s6,s21)
        self.addLink(s7,s21)
        self.addLink(s21,s52)
        self.addLink(s21,s53)
        self.addLink(s21,s54)
        self.addLink(s21,s55)
        self.addLink(s8,s22)
        self.addLink(s9,s22)
        self.addLink(s10,s22)
        self.addLink(s11,s22)
        self.addLink(s22,s52)
        self.addLink(s22,s53)
        self.addLink(s22,s54)
        self.addLink(s22,s55)
        self.addLink(s12,s23)
        self.addLink(s13,s23)
        self.addLink(s14,s23)
        self.addLink(s15,s23)
        self.addLink(s23,s52)
        self.addLink(s23,s53)
        self.addLink(s23,s54)
        self.addLink(s23,s55)
        self.addLink(s52,h17)
        self.addLink(s52,h18)
        self.addLink(s52,h19)
        self.addLink(s52,h20)
        self.addLink(s53,h21)
        self.addLink(s53,h22)
        self.addLink(s53,h23)
        self.addLink(s53,h24)
        self.addLink(s54,h25)
        self.addLink(s54,h26)
        self.addLink(s54,h27)
        self.addLink(s54,h28)
        self.addLink(s55,h29)
        self.addLink(s55,h30)
        self.addLink(s55,h31)
        self.addLink(s55,h32)
        self.addLink(s0,s24)
        self.addLink(s1,s24)
        self.addLink(s2,s24)
        self.addLink(s3,s24)
        self.addLink(s24,s56)
        self.addLink(s24,s57)
        self.addLink(s24,s58)
        self.addLink(s24,s59)
        self.addLink(s4,s25)
        self.addLink(s5,s25)
        self.addLink(s6,s25)
        self.addLink(s7,s25)
        self.addLink(s25,s56)
        self.addLink(s25,s57)
        self.addLink(s25,s58)
        self.addLink(s25,s59)
        self.addLink(s8,s26)
        self.addLink(s9,s26)
        self.addLink(s10,s26)
        self.addLink(s11,s26)
        self.addLink(s26,s56)
        self.addLink(s26,s57)
        self.addLink(s26,s58)
        self.addLink(s26,s59)
        self.addLink(s12,s27)
        self.addLink(s13,s27)
        self.addLink(s14,s27)
        self.addLink(s15,s27)
        self.addLink(s27,s56)
        self.addLink(s27,s57)
        self.addLink(s27,s58)
        self.addLink(s27,s59)
        self.addLink(s56,h33)
        self.addLink(s56,h34)
        self.addLink(s56,h35)
        self.addLink(s56,h36)
        self.addLink(s57,h37)
        self.addLink(s57,h38)
        self.addLink(s57,h39)
        self.addLink(s57,h40)
        self.addLink(s58,h41)
        self.addLink(s58,h42)
        self.addLink(s58,h43)
        self.addLink(s58,h44)
        self.addLink(s59,h45)
        self.addLink(s59,h46)
        self.addLink(s59,h47)
        self.addLink(s59,h48)
        self.addLink(s0,s28)
        self.addLink(s1,s28)
        self.addLink(s2,s28)
        self.addLink(s3,s28)
        self.addLink(s28,s60)
        self.addLink(s28,s61)
        self.addLink(s28,s62)
        self.addLink(s28,s63)
        self.addLink(s4,s29)
        self.addLink(s5,s29)
        self.addLink(s6,s29)
        self.addLink(s7,s29)
        self.addLink(s29,s60)
        self.addLink(s29,s61)
        self.addLink(s29,s62)
        self.addLink(s29,s63)
        self.addLink(s8,s30)
        self.addLink(s9,s30)
        self.addLink(s10,s30)
        self.addLink(s11,s30)
        self.addLink(s30,s60)
        self.addLink(s30,s61)
        self.addLink(s30,s62)
        self.addLink(s30,s63)
        self.addLink(s12,s31)
        self.addLink(s13,s31)
        self.addLink(s14,s31)
        self.addLink(s15,s31)
        self.addLink(s31,s60)
        self.addLink(s31,s61)
        self.addLink(s31,s62)
        self.addLink(s31,s63)
        self.addLink(s60,h49)
        self.addLink(s60,h50)
        self.addLink(s60,h51)
        self.addLink(s60,h52)
        self.addLink(s61,h53)
        self.addLink(s61,h54)
        self.addLink(s61,h55)
        self.addLink(s61,h56)
        self.addLink(s62,h57)
        self.addLink(s62,h58)
        self.addLink(s62,h59)
        self.addLink(s62,h60)
        self.addLink(s63,h61)
        self.addLink(s63,h62)
        self.addLink(s63,h63)
        self.addLink(s63,h64)
        self.addLink(s0,s32)
        self.addLink(s1,s32)
        self.addLink(s2,s32)
        self.addLink(s3,s32)
        self.addLink(s32,s64)
        self.addLink(s32,s65)
        self.addLink(s32,s66)
        self.addLink(s32,s67)
        self.addLink(s4,s33)
        self.addLink(s5,s33)
        self.addLink(s6,s33)
        self.addLink(s7,s33)
        self.addLink(s33,s64)
        self.addLink(s33,s65)
        self.addLink(s33,s66)
        self.addLink(s33,s67)
        self.addLink(s8,s34)
        self.addLink(s9,s34)
        self.addLink(s10,s34)
        self.addLink(s11,s34)
        self.addLink(s34,s64)
        self.addLink(s34,s65)
        self.addLink(s34,s66)
        self.addLink(s34,s67)
        self.addLink(s12,s35)
        self.addLink(s13,s35)
        self.addLink(s14,s35)
        self.addLink(s15,s35)
        self.addLink(s35,s64)
        self.addLink(s35,s65)
        self.addLink(s35,s66)
        self.addLink(s35,s67)
        self.addLink(s64,h65)
        self.addLink(s64,h66)
        self.addLink(s64,h67)
        self.addLink(s64,h68)
        self.addLink(s65,h69)
        self.addLink(s65,h70)
        self.addLink(s65,h71)
        self.addLink(s65,h72)
        self.addLink(s66,h73)
        self.addLink(s66,h74)
        self.addLink(s66,h75)
        self.addLink(s66,h76)
        self.addLink(s67,h77)
        self.addLink(s67,h78)
        self.addLink(s67,h79)
        self.addLink(s67,h80)
        self.addLink(s0,s36)
        self.addLink(s1,s36)
        self.addLink(s2,s36)
        self.addLink(s3,s36)
        self.addLink(s36,s68)
        self.addLink(s36,s69)
        self.addLink(s36,s70)
        self.addLink(s36,s71)
        self.addLink(s4,s37)
        self.addLink(s5,s37)
        self.addLink(s6,s37)
        self.addLink(s7,s37)
        self.addLink(s37,s68)
        self.addLink(s37,s69)
        self.addLink(s37,s70)
        self.addLink(s37,s71)
        self.addLink(s8,s38)
        self.addLink(s9,s38)
        self.addLink(s10,s38)
        self.addLink(s11,s38)
        self.addLink(s38,s68)
        self.addLink(s38,s69)
        self.addLink(s38,s70)
        self.addLink(s38,s71)
        self.addLink(s12,s39)
        self.addLink(s13,s39)
        self.addLink(s14,s39)
        self.addLink(s15,s39)
        self.addLink(s39,s68)
        self.addLink(s39,s69)
        self.addLink(s39,s70)
        self.addLink(s39,s71)
        self.addLink(s68,h81)
        self.addLink(s68,h82)
        self.addLink(s68,h83)
        self.addLink(s68,h84)
        self.addLink(s69,h85)
        self.addLink(s69,h86)
        self.addLink(s69,h87)
        self.addLink(s69,h88)
        self.addLink(s70,h89)
        self.addLink(s70,h90)
        self.addLink(s70,h91)
        self.addLink(s70,h92)
        self.addLink(s71,h93)
        self.addLink(s71,h94)
        self.addLink(s71,h95)
        self.addLink(s71,h96)
        self.addLink(s0,s40)
        self.addLink(s1,s40)
        self.addLink(s2,s40)
        self.addLink(s3,s40)
        self.addLink(s40,s72)
        self.addLink(s40,s73)
        self.addLink(s40,s74)
        self.addLink(s40,s75)
        self.addLink(s4,s41)
        self.addLink(s5,s41)
        self.addLink(s6,s41)
        self.addLink(s7,s41)
        self.addLink(s41,s72)
        self.addLink(s41,s73)
        self.addLink(s41,s74)
        self.addLink(s41,s75)
        self.addLink(s8,s42)
        self.addLink(s9,s42)
        self.addLink(s10,s42)
        self.addLink(s11,s42)
        self.addLink(s42,s72)
        self.addLink(s42,s73)
        self.addLink(s42,s74)
        self.addLink(s42,s75)
        self.addLink(s12,s43)
        self.addLink(s13,s43)
        self.addLink(s14,s43)
        self.addLink(s15,s43)
        self.addLink(s43,s72)
        self.addLink(s43,s73)
        self.addLink(s43,s74)
        self.addLink(s43,s75)
        self.addLink(s72,h97)
        self.addLink(s72,h98)
        self.addLink(s72,h99)
        self.addLink(s72,h100)
        self.addLink(s73,h101)
        self.addLink(s73,h102)
        self.addLink(s73,h103)
        self.addLink(s73,h104)
        self.addLink(s74,h105)
        self.addLink(s74,h106)
        self.addLink(s74,h107)
        self.addLink(s74,h108)
        self.addLink(s75,h109)
        self.addLink(s75,h110)
        self.addLink(s75,h111)
        self.addLink(s75,h112)
        self.addLink(s0,s44)
        self.addLink(s1,s44)
        self.addLink(s2,s44)
        self.addLink(s3,s44)
        self.addLink(s44,s76)
        self.addLink(s44,s77)
        self.addLink(s44,s78)
        self.addLink(s44,s79)
        self.addLink(s4,s45)
        self.addLink(s5,s45)
        self.addLink(s6,s45)
        self.addLink(s7,s45)
        self.addLink(s45,s76)
        self.addLink(s45,s77)
        self.addLink(s45,s78)
        self.addLink(s45,s79)
        self.addLink(s8,s46)
        self.addLink(s9,s46)
        self.addLink(s10,s46)
        self.addLink(s11,s46)
        self.addLink(s46,s76)
        self.addLink(s46,s77)
        self.addLink(s46,s78)
        self.addLink(s46,s79)
        self.addLink(s12,s47)
        self.addLink(s13,s47)
        self.addLink(s14,s47)
        self.addLink(s15,s47)
        self.addLink(s47,s76)
        self.addLink(s47,s77)
        self.addLink(s47,s78)
        self.addLink(s47,s79)
        self.addLink(s76,h113)
        self.addLink(s76,h114)
        self.addLink(s76,h115)
        self.addLink(s76,h116)
        self.addLink(s77,h117)
        self.addLink(s77,h118)
        self.addLink(s77,h119)
        self.addLink(s77,h120)
        self.addLink(s78,h121)
        self.addLink(s78,h122)
        self.addLink(s78,h123)
        self.addLink(s78,h124)
        self.addLink(s79,h125)
        self.addLink(s79,h126)
        self.addLink(s79,h127)
        self.addLink(s79,h128)

topos = { 'mytopo': ( lambda: MyTopo() ) }
    
