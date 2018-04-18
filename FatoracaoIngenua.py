n = input()
for i in range(0, n):
    a = input()
    b = 2
    p = 0
    while(a != 1):
        if(a % b == 0):
            p += 1
            a /= b
            if(a % b != 0):
                print b, p
                p = 0
        else:
            while(True):
                b += 1
                for i in range(2,b):
                    if(b % i == 0):
                        continue
                break
    print "---"
