#!/usr/bin/python

fout = open("../DMux.cmp", 'w')

fout.write("|  in   |  sel  |   a   |   b   |\n")

table = "|   %d   |   %d   |   %d   |   %d   |\n"

for i in range(2):
    for j in range(2):
        en = i
        sel= j
        if sel == 0:
            a = en
            b = 0
        else:
            a = 0
            b = en
        fout.write(table%(en, sel, a, b))


fout.close()
