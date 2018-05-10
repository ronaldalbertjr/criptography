t = input()
for i in range(0, t):
    n, b = input();
    bF = b;
    k = 1;
    q = (n - 1)/(2**k);
    r = 1;
    while(q % 2 == 0):
        k = k + 1;
        q = (n - 1)/(2**k);
    e = q
    print k, q;
    c = 'S' if q % 2 != 0 else 'N';
    print r, b, q, c;
    while(q != 0):
        if(q % 2 != 0):
            r = (r * b) % n;
            q = (q - 1)/2;
        else:
            q //= 2;
        c = 'S' if q % 2 != 0 else 'N';
        b = (b*b) % n;
        print r, b, q, c;
    print e, r;
    if(r == 1):
        print "INCONCLUSIVO";
        continue;
    for j in range(1, k):
        print ((2**j)*e), (bF**((2**j)*e)) % n;
        if(bF**((2**j)*e) % n == n-1):
            print "INCONCLUSIVO";
            break;
        if(j == k-1):
            print "COMPOSTO";
    print "---";