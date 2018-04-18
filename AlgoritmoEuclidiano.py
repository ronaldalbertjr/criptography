n = input()
for x in range(0, n):
    a,b = input()
    aux = 0
    print a
    print b
    while(b!=0):
        aux = b
        b = a % b
        a = aux
        print b
    print "---"
        
