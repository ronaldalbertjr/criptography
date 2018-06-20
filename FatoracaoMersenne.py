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

k = input()
for i in range(0, k):
    p = input()
    m = (2 ** p) - 1
    x = 1
    composto = False
    print m
    r = int(((2.0 ** (p/2.0)) - 1)/(2.0 * p))
    print r
    while (x <= r):
        q = 1 + (2 * x * p)
        print x
        resultado = potModular(2, p, q)
        if(resultado == 1):
            composto = True
            print q
            break
        x += 1
    if(not composto):
        print m
    print "---"
                
        
        
