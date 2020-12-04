"""
ReadTheDocs needs to build sphinx docs, but has trouble installing RocketCEA.
This mocks the ox and fuel CEA input cards.
"""

#  ==== Use convention of ending with (G) for gaseous propellants, O2(G), CH4(G), etc.
#  NOTE !!!!! xxx(G) will be Changed to Gxxx <========= !!!!!!!!
#
# cards are an index to either a string or a list of strings
#
#  Heats of formation in CEA thermo.inp file are in Joules
#    Multiply by 0.238846 to convert into cal
#
# !!! MAKE SURE LINES HAVE A SPACE ON THE END !!!

oxCards = {
        "AIR"  :["oxid Air    wt%=100.00 ",
                  " h,cal=-28.2     t(k)=298.15   "],
        "AIRSIMP" :[" oxid AIRSIMP  N 1.5622 O .4192 Ar .0093 ",
                " h,cal=0.     t(k)=298.15   "],
        "CLF5"  :[" oxid CLF5(L)   CL 1 F 5   wt%=100.00 ",
                  " h,cal=-60500.0     t(k)=298.15   "],
        "CLF3"  :[" oxid CLF3(L)   CL 1 F 3   wt%=100.00 ",
                  " h,cal=-45680.0     t(k)=298.15   "],
        "OF2": [" oxid OF2(L)  O 1 F 2  ",
                 " h,cal=2524.      t(k)=167.0       wt%=100. "],
        "N2H4" :[" oxid N2H4(L)  N 2 H 4    wt%=100. ",
                " h,cal=12100.0     t(k)=298.15   rho=1.0036 "],
        "N2F4": [" oxid N2F4(L)  N 2 F 4  ",
                 " h,cal=-5200.0      t(k)=199.0       wt%=100. "],
        "F2":  [" oxid F2(L)  F 2  ",
                 " h,cal=-3098.      t(k)=82.02       wt%=100. "],
        "O2":  [" oxid O2(L)  O 2  ",
                 " h,cal=-3102.      t(k)=90.18       wt%=100. "],
        # match the O2(L) properties used on the CEA on-line site
        "LO2_NASA":  [" oxid O2(L)  O 2  ",
                 " h,cal=-3102.055      t(k)=90.17       wt%=100. "],
        "LO2":  [" oxid O2(L)  O 2  ",
                 " h,cal=-3102.      t(k)=90.18       wt%=100. "],
        "LOX":  [" oxid O2(L)  O 2  ",
                 " h,cal=-3102.      t(k)=90.18       wt%=100. "],
        "GOX":  [" oxid O2(G)  O 2  ",
                 " h,cal=0.      t(k)=298.15       wt%=100. "],
        "GO2":  [" oxid O2(G)  O 2  ",
                 " h,cal=0.      t(k)=298.15       wt%=100. "],
        "MON3"  :[" oxid N2O4(L)   N 2 O 4   wt%=100.00 ",
                  " h,cal=-4676.0     t(k)=298.15   "],
        "N2O4"  :[" oxid N2O4(L)   N 2 O 4   wt%=100.00 ",
                  " h,cal=-4676.0     t(k)=298.15   "],
        "N2O3"  :[" oxid N2O3(L)   N 2 O 3   wt%=100.00 ",
                  " h,cal=12020.7     t(k)=298.15   "],                  
        "MON15"  :[" oxid N2O4(L)   N 2 O 4   wt%=62.01 ",
                  " h,cal=-4676.0     t(k)=298.15    ",
                  " oxid N2O3   N 2 O 3   wt%=37.99 ",
                  " h,cal=12020.7     t(k)=298.15   "],
        "MON25"  :[" oxid N2O4(L)   N 2 O 4   wt%=36.67 ",
                  " h,cal=-4676.0     t(k)=298.15    ",
                  " oxid N2O3   N 2 O 3   wt%=63.33 ",
                  " h,cal=12020.7     t(k)=298.15   "],
        "N2O"   :[" oxid NitrousOxide  N 2.0 O 1.0  wt%=100.00 ",
                  " h,cal= 19467.0 t(k)=298.15 "],
        "N2O_nbp"   :[" oxid NitrousOxide  N 2.0 O 1.0  wt%=100.00 ",
                  " h,cal= 14583.0 t(k)=184.4 "],
        "HNO3"  :[" oxid HNO3(L) H 1 N 1 O 3   wt%=100.00 ",
                  " h,cal=-42460.0     t(k)=298.15  rho.g/cc=1.5027 "],
        "IRFNA"  :[" oxid IRFNA  H 1.57216 N 1.62945 O 4.69505 F 0.02499   wt%=100.00 ",
                  " h,cal=-64860.0     t(k)=298.15  rho.g/cc=1.48 "],
        "H2O2"  :[" oxid H2O2(L) H 2 O 2  wt%=100.00 ",
                  " h,cal=-44880.0     t(k)=298.15  rho.g/cc=1.407 "],
        "H2O":["oxid water H 2.0 O 1.0  wt%=100.0 ",
               "h,cal=-68308.  t(k)=298.15 rho,g/cc = 0.9998  "],
        "90_H2O2":[" oxid H2O2(L) H 2 O 2  wt%=90.00 ",
                  " h,cal=-44880.0     t(k)=298.15  rho.g/cc=1.407 ",
                   " oxid = WATER H 2.0 O 1.0 wt%= 10.0        ",
                   " h,cal=-68317. t(k)=298.15 rho.g/cc=1.0   "],
        "98_H2O2":[" oxid H2O2(L) H 2 O 2  wt%=98.00 ",
                  " h,cal=-44880.0     t(k)=298.15  rho.g/cc=1.407 ",
                   " oxid = WATER H 2.0 O 1.0 wt%= 2.0        ",
                   " h,cal=-68317. t(k)=298.15 rho.g/cc=1.0   "],
        "Peroxide98":[" oxid H2O2(L) H 2 O 2  wt%=98.00 ",
                  " h,cal=-44880.0     t(k)=298.15  rho.g/cc=1.407 ",
                   " oxid = WATER H 2.0 O 1.0 wt%= 2.0        ",
                   " h,cal=-68317. t(k)=298.15 rho.g/cc=1.0   "],
        "Peroxide90":[" oxid H2O2(L) H 2 O 2  wt%=90.00 ",
                  " h,cal=-44880.0     t(k)=298.15  rho.g/cc=1.407 ",
                   " oxid = WATER H 2.0 O 1.0 wt%= 10.0        ",
                   " h,cal=-68317. t(k)=298.15 rho.g/cc=1.0   "],
        "HAN315" :[ " oxid = HAN C 0.064 H 4.296 N 2.062 O 4.1 P 0.008 wt%= 44.5       ",
                    " h,cal=-93980. t(k)=298.15 rho.g/cc=1.685     ",
                    " oxid = HEHN C 2.0 H 9.0 N 3.0 O 4.0 wt%= 44.5         ",
                    " h,cal=-108000. t(k)=298.15 rho.g/cc=1.428    ",
                    " oxid = WATER H 2.0 O 1.0 wt%= 11.0        ",
                    " h,cal=-68000. t(k)=298.15 rho.g/cc=1.0    ",
                  ]
        }
                
