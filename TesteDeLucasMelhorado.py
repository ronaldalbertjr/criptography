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
    a = input()
    a -= 1
    aux = a + 1
    b = 2
    p = 0
    bi = []
    pi = []
    nTest = []
    o = 1
    primo = False
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
    for j in range(2, aux):
        if(len(nTest) == len(bi)):
            print "PRIMO"
            primo = True
        if(primo):
            break
        print j
        print aux - 1
        r = potModular(j, aux - 1, aux)
        if(r % aux != 1):
            print "COMPOSTO"
            primo = True
            break
        for l in range(0, len(bi)):
            if((aux - 1)/bi[l] not in nTest):
                print (aux - 1)/bi[l]
                r = potModular(j, (aux - 1)/bi[l], aux)
                if(not (r % aux == 1)):
                    nTest.append((aux - 1)/bi[l])
    if(not primo):
        print "COMPOSTO"    
    print "---" 
