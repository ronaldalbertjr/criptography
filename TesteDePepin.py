def potModular(a, e, n):
    r = 1
    c = 'S' if e % 2 != 0 else 'N'
    print r, a, e, c
    while(e != 0):
        if(e % 2 != 0):
            r = (r * a) % n
            e = (e - 1)/2
        else:
            e //= 2
        c = 'S' if e % 2 != 0 else 'N'
        a = (a*a) % n
        print r, a, e, c
    return r

n = input()
for i in range(0, n):
    k = input()
    F = (2 ** (2 ** k)) + 1
    e = (F - 1)/2
    print F
    r = potModular(5, e, F)
    if(r == F - 1):
        print "PRIMO"
    else:
        print "COMPOSTO"
    print "---"
