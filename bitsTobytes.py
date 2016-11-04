def bitsToBytes(a):
    s = i = 0
    for x in a:
        s += s + x
        i += 1
        if i == 8:
            yield s
            s = i = 0
    if i > 0:
        yield s << (8 - i)

lst = [0,0,0,0,0,0,1,1]

for b in bitsToBytes(iter(lst)):
    print b
