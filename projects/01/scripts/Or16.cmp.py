#!/usr/bin/python

fout = open("../Or16.cmp", 'w')

fout.write("|          a           |          b           |         out          |\n")


zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"

# Setting up test cases to use

for i in range(6):
    out = ""
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

    for j in range(16):
        out1 = int(a[j]) or int(b[j])
        out += str(out1)

    table = "|   {a}   |   {b}   |   {out}   |\n".format(a = a, b = b, out = out)
    fout.write(table)

fout.close()
