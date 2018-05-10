n = input()
for i in range(0, n):
    r = 1
    a,e,n = input()
    e %= (n-1)
    print e
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
    print "---"
