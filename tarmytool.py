# This tool helps calculate army build times for travian
# Version: .02 alpha
# Author: Juan A. Uribe
# Date: April 4, 2015

#               Updated: April 5, 2015
#               Description: User can adjust based on age (days) of server and day arm building started
#               Description: Works for anvils and hammer armies optimal prototypes (Teuton mace rammer, roman ei hammer)
# TODO:
# Add calculations when trainer used after day 100
# Add ability to calculate more than anvil of each time, i.e. the amount of anvils at the WW

import os
# for linux os.system('clear')

# Roman Army 
praet = 238
imp = 259
ei = 245
ec = 380
el = 207
bram = 621
fcat = 1216

# Gaul Army
phal = 140
sword = 195
druid = 346
head = 421
tt = 335
gram = 675
treb = 1216

# Teuton Army
spear = 191
mace = 97
scout = 151 
axe = 202
pal = 324
tk = 400 
ram = 567
cat = 1216

# Time to build
hour = 3600
day = 24 * hour
week = 7 * day
month = 30 * day
year = 356 * day

fdef = 3000
dactive = 0

class bcolors:
        OKWHITE = '\033[96m'
        OKCYAN = '\033[96m'
        OKPINK = '\033[95m'
        OKBLUE = '\033[94m'
        OKYELLOW = '\033[93m'
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
# Methods to calculate hammers
def rom_hammer(time,active):
        cav = ei
	infsize = (time-active)* day / imp
	cavsize = (time-active)* day/ cav
	siege = (time-active)*day /fcat
	feeder = time/10
	print "Imperians built in this time: %d" %( infsize )
	print "EI built in this time: %d" % cavsize
	print "Fire Catapults built in this time: %d" % siege
	print "Total anvil size:  " + bcolors.OKBLUE + "%d" % (infsize + 2*cavsize + siege*6) + bcolors.ENDC
	print "Total number of villages : " +bcolors.OKCYAN + "%d" % feeder + bcolors.ENDC
	print ""
def gaul_hammer(time,active):
        cav = tt
	infsize = (time-active)* day / sword
	cavsize = (time-active)* day/ cav
	siege = (time-active)*day /treb
	feeder = time/10
	print "Swordsmen built in this time: %d" %( infsize )
	print "TT built in this time: %d" % cavsize
	print "Trebuchets built in this time: %d" % siege
	print "Total Hammer size:  " + bcolors.OKYELLOW + "%d" % (infsize + 2*cavsize + siege*6) + bcolors.ENDC
	print "Total number of villages : " +bcolors.OKCYAN + "%d" % feeder + bcolors.ENDC
	print ""
def teut_rammer(time,active):
        cav = tk
	infsize = (time-active)* day / mace
	cavsize = (time-active)* day/ cav
	siege = (time-active)*day /ram
	feeder = time/10
	print "Macemen built in this time: %d" %( infsize )
	print "TK built in this time: %d" % cavsize
	print "Rams built in this time: %d" % siege
	print "Total Hammer size:  " + bcolors.OKGREEN + "%d" % (infsize + 3*cavsize + siege*3) + bcolors.ENDC
	print "Total number of villages : " +bcolors.OKCYAN + "%d" % feeder + bcolors.ENDC
	print ""


        
# Methods to calculate anvils
def rom_anvil(time,active):
       	feeder = time/10
	psize = (time-active)* day / praet + feeder * fdef
	ecsize = (time-active)* day/ ec
	print "Praets built in this time: %d" %( psize )
	print "EC built in this time : %d" % ecsize
	print "Total anvil size:  " + bcolors.OKBLUE + "%d" % (psize + 4*ecsize ) + bcolors.ENDC
	print "Total number of villages : " +bcolors.OKCYAN + "%d" % feeder + bcolors.ENDC
	print ""

def gaul_anvil(time,active):
	feeder = time/10
	gsize = (time-active)*day/phal + fdef * feeder
	drusize = (time-active)*day/druid
	print "Phalanx built in this time: %d" %gsize
	print "Druidriders built in this time: %d" % drusize
	print "Total anvil size: " + bcolors.OKYELLOW + "%d" % (gsize + 2*drusize) + bcolors.ENDC
	print "Total number of villages: " +bcolors.OKCYAN + "%d" % feeder + bcolors.ENDC
	print ""

def teut_anvil(time,active):
	feeder = time/10
	infsize = (time-active)*day/spear + feeder *fdef
	cavsize = (time-active)*day/pal
	print "Spear built in this time: %d" %infsize
	print "Paladins built in this time: %d" % cavsize
	print "Total anvil size: " + bcolors.OKGREEN +"%d" % (infsize + 2*cavsize) + bcolors.ENDC
	print "Total number of villages: " +bcolors.OKCYAN + "%d" % feeder + bcolors.ENDC
        print ""

# Menu
def menu():
	os.system('clear')

	print "Welcome to army size calculator for Travian 4.4"
	print "Enter the type of army being built."
	print "For Anvil press 1"
	print "For Hammer press 2"
	atype = raw_input(">>")
	print ""
	
	print "Enter the number of days server is open."
	time = raw_input(">>")
	print ""

	print "Enter day troop building started"
	active = raw_input(">>")
	print ""

	print "Select race for army"
	print "Press 1 for Roman"
	print "Press 2 for Gaul"
	print "Press 3 for Teuton"
	race = raw_input(">>")
        print ""
        
        dactive = int(time) - int(active) #Days actively building troops
        return race, time, active, atype

# Select Anvil Race
def sel_anvil_race(tribe, time, active):
        rom = 1
        gaul = 2
        teut = 3
        
        if tribe == rom:
                print bcolors.OKBLUE + "Roman tribe selected." + bcolors.ENDC# User picked Roman
                print ""
                rom_anvil(time, active)
        elif tribe == gaul:
                print bcolors.OKYELLOW + "Gaul tribe selected." + bcolors.ENDC # User picked Gaul
                print ""
                gaul_anvil(time, active)
        elif tribe == teut:
                print bcolors.OKGREEN + "Teuton tribe selected." + bcolors.ENDC # User chose Teuton
                print ""
                teut_anvil(time, active)
        else:
                print bcolors.FAIL + "Valid race not selected." + bcolors.ENDC
                print ""

# Select Hammer Race
def sel_hammer_race(tribe, time, active):
        rom = 1
        gaul = 2
        teut = 3
        
        if tribe == rom:
                print bcolors.OKBLUE + "Roman tribe selected." + bcolors.ENDC# User picked Roman
                print ""
                rom_hammer(time, active)
        elif tribe == gaul:
                print bcolors.OKYELLOW + "Gaul tribe selected." + bcolors.ENDC # User picked Gaul
                print ""
                gaul_hammer(time, active)
        elif tribe == teut:
                print bcolors.OKGREEN + "Teuton tribe selected." + bcolors.ENDC # User chose Teuton
                print ""
                teut_rammer(time, active)
        else:
                print bcolors.FAIL + "Valid race not selected." + bcolors.ENDC
                print ""

                
race, servTime, servActive, type = menu()
if type == "1":
        sel_anvil_race(int(race), int(servTime), int(servActive))
elif type == "2":
        sel_hammer_race(int(race), int(servTime), int(servActive))
else:
        print "Did not select an army type"
