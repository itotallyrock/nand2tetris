#!/usr/bin/python

# File Setup

fout = open("../Or16.tst", 'w')

fout.write("""
load Or16.hdl,
output-file Or16.out,
compare-to Or16.cmp,
output-list a%B3.16.3 b%B3.16.3 out%B3.16.3;

// Used these six test cases because it there were over 256 possibilities

""")
# Test Cases

zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"



for i in range(6):
    if i == 0:
        a = zero
        b = zero
    elif i == 1:
        a = one
        b = one
    elif i == 2:
        a = one
        b = zero
    elif i == 3:
        a = alt_a
        b = alt_b
    elif i == 4:
        a = alt_a
        b = zero
    else:
        a = alt_a
        b = one

    fout.write("""
set a %B{a},
set b %B{b},
eval,
output;

""".format(a = a, b = b))



fout.close()
