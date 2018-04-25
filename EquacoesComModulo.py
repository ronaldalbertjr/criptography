n = input()
for i in range(0, n):
    a,b,n = input()
    s = (a + b) % n 
    u = (a - b) % n 
    v = (a * b) % n
    a %= n
    b %= n
    print a, b, s, u, v
    print "---"
