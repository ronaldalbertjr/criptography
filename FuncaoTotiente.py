k = input()
for i in range(0, k):
    a = input()
    b = 2
    p = 0
    bi = []
    pi = []
    o = 1
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
    for q in range(0, len(bi)):
        o *= (bi[q]**(pi[q]-1))*(bi[q] - 1)
    print o
    print "---"
