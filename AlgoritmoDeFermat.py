import math

n = input()
for i in range(0,n):
    n = input()
    x = int (math.floor(math.sqrt(n)))
    y = 0
    while(n != (x*x) - (y*y)):
        print x, y, 'N'
        x += 1
        y = int (math.floor(math.sqrt((x*x) - n)))
    print x, y, 'S'
    print (x - y), (x + y)
    print "---"

            
