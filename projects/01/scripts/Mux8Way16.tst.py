#!/usr/bin/python

# File Setup

fout = open("../Mux8Way16.tst", 'w')

fout.write("""
load Mux8Way16.hdl,
output-file Mux8Way16.out,
compare-to Mux8Way16.cmp,
output-list a%B3.16.3 b%B3.16.3  c%B3.16.3 d%B3.16.3 e%B3.16.3 f%B3.16.3 g%B3.16.3 h%B3.16.3 sel%B3.3.3 out%B3.16.3;

// Used these eight test cases because it there were over 256 possibilities

""")
# Test Cases

zeroes = "%B0000000000000000"
ones = "%B1111111111111111"
alt_c = "%B1010101010101010"
alt_d = "%B0101010101010101"
ee = "%B1001001001001001"
ff = "%B0010010010010010"
gee = "%B0000000011111111"
hh = "%B1111111100000000"

# 2-bit options
zero = "%B000"
zzone = "%B001"
zonez = "%B010"
zoneone = "%B011"
onezz = "%B100"
onezone = "%B101"
oneonez = "%B110"
oneoneone = "%B111"

fout.write("""
set a {z},
set b {o},
set c {altc},
set d {altd},
set e {ee},
set f {ff},
set g {gee},
set h {hh},""".format(z = zeroes, o = ones, altc = alt_c, altd = alt_d, ee = ee, ff = ff, gee = gee, hh = hh))
for i in range(8):
    if i == 0:
        sel = zero
    elif i == 1:
        sel = zzone
    elif i == 2:
        sel = zonez
    elif i == 3:
        sel = zoneone
    elif i == 4:
        sel = onezz
    elif i == 5:
        sel = onezone
    elif i == 6:
        sel = oneonez
    else:
        sel = oneoneone
    fout.write("""
set sel {s},
eval,
output;
    """.format(s = sel))



fout.close()
