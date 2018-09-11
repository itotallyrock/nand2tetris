#!/usr/bin/python

fout = open("../Not16.cmp", 'w')

fout.write("|          in          |         out          |\n")


zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"

# Setting up test cases to use

for i in range(4):
    out = ""
    if i == 0:
        en = zero
    elif i == 1:
        en = one
    elif i == 2:
        en = alt_a
    else:
        en = alt_b

    for j in range(16):
        out1 = int(en[j])
        if out1 == 0:
            out += "1"
        else:
            out += "0"

    table = "|   {en}   |   {out}   |\n".format(en = en, out = out)
    fout.write(table)

fout.close()
