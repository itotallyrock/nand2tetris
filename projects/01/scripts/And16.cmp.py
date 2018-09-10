#!/usr/bin/python

fout = open("../And16.cmp", 'w')

fout.write("|          a           |          b           |         out          |\n")


zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"

# Setting up test cases to use

for i in range(6):
    output = ""
    if i == 0:
        change_a = zero
        change_b = zero
    elif i == 1:
        change_a = one
        change_b = one
    elif i == 2:
        change_a = one
        change_b = zero
    elif i == 3:
        change_a = alt_a
        change_b = alt_b
    elif i == 4:
        change_a = alt_a
        change_b = zero
    elif i == 5:
        change_a = alt_a
        change_b = one
    for j in range(16):
        output_num = int(change_a[j]) and int(change_b[j])
        output += str(output_num)
    table = "|   {ca}   |   {cb}   |   {out}   |\n".format(ca = change_a, cb = change_b, out = output)
    fout.write(table)

fout.close()
