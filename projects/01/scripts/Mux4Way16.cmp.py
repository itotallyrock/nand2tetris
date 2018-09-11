#!/usr/bin/python

fout = open("../Mux4Way16.cmp", 'w')

fout.write("|          a           |          b           |          c           |          d           |  sel   |         out          |\n")


# Setting up test cases to use
zeroes = "0000000000000000"
ones = "1111111111111111"
alt_c = "1010101010101010"
alt_d = "0101010101010101"

# 2-bit options
zero = "00"
zone = "01"
onez = "10"
oneone = "11"

a = zeroes
b = ones
c = alt_c
d = alt_d
for i in range(4):
    if i == 0:
        sel = zero
    elif i == 1:
        sel = zone
    elif i == 2:
        sel = onez
    elif i == 3:
        sel = oneone
    if sel == zero:
        output = a
    elif sel == zone:
        output = b
    elif sel == onez:
        output = c
    elif sel == oneone:
        output = d
    table = "|   {a}   |   {b}   |   {c}   |   {d}   |   {sel}   |   {out}   |".format(a = a, b = b, c = c, d = d, sel = sel, out = output)
    fout.write(table+"\n")

fout.close()
