#!/usr/bin/python

# File Setup

fout = open("../HalfAdder.tst", 'w')

fout.write("""
load HalfAdder.hdl,
output-file HalfAdder.out,
compare-to HalfAdder.cmp,
output-list a%B3.1.3 b%B3.1.3 sum%B3.1.3 carry%B3.1.3;

""")

for i in range(2):
    fout.write("set a {i},".format(i = i))
    for j in range(2):
        fout.write("""
set b {j},
eval,
output;

""".format(j = j))



fout.close()
