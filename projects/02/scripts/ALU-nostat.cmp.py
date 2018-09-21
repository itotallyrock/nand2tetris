#!/usr/bin/python

#defining functions
def add16(x, y):
    out = ""
    if (int(x[15]) == 0 and int(y[15]) == 0) or (int(x[15]) == 1 and int(y[15]) == 1):
        sume = 0
    else:
        sume = 1
    carryx = int(x[15])
    carryy = int(y[15])
    if carryx == 1 and carryy == 1:
        carry = 1
    else:
        carry = 0
    out += str(sume)
    for j in range(15, 0, -1):
        if (int(x[j-1]) == 0 and int(y[j-1]) == 0) or (int(x[j-1]) == 1 and int(y[j-1]) == 1):
            o = 0
        else:
            o = 1

        if (o == 0 and carry == 0) or (o == 1 and carry == 1):
            sume = 0
        else:
            sume = 1
        carry1 = int(x[j-1]) and int(y[j-1])
        carry2 = o and carry
        carry = carry1 or carry2
        out += str(sume)
    out = out[::-1]
    return out

def zerox(x):
    x = "0000000000000000"
    return x

def negatex(x):
    x = list(x)
    for i in range(16):
        if x[i] == "0":
            x[i] = "1"
        else:
            x[i] = "0"
    x = "".join(x)
    return x

def zeroy(y):
    y = "0000000000000000"
    return y

def negatey(y):
    y = list(y)
    for i in range(16):
        if y[i] == "0":
            y[i] = "1"
        else:
            y[i] = "0"
    y = "".join(y)
    return y

def anding(x,y):
    out = ""
    for i in range(16):
        tempx = int(x[i])
        tempy = int(y[i])
        if tempx == 1 and tempy == 1:
            temp = 1
        else:
            temp = 0
        out += str(temp)
    return out

def negateout(out):
    out = list(out)
    for i in range(16):
        if out[i] == "0":
            out[i] = "1"
        else:
            out[i] = "0"
    out = "".join(out)
    return out


#setting up files

fout = open("../ALU-nostat.cmp", 'w')

fout.write("|          x           |          y           |  zx   |  nx   |  zy   |  ny   |   f   |  no   |         out          |\n")

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

    x = a
    y = b
    snx = 0
    szy = 0

    for zx in range(2):
        if zx == 1:
            snx = 0
            szy = 0
            y = b
            x = zerox(x)
        for nx in range(2):
            if nx == 1:
                if snx == 0:
                    if zx == 1:
                        y = b
                    else:
                        x = a
                        y = b
                    snx = 1
                x = negatex(x)
                if zx == 1:
                    y = b
                    szy = 0
            for zy in range(2):
                if zy == 1:
                    if szy == 0:
                        if zx == 1 or nx == 1:
                            y = b
                        else:
                            x = a
                            y = b
                        szy = 1
                    y = zeroy(y)
                for ny in range(2):
                    if ny == 1:
                        y = negatey(y)
                    for f in range(2):
                        if f == 1:
                            out = add16(x,y)
                            for no in range(2):
                                if no == 1:
                                    out = negateout(out)
                                table = "|   {x}   |   {y}   |   {zx}   |   {nx}   |   {zy}   |   {ny}   |   {f}   |   {no}   |   {out}   |\n".format(x = a, y = b, zx = zx, nx = nx, zy = zy, ny = ny, f = f, no = no, out = out)
                                fout.write(table)
                        else:
                            out = anding(x,y)
                            for no in range(2):
                                if no == 1:
                                    out = negateout(out)
                                table = "|   {x}   |   {y}   |   {zx}   |   {nx}   |   {zy}   |   {ny}   |   {f}   |   {no}   |   {out}   |\n".format(x = a, y = b, zx = zx, nx = nx, zy = zy, ny = ny, f = f, no = no, out = out)
                                fout.write(table)






fout.close()
