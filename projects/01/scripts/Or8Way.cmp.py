#!/usr/bin/python

fout = open("../Or8Way.cmp", 'w')

fout.write("|      in      |  out  |\n")


zero = "00000000"
one = "11111111"
alt_a = "10101010"
alt_b = "01010101"

# Setting up test cases to use

for i in range(4):
    if i == 0:
        en = zero
    elif i == 1:
        en = one
    elif i == 2:
        en = alt_a
    elif i == 3:
        en = alt_b

    for j in range(8):
        if en[j] == '1':
            out = 1
            break;
        else:
            out = 0

    table = "|   {en}   |   {out}   |\n".format(en = en, out = out)
    fout.write(table)

fout.close()
