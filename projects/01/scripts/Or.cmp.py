#!/usr/bin/python

fout = open("../Or.cmp", 'w')

fout.write("|   a   |   b   |  out  |\n")



for i in range(2):
    for j in range(2):
        a = i
        b = j
        out = i or j
        table = "|   {a}   |   {b}   |   {out}   |\n".format(a = a, b = b, out = out)
        fout.write(table)

fout.close()