# cards are an index to either a string or a list of strings
#
#  Heats of formation in CEA thermo.inp file are in Joules
#    Multiply by 0.238846 to convert into cal
#
# added Kerosene, Gasoline, JP10, JP4, JPX, Acetylene AT BOTTOM of "fuelCards ="
fuelCards = {
        "CH3OH":  [" fuel CH3OH(L)   C 1 H 4 O 1   ",
                 " h,cal=-57040.0      t(k)=298.15       wt%=100. "],
        "Methanol":  [" fuel CH3OH(L)   C 1 H 4 O 1   ",
                 " h,cal=-57040.0      t(k)=298.15       wt%=100. "],
        "METHANOL":  [" fuel CH3OH(L)   C 1 H 4 O 1   ",
                 " h,cal=-57040.0      t(k)=298.15       wt%=100. "],
        "B2H6":  [" fuel B2H6(L)   B 2 H 6   ",
                 " h,cal=4970.0      t(k)=180.0       wt%=100. "],
        "C2H5OH":  [" fuel C2H5OH(L)   C 2 H 6 O 1   ",
                 " h,cal=-66370.0      t(k)=298.15       wt%=100. "],
        "Ethanol":  [" fuel C2H5OH(L)   C 2 H 6 O 1   ",
                 " h,cal=-66370.0      t(k)=298.15       wt%=100. "],
        "ETHANOL":  [" fuel C2H5OH(L)   C 2 H 6 O 1   ",
                 " h,cal=-66370.0      t(k)=298.15       wt%=100. "],
        "GH2_160":  [" fuel H2(G)  H 2  ",
                 " h,cal=-940.      t(k)=160.0       wt%=100. "],
        "GH2":  [" fuel H2(G)  H 2  ",
                 " h,cal=0.      t(k)=298.15       wt%=100. "],
        "LH2":  [" fuel H2(L)  H 2  ",
                 " h,cal=-2154.0      t(k)=20.27       wt%=100. "],
        "H2":  [" fuel H2(L)  H 2  ",
                 " h,cal=-2154.0      t(k)=20.27       wt%=100. "],
        # match the H2(L) properties used on the CEA on-line site
        "LH2_NASA":  [" fuel H2(L)  H 2  ",
                 " h,cal=-2153.920      t(k)=20.27       wt%=100. "],
                 
        "MMH" :[" fuel CH6N2(L)  C 1     H 6     N 2     wt%=100.00 ",
                " h,cal=12900.0     t(k)=298.15   rho=.874 "],
        "N2H4" :[" fuel N2H4(L)  N 2 H 4    wt%=100. ",
                " h,cal=12100.0     t(k)=298.15   rho=1.0036 "],
        "NH3" :[" fuel NH3(L)   N 1 H 3      wt%=100. ",
                " h,cal=-17090.     t(k)=298.15   rho=0.676 "],
        "M20_NH3" :["  fuel CH6N2(L)  C 1 H 6 N 2  wt%=17.9 ",
               " h,cal=12900.0     t(k)=298.15   rho=.874 ",
               " fuel N2H4(L)  N 2 H 4    wt%=71.6 ",
               " h,cal=12100.0     t(k)=298.15   rho=1.0036 ",
               " fuel NH3(L)   N 1 H 3      wt%=10.5 ",
               " h,cal=-17090.     t(k)=298.15   rho=0.676"    ],
        "M20" :["  fuel CH6N2(L)  C 1 H 6 N 2  wt%=20.0 ",
               " h,cal=12900.0     t(k)=298.15   rho=.874 ",
               " fuel N2H4(L)  N 2 H 4    wt%=80.0 ",
               " h,cal=12100.0     t(k)=298.15   rho=1.0036"   ],
        "MHF3" :["  fuel CH6N2(L)  C 1 H 6 N 2  wt%=86.0 ",
               " h,cal=12900.0     t(k)=298.15   rho=.874 ",
               " fuel N2H4(L)  N 2 H 4    wt%=14.0 ",
               " h,cal=12100.0     t(k)=298.15   rho=1.0036"   ],
        "A50" :[" fuel C2H8N2(L),UDMH wt% 50.   t(k) 298.15 ",
                " h,cal=11900.0     t(k)=298.15   rho=.783 ",
                " fuel N2H4(L)  N 2 H 4    wt%=50. ",
                " h,cal=12100.0     t(k)=298.15   rho=1.0036 "],
        "UDMH" :[" fuel C2H8N2(L),UDMH wt% 50.   t(k) 298.15 ",
                " h,cal=11900.0     t(k)=298.15   rho=.783 "],
        "RP_1" :[" fuel RP-1  C 1 H 1.9423 ",
                " h,cal=-5430.     t(k)=298.15   rho=0.773 "],
        "RP1" :[" fuel RP-1  C 1 H 1.9423 ",
                " h,cal=-5430.     t(k)=298.15   rho=0.773 "],
        # match the RP1 properties used on the CEA on-line site
        "RP1_NASA" :[" fuel RP-1  C 1 H 1.95 ",
                " h,cal=-5907.672     t(k)=298.15   rho=0.773 "],
        "JetA" :[" fuel Jet-A(L)  C  12.0 H  23.0 ",
                " h,cal=-72466.6     t(k)=298.15   rho=0.815 "],
        "C3H8" :[" fuel C3H8(L) C 3 H 8     wt%=100. ",
                " h,cal=-30372.     t(k)=231.08   rho=0.5808 "],
        "Propane" :[" fuel C3H8(L) C 3 H 8     wt%=100. ",
                " h,cal=-30372.     t(k)=231.08   rho=0.5808 "],
        "C2H6_167" :[" fuel C2H6(L) C 2 H 6     wt%=100. ",
                " h,cal=-25296.0     t(k)=167.0   rho=0.5808 "],
        "C2H6" :[" fuel C2H6(L) C 2 H 6     wt%=100. ",
                " h,cal=-24797.0     t(k)=184.56   rho=0.5808 "],
        "Isopropanol" : [" fuel C3H8O-2propanol C 3 H 8 O 1    wt%=100. ",
                " h,cal=-65133.     t(k)=298.15   rho=0.786 "],
        "Propylene" : [" fuel C3H6,propylene C 3 H 6    wt%=100. ",
                " h,cal=4776.92     t(k)=298.15   rho=0.0018 "],
        "propylene" : [" fuel C3H6,propylene C 3 H 6    wt%=100. ",
                " h,cal=4776.92     t(k)=298.15   rho=0.0018 "],
        "CH4" :[" fuel CH4(L) C 1 H 4     wt%=100.  ",
                " h,cal=-21390.     t(k)=111.66   rho=0.4239  "],
        # match the CH4(L) properties used on the CEA on-line site
        "LCH4_NASA" :[" fuel CH4(L) C 1 H 4     wt%=100.  ",
                " h,cal=-21327.199     t(k)=111.643   rho=0.4239  "],
        "GCH4": [" fuel CH4(G) C 1 H 4  ",
               " h,cal=-17895.0      t(k)=298.15       wt%=100.  "],
        "CINCH":[" fuel CINCH(L)     C 4.     H 10.    N 4.  ",
                 " h,cal=66550.      t(k)=298.15             wt%=100. "],
        "ECP_dimer":[" fuel ECP-dimer(L) C 10.    H 10. ",
                     " h,cal=123600.     t(k)=298.15                     wt%=100. "],
        "H2O":["fuel water H 2.0 O 1.0  wt%=100.0  ",
               "h,cal=-68308.  t(k)=298.15 rho,g/cc = 0.9998  "],
        "DMAZ":["fuel dmaz C 4.0 H 10.0 N 4.0 wt%= 100.00  ",
                "h,cal=66548. t(k)=298.15 rho,g/cc = 0.93   "],
        "NITROMETHANE":["fuel nitroMethane C 1. H 3. N 1. O 2. wt%= 100.00  ",
            "h,cal=-27030. t(k)=298.15  rho,g/cc =1.1371 "],
        "AL":["fuel  Aluminum  t(k)=298.15 AL 1                               wt%=100.00  ",
                        "h,cal=0.0     t(k)=298.15  "],
        "HTPB":["fuel R-45(HTPB FROM_RPL_DATA) C 7.3165 H 10.3360 O 0.1063    wt%=100.00  ",
                        "h,cal= 1200.0 t(k)=298.15 rho=0.9220 "],
        "AP":[" fuel NH4CLO4(I)       wt%=100.00 "],
        "CFx":[" fuel CFx    C 1.0 F 1.0   wt%=100.00  ",
                " h,cal=57863.0     t(k)=298.15   rho=1.8200 "]
        }
        
