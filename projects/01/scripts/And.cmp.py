#!/usr/bin/python

fout = open("And.cmp", 'w')

fout.write("|   a   |   b   |  out  |\n")

table = "|   %d   |   %d   |   %d   |\n"

for i in range(2):
    for j in range(2):
        a = i
        b = j
        out = a and j
        fout.write(table%(a, b, out))


fout.close()
