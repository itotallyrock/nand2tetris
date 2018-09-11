#!/usr/bin/python

fout = open("../DMux4Way.cmp", 'w')

fout.write("|  in   |  sel   |   a   |   b   |   c   |   d   |\n")

table = "|   %d   |   %s   |   %d   |   %d   |   %d   |   %d   |\n"


# 2-bit values
zero = "00"
zone = "01"
onez = "10"
oneone = "11"
sel = ""


for i in range(2):
    for j in range(4):
        a = 0
        b = 0
        c = 0
        d = 0
        en = i
        if j == 0:
            sel = zero
        elif j == 1:
            sel = zone
        elif j == 2:
            sel = onez
        elif j == 3:
            sel = oneone
        if en == 1:
            if sel == zero:
                a = 1
            elif sel == zone:
                b = 1
            elif sel == onez:
                c = 1
            else:
                d = 1
        fout.write(table%(en, sel, a, b, c, d))


fout.close()