fuelCards["Kerosene"] = [" fuel Kerosene  C 1 H 1.9532  ",
                        " h,cal=-5769.     t(k)=298.15   rho=0.8 "]
                             
fuelCards["Kerosene90_H2O10"] = [" fuel Kerosene  C 1 H 1.9532  wt%=90.00  ",
                                " h,cal=-5769.     t(k)=298.15   rho=0.8  ",
                                " fuel = WATER H 2.0 O 1.0  wt%= 10.0    ",
                                " h,cal=-68317. t(k)=298.15 rho.g/cc=1.0   "]
                             
                             
fuelCards["Gasoline"] = [" fuel Gasoline  C 8 H 18  ",
                        " h,cal=-49809.     t(k)=298.15   rho=0.7025 "]

# JP10 from TDK Reactant Cards
# cards["JP10"]    = "C 10.0   H 16.000                              100.    -29350.L 298.15 F"
fuelCards["JP10"] = [" fuel JP10  C 10 H 16  wt%=100.00  ",
                    " h,cal=-29350.     t(k)=298.15   rho=0.9318 "]


# JP4 is 50/50 Kerosene/Gasoline
fuelCards["JP4"] = [" fuel Kerosene  C 1 H 1.9532  wt%=50.00  ",
                    " h,cal=-5769.     t(k)=298.15   rho=0.8  ",
                    " fuel Gasoline  C 8 H 18  wt%=50.00  ",
                    " h,cal=-49809.     t(k)=298.15   rho=0.7025 "]

