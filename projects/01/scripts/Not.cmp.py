#!/usr/bin/python

fout = open("../Not.cmp", 'w')

fout.write("|  in   |  out  |\n")



for i in range(2):
    en = i
    if en == 0:
        out = 1
    else:
        out = 0
    table = "|   {en}   |   {out}   |\n".format(en = en, out = out)
    fout.write(table)

fout.close()
