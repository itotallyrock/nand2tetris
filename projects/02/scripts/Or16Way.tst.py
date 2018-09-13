#!/usr/bin/python

# File Setup

fout = open("../Or16Way.tst", 'w')

fout.write("""
load Or16Way.hdl,
output-file Or16Way.out,
compare-to Or16Way.cmp,
output-list in%B3.16.3 out%B3.1.3;

// Used these 4 cases because there were over 256 possibilities

""")

#Test Cases
zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"



for i in range(4):
    if i == 0:
        en = zero
    elif i == 1:
        en = one
    elif i == 2:
        en = alt_a
    else:
        en = alt_b
    fout.write("""
set in %B{en},
eval,
output;

""".format(en = en))



fout.close()