# JPX is 60/40 JP4/UDMH
fuelCards["JPX"] = [" fuel C2H8N2(L),UDMH wt%=60.   t(k) 298.15  ",
                    " h,cal=11900.0     t(k)=298.15   rho=.783  ",
                    " fuel Kerosene  C 1 H 1.9532  wt%=30.00  ",
                    " h,cal=-5769.     t(k)=298.15   rho=0.8  ",
                    " fuel Gasoline  C 8 H 18  wt%=30.00  ",
                    " h,cal=-49809.     t(k)=298.15   rho=0.7025 "]
                        
fuelCards["C2H2"] = [" fuel Acetylene  C 2 H 2   wt%=100.   ",
                          " h,cal=54324.     t(k)=198.3   rho=0.9 "]
fuelCards["Acetylene"] = fuelCards["C2H2"]


                
# cards are an index to either a string or a list of strings
propCards = {
        "ARC448":[" name ARC448  H 3.359766 C 2.052322 N 1.932190 O 2.806300  wt%=100.00  ",
                  " h,cal= -36867.1  t(k)=298.15 rho=1.537 "],
        "ARC452":[" name ARC452  H 3.694563 C 2.469813 N 1.041212 O 3.251794  wt%=100.00  ",                                
                  " h,cal= -67947.0  t(k)=298.15 rho=1.473 "],
        "ARC457":[" name ARC457  H 4.080395 C 1.238333 N 1.677693 O 3.593891  ",                                                        
                  " wt%=100.00 h,cal= -80325.0 t(k)=298.15 rho=1.594 "], 
        "ARC311":[" name ARC311  H 3.919935 C 2.237043 N 2.300870 O 2.309573  wt%=100.00  ",                                                            
                  " h,cal= 3939.6  t(k)=298.15 rho=1.634 "],                                    
        "HYD40" :[   " name = diss UA 0.800 H 1.600 N 1.200 wt%= 99.5  ", # N2H4 with 40% NH3 dissociation
                    " h,cal=12094. t(k)=298.15 rho,g/cc = 1.004     ",
                    "  ",
                    " name = water H 2.0 O 1.0  wt%=0.5   ",
                    " h,cal=-68308.  t(k)=298.15 rho,g/cc = 0.9998   ",
                    " !	THIS IS 40% AMMONIA DISSOCIATION ",
                    " omit NH3 "],
        "HAN269" :[ " name = HAN N 2.0 H 4.0 O 4.0 wt%= 69.15        ",
                    " h,cal=-80962. t(k)=298.15 rho,g/cc = 1.685   ",
                    " name = MEOH C 1.0 H 4.0 O 1.0 wt%= 15.46       ",
                    " h,cal=-57146. t(k)=298.15 rho,g/cc = 0.791 ",
                    " name = water H 2.0 O 1.0 wt%= 14.80      ",
                    " h,cal=-68256. t(k)=298.17 rho,g/cc=1.00  ",
                    " name = AN H 4.0 N 2.0 O 3.0 wt%= 0.59      ",
                    " h,cal=-87380. t(k)=298.17 rho,g/cc=1.725 ",
                  ],
        "HAN315" :[ " name = HAN C 0.064 H 4.296 N 2.062 O 4.1 P 0.008 wt%= 44.5      ",
                    " h,cal=-93980. t(k)=298.15 rho.g/cc=1.685    ",
                    " name = HEHN C 2.0 H 9.0 N 3.0 O 4.0 wt%= 44.5        ",
                    " h,cal=-108000. t(k)=298.15 rho.g/cc=1.428   ",
                    " name = WATER H 2.0 O 1.0 wt%= 11.0       ",
                    " h,cal=-68000. t(k)=298.15 rho.g/cc=1.0   ",
                  ],
        "HPB24" :[  " name = diss UA 0.6667 H 2.0000 N 1.3333 wt%= 71.46   ",
                    " h,cal=12094. t(k)=298.15 rho,g/cc = 1.004   ",
                    " name = water H 2.0 O 1.0  wt%=0.5   ",
                    " h,cal=-68308.  t(k)=298.15 rho,g/cc = 0.9998   ",
                    " name = hydra H 4.0 N 2.0 wt%= 4.04    ",
                    " h,cal=12094. t(k)=298.15 rho,g/cc = 1.004    ",
                    " name = hydni N 3.000 H 5.000 O 3.000 wt%= 24.00   ",     
                    " h,cal=-50477. t(k)=298.15 rho,g/cc = 1.647 ",
                ],
        "AP10_RDX25_HTPB":["  name NH4CLO4(I)       wt%=10.0 ",
               " name RDX    C 1.3506 H 2.7011 O 2.7011 N 2.7011  wt%=25.00 ",
               " h,cal=6610.     t(k)=298.15   rho=1.8200 ",
               " name R-45(HTPB FROM_RPL_DATA) C 7.3165 H 10.3360 O 0.1063    wt%=65.00 ",
               " h,cal= 1200.0 t(k)=298.15 rho=0.9220 "],
               
        "AMT_2091":[  "name NH4NO3         H  4.9968 O  3.7476 N  2.4984                   wt%=75.00 ",
                      "h,cal=-109019.9966   t(k)=298.15   rho=1.7250 ",
                      "name (NH4)2CR2O7   H  3.1733 O  2.7766  N  0.7933  CR 0.7933        wt%=2.00 ",
                      "h,cal=-168780.   t(k)=298.15   rho=2.1500 ",
                      "name A-20_GENPOL  C  4.5500  H  7.1000  O  2.3900                   wt%=7.24 ",
                      "h,cal=-111000.   t(k)=298.15   rho=1.0380 ",
                      "name METHYL_ACRYLATE   C  4.6464  H  6.9696  O  2.3232              wt%=11.08 ",
                      "h,cal=-111300.   t(k)=298.15   rho=1.2000 ",
                      "name POLYSTYRENE  C  7.6817  H  7.6817                              wt%=3.957 ",
                      "h,cal=8000.   t(k)=298.15   rho=1.0600 ",
                      "name MAKP   C  5.3768  H 10.7535  O  1.5362  wt%=0.40 ",
                      "h,cal=-134060.   t(k)=298.15   rho=0.8500 ",
                      "name CALCIUM_PHOSPHATE  P  0.6447  CA 0.9671 O  2.5790              wt%=0.50 ",
                      "h,cal=-300500.   t(k)=298.15   rho=3.1400 ",
                      "name TIN_OCTOATE  C  3.9497 H  7.4057 O  0.9874 PB 0.0948 CU 0.1521 wt%=0.003 ",
                      "h,cal=-76120.   t(k)=298.15   rho=1.0000 ",
                      "name LECITHIN  C  5.5611 H 11.1223 O  1.2692 N  0.1208              wt%=0.18 ",
                      "h,cal=-63010.   t(k)=298.15   rho=1.0220 "],
            }
# !!! MAKE SURE LINES HAVE A SPACE ON THE END !!!
            
