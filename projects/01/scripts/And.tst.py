#!/usr/bin/python

fout = open("../And.tst", 'w')
fout.write("load And.hdl,\n")
fout.write("output-file And.out,\n")
fout.write("compare-to And.cmp,\n")
fout.write("output-list a%B3.1.3 b%B3.1.3 out%B3.1.3;\n\n")

ss = "set %c %d"

for i in range(2):
    for j in range(2):
        fout.write(eval%('a', i)+",\n")
        fout.write(eval%('b', j)+",\n")
        fout.write("eval,\n")
        fout.write("output;\n\n")


fout.close()
