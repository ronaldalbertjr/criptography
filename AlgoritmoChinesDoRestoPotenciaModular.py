n = input()
for i in range(0, n):
    v, e, mod = input()
    a = mod
    b = [2]
    o = []
    j = 0
    p = 0
    while(a != 1):
        if(a % b[j] == 0):
            p += 1
            a /= b[j]
            if(a % b[j] != 0):
                print b[j], p
                p = 0
                b.append(b[j])
                j += 1
        else:
            while(True):
                b[j] += 1
                for i in range(2,b[j]):
                    if(b[j] % i == 0):
                        continue
                break
    for i in range(0, len(b) - 1):
        if(v % b[i] == 0):
            print 0
            o.append(0)
        else:
            k = 1
            r = e % (b[i] - 1)
            l = v
            print r
            c = 'S' if r % 2 != 0 else 'N'
            print k, l, r, c
            while(r != 0):
                if(r % 2 != 0):
                    k = (k * l) % b[i]
                    r = (r - 1)/2
                else:
                    r //= 2
                c = 'S' if r % 2 != 0 else 'N'
                l = (l*l) % b[i]
                print k, l, r, c
            o.append(k)
    aMod = b[0]
    r = o[0]
    for i in range(0, len(o) - 1):
        a,c = aMod, b[i+1]
        aux,x2,x1,y2,y0,q = (0,)*6
        x0,y1 = (1,)*2
        print a,'-',x0,y0
        print c,'-',x1,y1
        while(c != 0):
            q = a/c
            aux = c
            c = a % c
            a = aux
            x2 = x0 - (x1 * q)
            y2 = y0 - (y1 * q)
            x0 = x1
            x1 = x2
            y0 = y1
            y1 = y2
            if(c == 0):
                print c,q,"- -"
            else:
                print c,q,x2,y2
        print x0, y0
        r = ((r * y0 * b[i+1]) + (o[i+1] * x0 * aMod)) % (b[i+1]*aMod) 
        aMod *= b[i+1]
        print r, aMod
    print "---"
