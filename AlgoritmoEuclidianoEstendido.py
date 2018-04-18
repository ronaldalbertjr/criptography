n = input()
for x in range(0, n):
    a,b = input()
    aux,x2,x1,y2,y0,q = (0,)*6
    x0,y1 = (1,)*2
    print a,'-',x0,y0
    print b,'-',x1,y1
    while(b != 0):
        q = a/b
        aux = b
        b = a % b
        a = aux
        x2 = x0 - (x1 * q)
        y2 = y0 - (y1 * q)
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
        if(b == 0):
            print b,q,"- -"
        else:
            print b,q,x2,y2
    print "---"

