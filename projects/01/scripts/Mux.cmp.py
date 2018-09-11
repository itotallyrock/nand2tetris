#!/usr/bin/python

fout = open("../Mux.cmp", 'w')

fout.write("|   a   |   b   |  sel  |  out  |\n")

table = "|   %d   |   %d   |   %d   |   %d   |\n"

for i in range(2):
    for j in range(2):
        for k in range(2):
            a = i
            b = j
            sel = k
            if sel == 0:
                out = a
            else:
                out = b
            fout.write(table%(a, b, sel, out))


fout.close()
