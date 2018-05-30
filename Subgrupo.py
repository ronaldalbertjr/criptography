def MDC(a, b):
    aux = 0
    while(b!=0):
        aux = b
        b = a % b
        a = aux
    return a

n = input()
for i in range(0, n):
    q, c = input()
    U = []
    error = False
    for j in range(1, q):
            a = q
            b = j
            aux = 0
            while(b != 0):
                aux = b
                b = a % b
                a = aux
            if(a == 1):
                U.append(j);
    if 1 not in c:
        error = True
    else:
        for j in range(0, len(c)):
            if (c[j] not in U) or not (MDC(c[j], q) ==  1):
                error = True
            for k in range(0, len(c)):
                if (c[j] * c[k]) % q not in c:
                    error = True
                    break
            if error:
                break
    if error:
        print "NAO"
    else:
        print "SIM"
    print "---"
