n = input()
for i in range(0, n):
    a = input()
    r = a
    b = 2
    p = 0
    bs = []
    while(a != 1):
        if(a % b == 0):
            p += 1
            a /= b
            if(a % b != 0):
                print b, p
                bs.append(b);
                p = 0
        else:
            while(True):
                b += 1
                for i in range(2,b):
                    if(b % i == 0):
                        continue
                break
    if(len(bs) <= 1):
        print "NAO"
    else:
        for i in range(0, len(bs)):
            if(r % (bs[i]**2) == 0 or (r-1) % (bs[i]-1) != 0):
                print "NAO"
                break
            elif(i == len(bs)-1):
                print "SIM"  
    print "---"
