n = input()
for x in range(0, n):
    a, b = input()
    q = 0
    print q, a;
    while(a >= b):
        q += 1
        a -= b
        print q, a;
    print "---"
