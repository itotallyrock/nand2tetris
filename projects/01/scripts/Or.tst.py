#!/usr/bin/python

# File Setup

fout = open("../Or.tst", 'w')

fout.write("""
load Or.hdl,
output-file Or.out,
compare-to Or.cmp,
output-list a%B3.1.3 b%B3.1.3 out%B3.1.3;

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
