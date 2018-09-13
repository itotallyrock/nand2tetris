#!/usr/bin/python

# File Setup

fout = open("../Or8Way.tst", 'w')

fout.write("""
load Or8Way.hdl,
output-file Or8Way.out,
compare-to Or8Way.cmp,
output-list in%B3.8.3 out%B3.1.3;

// Used these four test cases because it there were 256 possibilities

""")
# Test Cases

zero = "00000000"
one = "11111111"
alt_a = "10101010"
alt_b = "01010101"



for i in range(4):
    if i == 0:
        en = zero
    elif i == 1:
        en = one
    elif i == 2:
        en = alt_a
    elif i == 3:
        en = alt_b

    fout.write("""
set in %B{en},
eval,
output;

""".format(en = en))



fout.close()
