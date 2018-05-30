n = input()
for i in range(0, n):
    v, m = input()
    aMod = m[0]
    r = v[0]
    for i in range(0, len(m) - 1):
        a,b = aMod, m[i+1]
        aux,x2,x1,y2,y0,q = (0,)*6
        x0,y1 = (1,)*2
        print a,'-',x0,y0
        print b,'-',x1,y1
        while(b != 0):
            q = a/b
            aux = b
            b = a % b
            a = aux
            x2 = x0 - (x1 * q)
            y2 = y0 - (y1 * q)
            x0 = x1
            x1 = x2
            y0 = y1
            y1 = y2
            if(b == 0):
                print b,q,"- -"
            else:
                print b,q,x2,y2
        print x0, y0
        r = ((r * y0 * m[i+1]) + (v[i+1] * x0 * aMod)) % (m[i+1]*aMod) 
        aMod *= m[i+1]
        print r, aMod
    print "---"
