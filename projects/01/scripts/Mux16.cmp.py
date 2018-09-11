#!/usr/bin/python

fout = open("../Mux16.cmp", 'w')

fout.write("|          a           |          b           |  sel  |         out          |\n")


zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"

# Setting up test cases to use

for i in range(6):
    for j in range(2):
        sel = j
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
        elif i == 5:
            a = alt_a
            b = one
        if sel == 0:
            output = a
        else:
            output = b
        table = "|   {ca}   |   {cb}   |   {sel}   |   {out}   |\n".format(ca = a, cb = b, sel = j, out = output)
        fout.write(table)

fout.close()
