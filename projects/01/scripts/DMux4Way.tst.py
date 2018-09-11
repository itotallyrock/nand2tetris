#!/usr/bin/python

fout = open("../DMux4Way.tst", 'w')
fout.write("load DMux4Way.hdl,\n")
fout.write("output-file DMux4Way.out,\n")
fout.write("compare-to DMux4Way.cmp,\n")
fout.write("output-list in%B3.1.3 sel%B3.2.3 a%B3.1.3 b%B3.1.3 c%B3.1.3 d%B3.1.3;\n\n")

ss = "set %s %s"

# 2-bit options
zero = "%B00"
zone = "%B01"
onez = "%B10"
oneone = "%B11"
choose = ""


for i in range(2):
    fout.write(ss%("in", i)+",\n")
    for j in range(4):
        if j == 0:
            choose = zero
        elif j == 1:
            choose = zone
        elif j == 2:
            choose = onez
        elif j == 3:
            choose = oneone
        fout.write(ss%("sel", choose)+",\n")
        fout.write("eval,\n")
        fout.write("output;\n\n")


fout.close()
