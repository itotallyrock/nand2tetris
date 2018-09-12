#!/usr/bin/python

#setting up files

fout = open("../FullAdder.cmp", 'w')

fout.write("|   a   |   b   |   c   |  sum  | carry |\n")

for i in range(2):
    for j in range(2):
        for k in range(2):
            a = i
            b = j
            c = k
            if (a == 0 and b == 0) or (a == 1 and b == 1):
                out = 0
            else:
                out = 1

            if (out == 0 and c == 0) or (out == 1 and c == 1):
                sume = 0
            else:
                sume = 1
            carry1 = a and b
            carry2 = out and c
            carry = carry1 or carry2

            table = "|   {a}   |   {b}   |   {c}   |   {sume}   |   {carry}   |\n".format(a = a, b = b, c = c, sume = sume, carry = carry)
            fout.write(table)



fout.close()
