k = input()
for i in range(0, k):
    n = input()
    U = []
    s = []
    for j in range(1, n):
        a = n
        b = j
        aux = 0
        while(b != 0):
            aux = b
            b = a % b
            a = aux
        if(a == 1):
            U.append(j)
    print U
    for j in range(0, len(U)):
        s.append(U[j])
        aux = 2
        while(not ((U[j]**aux) % n == 1)):
            s.append((U[j] ** aux) % n)
            aux = aux + 1
            s.sort()
        print s
        s = [1]
    print "---"
