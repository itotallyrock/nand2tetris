#!/usr/bin/python

# File Setup

fout = open("../Xor.tst", 'w')

fout.write("""
load Xor.hdl,
output-file Xor.out,
compare-to Xor.cmp,
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
