#!/usr/bin/python

#setting up files

fout = open("../Inc16.cmp", 'w')

fout.write("|          in          |         out          |\n")

#Test Cases
zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1100110100111101"
alt_b = "0101010101010101"

for i in range(4):
    if i == 0:
        en = zero
    elif i == 1:
        en = one
    elif i == 2:
        en = alt_a
    else:
        en = alt_b
    out = list(en)
    for j in range(15, -1, -1):
        if out[j] == "0":
            out[j] = "1"
            break;
        elif out[j] == "1":
            out[j] = "0"
    out = "".join(out)
    table = "|   {en}   |   {out}   |\n".format(en = en, out = out)
    fout.write(table)



fout.close()
