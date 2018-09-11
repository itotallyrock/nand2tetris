#!/usr/bin/python

fout = open("../Mux.tst", 'w')
fout.write("load Mux.hdl,\n")
fout.write("output-file Mux.out,\n")
fout.write("compare-to Mux.cmp,\n")
fout.write("output-list a%B3.1.3 b%B3.1.3 sel%B3.1.3 out%B3.1.3;\n\n")

ss = "set %s %d"

for i in range(2):
    for j in range(2):
        for k in range(2):
            fout.write(ss%("a", i)+",\n")
            fout.write(ss%("b", j)+",\n")
            fout.write(ss%("sel", k)+",\n")
            fout.write("eval,\n")
            fout.write("output;\n\n")


fout.close()
