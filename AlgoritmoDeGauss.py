k = input()
for i in range(0, k):
    a = input()
    a -= 1
    aux = a
    b = 2
    p = 0
    bi = []
    pi = []
    o = 1
    q = 1
    while(a != 1):
        if(a % b == 0):
            p += 1
            a /= b
            if(a % b != 0):
                print b, p
                bi.append(b)
                pi.append(p)
                p = 0
        else:
            while(True):
                b += 1
                for i in range(2,b):
                    if(b % i == 0):
                        continue
                break
    for i in range(0, len(bi)):
        t = 2
        while((t ** (aux/bi[i])) % (aux + 1) == 1):
            t += 1
        h = (t ** (aux /(bi[i] ** pi[i]))) % (aux + 1)
        print bi[i], t, h
        q = (q * h) % (aux + 1)
    print q
    print "---"
