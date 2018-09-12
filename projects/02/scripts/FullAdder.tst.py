#!/usr/bin/python

# File Setup

fout = open("../FullAdder.tst", 'w')

fout.write("""
load FullAdder.hdl,
output-file FullAdder.out,
compare-to FullAdder.cmp,
output-list a%B3.1.3 b%B3.1.3 c%B3.1.3 sum%B3.1.3 carry%B3.1.3;

""")

for i in range(2):
    fout.write("set a {i},\n".format(i = i))
    for j in range(2):
        fout.write("set b {j},".format(j = j))
        for k in range(2):
            fout.write("""
set c {k},
eval,
output;

""".format(k = k))



fout.close()
