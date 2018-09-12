#!/usr/bin/python

#setting up files

fout = open("../HalfAdder.cmp", 'w')

fout.write("|   a   |   b   |  sum  | carry |\n")

for i in range(2):
    for j in range(2):
        a = i
        b = j
        if (a == 0 and b == 0) or (a == 1 and b == 1):
            sume = 0
        else:
            sume = 1
        carry = a and b

        table = "|   {a}   |   {b}   |   {sume}   |   {carry}   |\n".format(a = a, b = b, sume = sume, carry = carry)
        fout.write(table)



fout.close()
