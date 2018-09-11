#!/usr/bin/python

fout = open("../DMux8Way.cmp", 'w')

fout.write("|  in   |   sel   |   a   |   b   |   c   |   d   |   e   |   f   |   g   |   h   |\n")

table = "|   %d   |   %s   |   %d   |   %d   |   %d   |   %d   |   %d   |   %d   |   %d   |   %d   |\n"


# 3-bit values
zero = "000"
zzone = "001"
zonez = "010"
zoneone = "011"
onezz = "100"
onezone = "101"
oneonez = "110"
oneoneone = "111"
sel = ""


for i in range(2):
    for j in range(8):
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        en = i
        if j == 0:
            sel = zero
        elif j == 1:
            sel = zzone
        elif j == 2:
            sel = zonez
        elif j == 3:
            sel = zoneone
        elif j == 4:
            sel = onezz
        elif j == 5:
            sel = onezone
        elif j == 6:
            sel = oneonez
        elif j == 7:
            sel = oneoneone
        if en == 1:
            if sel == zero:
                a = 1
            elif sel == zzone:
                b = 1
            elif sel == zonez:
                c = 1
            elif sel == zoneone:
                d = 1
            elif sel == onezz:
                e = 1
            elif sel == onezone:
                f = 1
            elif sel == oneonez:
                g = 1
            else:
                h = 1
        fout.write(table%(en, sel, a, b, c, d, e, f, g, h))


fout.close()
