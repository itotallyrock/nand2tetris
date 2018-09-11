#!/usr/bin/python

fout = open("../Mux8Way16.cmp", 'w')

fout.write("|          a           |          b           |          c           |          d           |          e           |          f           |          g           |          h           |   sel   |         out          |\n")


# Setting up test cases to use
zeroes = "0000000000000000"
ones = "1111111111111111"
alt_c = "1010101010101010"
alt_d = "0101010101010101"
ee = "1001001001001001"
ff = "0010010010010010"
gee = "0000000011111111"
hh = "1111111100000000"

# 2-bit options
zero = "000"
zzone = "001"
zonez = "010"
zoneone = "011"
onezz = "100"
onezone = "101"
oneonez = "110"
oneoneone = "111"

a = zeroes
b = ones
c = alt_c
d = alt_d
e = ee
f = ff
g = gee
h = hh
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
    if sel == zero:
        output = a
    elif sel == zzone:
        output = b
    elif sel == zonez:
        output = c
    elif sel == zoneone:
        output = d
    elif sel == onezz:
        output = e
    elif sel == onezone:
        output = f
    elif sel == oneonez:
        output = g
    else:
        output = h
    table = "|   {a}   |   {b}   |   {c}   |   {d}   |   {e}   |   {f}   |   {g}   |   {h}   |   {sel}   |   {out}   |".format(a = a, b = b, c = c, d = d, e = e, f = f, g = g, h = h, sel = sel, out = output)
    fout.write(table+"\n")

fout.close()
