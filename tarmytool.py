# This tool helps calculate army build times for travian
# Version : .01 alpha
# Author : Juan A. Uribe
# Date : April 4, 2015

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

# Method to calculate roman anvil
def rom_anvil(time):
	psize = time * day / praet
	ecsize = time * day/ ec
	feeder = time/10
	print "Praets built in this time: %d" % psize
	print "EC built in this time : %d" % ecsize
	print "Total anvil size: %d with %d feeders" % (psize + 4*ecsize + feeder*fdef, feeder)
	print ""

def gaul_anvil(time):
	gsize = time*day/phal
	drusize = time*day/druid
	feeder = time/10
	print "Phalanx built in this time: %d" %gsize
	print "Druidriders built in this time: %d" % drusize
	print "Total anvil size: %d" % (gsize + 2*drusize + feeder * fdef)
	print ""

print "Roman anvil size after 60 days, at release of arti"
rom_anvil(60)

print "Roman anvil size after 100 days, 40 days after arti release"
rom_anvil(100)

print "Roman anvil size after 150 days, 110 days after arti release"
rom_anvil(150)

print "Gaul anvil size after 60 days, at release of arti"
gaul_anvil(60)

print "Gaul anvil size after 100 days, 40 days after arti release"
gaul_anvil(100)

print "Gaul anvil size after 150 days, 40 days after arti release"
gaul_anvil(150)
