#!/usr/bin/python

#setting up files

fout = open("../Add16.cmp", 'w')

fout.write("|          a           |          b           |         out          |\n")

#Test Cases
zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"
carry = 0

for i in range(6):
    out = ""
    if i == 0:
        a = zero
        b = zero
    elif i == 1:
        a = one
        b = one
    elif i == 2:
        a = one
        b = zero
    elif i == 3:
        a = alt_a
        b = alt_b
    elif i == 4:
        a = alt_a
        b = zero
    else:
        a = alt_a
        b = one
    if (int(a[15]) == 0 and int(b[15]) == 0) or (int(a[15]) == 1 and int(b[15]) == 1):
        sume = 0
    else:
        sume = 1
    carry = int(a[15]) and int(b[15])
    out += str(sume)
    for j in range(15, 0, -1):
        if (int(a[j-1]) == 0 and int(b[j-1]) == 0) or (int(a[j-1]) == 1 and int(b[j-1]) == 1):
            o = 0
        else:
            o = 1

        if (o == 0 and carry == 0) or (o == 1 and carry == 1):
            sume = 0
        else:
            sume = 1
        carry1 = int(a[j-1]) and int(b[j-1])
        carry2 = o and carry
        carry = carry1 or carry2
        out += str(sume)
    out = out[::-1]


    table = "|   {a}   |   {b}   |   {out}   |\n".format(a = a, b = b, out = out)
    fout.write(table)




fout.close()
