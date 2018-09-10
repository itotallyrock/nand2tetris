#!/usr/bin/python

# File Setup

fout = open("../And16.tst", 'w')

fout.write("""
load And16.hdl,
output-file And16.out,
compare-to And16.cmp,
output-list a%B3.16.3 b%B3.16.3 out%B3.16.3;

// Used these six test cases because it there were over 256 possiblities

""")
# Test Cases

zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"


for i in range(6):
    if i == 0:
        change_a = zero
        change_b = zero
    elif i == 1:
        change_a = one
        change_b = one
    elif i == 2:
        change_a = one
        change_b = zero
    elif i == 3:
        change_a = alt_a
        change_b = alt_b
    elif i == 4:
        change_a = alt_a
        change_b = zero
    elif i == 5:
        change_a = alt_a
        change_b = one
    fout.write("""
set a %B{ca},
set b %B{cb},
eval,
output;

    """.format(ca = change_a, cb = change_b))

fout.close()
