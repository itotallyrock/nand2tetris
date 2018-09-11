#!/usr/bin/python

fout = open("../DMux.tst", 'w')
fout.write("load DMux.hdl,\n")
fout.write("output-file DMux.out,\n")
fout.write("compare-to DMux.cmp,\n")
fout.write("output-list in%B3.1.3 sel%B3.1.3 a%B3.1.3 b%B3.1.3;\n\n")

ss = "set %s %d"

for i in range(2):
    fout.write(ss%("in", i)+",\n")
    for j in range(2):
        fout.write(ss%("sel", j)+",\n")
        fout.write("eval,\n")
        fout.write("output;\n\n")


fout.close()
