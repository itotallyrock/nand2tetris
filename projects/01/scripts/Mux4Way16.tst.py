#!/usr/bin/python

# File Setup

fout = open("../Mux4Way16.tst", 'w')

fout.write("""
load Mux4Way16.hdl,
output-file Mux4Way16.out,
compare-to Mux4Way16.cmp,
output-list a%B3.16.3 b%B3.16.3  c%B3.16.3 d%B3.16.3 sel%B3.2.3 out%B3.16.3;

// Used these four test cases because it there were over 256 possibilities

""")
# Test Cases

zeroes = "%B0000000000000000"
ones = "%B1111111111111111"
alt_c = "%B1010101010101010"
alt_d = "%B0101010101010101"

# 2-bit options
zero = "%B00"
zone = "%B01"
onez = "%B10"
oneone = "%B11"

fout.write("""
set a {z},
set b {o},
set c {altc},
set d {altd},""".format(z = zeroes, o = ones, altc = alt_c, altd = alt_d))
for i in range(4):
    if i == 0:
        sel = zero
    elif i == 1:
        sel = zone
    elif i == 2:
        sel = onez
    else:
        sel = oneone
    fout.write("""
set sel {s},
eval,
output;
    """.format(s = sel))



fout.close()
