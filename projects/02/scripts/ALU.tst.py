#!/usr/bin/python

# File Setup

fout = open("../ALU.tst", 'w')

fout.write("""
load ALU.hdl,
output-file ALU.out,
compare-to ALU.cmp,
output-list x%B3.16.3 y%B3.16.3 zx%B3.1.3 nx%B3.1.3 zy%B3.1.3 ny%B3.1.3 f%B3.1.3 no%B3.1.3 out%B3.16.3 zr%B3.1.3 ng%B3.1.3;

// Used these 6 cases because there were over 256 possibilities

""")

#Test Cases
zero = "0000000000000000"
one = "1111111111111111"
alt_a = "1010101010101010"
alt_b = "0101010101010101"
half_a = "1111111100000000"
half_b = "0000000011111111"



for i in range(10):
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
    elif i == 5:
        a = alt_a
        b = one
    elif i == 6:
        a = half_a
        b = half_b
    elif i == 7:
        a = half_a
        b = zero
    elif i == 8:
        a = half_a
        b = one
    else:
        a = half_a
        b = alt_b
    fout.write("""
set x %B{a},
set y %B{b},
""".format(a = a, b = b))

    for zx in range(2):
        fout.write("set zx {zx},\n".format(zx = zx))
        for nx in range(2):
            fout.write("set nx {nx},\n".format(nx = nx))
            for zy in range(2):
                fout.write("set zy {zy},\n".format(zy = zy))
                for ny in range(2):
                    fout.write("set ny {ny},\n".format(ny = ny))
                    for f in range(2):
                        fout.write("set f {f},\n".format(f = f))
                        for no in range(2):
                            fout.write("set no {no},".format(no = no))
                            fout.write("""
eval,
output;

""")



fout.close()
