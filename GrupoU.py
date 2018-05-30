k = input()
for i in range(0, k):
    n = input()
    U = []
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
    print "---"
                
            
