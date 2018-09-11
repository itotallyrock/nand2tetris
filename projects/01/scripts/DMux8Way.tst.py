#!/usr/bin/python

fout = open("../DMux8Way.tst", 'w')
fout.write("load DMux8Way.hdl,\n")
fout.write("output-file DMux8Way.out,\n")
fout.write("compare-to DMux8Way.cmp,\n")
fout.write("output-list in%B3.1.3 sel%B3.3.3 a%B3.1.3 b%B3.1.3 c%B3.1.3 d%B3.1.3 e%B3.1.3 f%B3.1.3 g%B3.1.3 h%B3.1.3;\n\n")

ss = "set %s %s"

# 3-bit options
zero = "%B000"
zzone = "%B001"
zonez = "%B010"
zoneone = "%B011"
onezz = "%B100"
onezone = "%B101"
oneonez = "%B110"
oneoneone = "%B111"
choose = ""


for i in range(2):
    fout.write(ss%("in", i)+",\n")
    for j in range(8):
        if j == 0:
            choose = zero
        elif j == 1:
            choose = zzone
        elif j == 2:
            choose = zonez
        elif j == 3:
            choose = zoneone
        elif j == 4:
            choose = onezz
        elif j == 5:
            choose = onezone
        elif j == 6:
            choose = oneonez
        elif j == 7:
            choose = oneoneone
        fout.write(ss%("sel", choose)+",\n")
        fout.write("eval,\n")
        fout.write("output;\n\n")


fout.close()
