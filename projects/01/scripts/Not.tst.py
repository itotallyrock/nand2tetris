#!/usr/bin/python

# File Setup

fout = open("../Not.tst", 'w')

fout.write("""
load Not.hdl,
output-file Not.out,
compare-to Not.cmp,
output-list in%B3.1.3 out%B3.1.3;

""")

for i in range(2):
    fout.write("set in {i},".format(i = i))
    fout.write("""
eval,
output;

""")



fout.close()
