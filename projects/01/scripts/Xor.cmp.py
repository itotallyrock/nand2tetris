#!/usr/bin/python

fout = open("../Xor.cmp", 'w')

fout.write("|   a   |   b   |  out  |\n")



for i in range(2):
    for j in range(2):
        a = i
        b = j
        if a == 0 and b == 0:
            out = 0
        elif a == 1 and b == 1:
            out = 0
        else:
            out = 1
        table = "|   {a}   |   {b}   |   {out}   |\n".format(a = a, b = b, out = out)
        fout.write(table)

fout.close()
