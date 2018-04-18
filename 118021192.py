n = input()
numbers = list()
greaterCounter = 0
counter = 0
cNumber = 0
for i in range(1, n+1):
    cNumber = i
    for j in range(1, cNumber+1):
        if cNumber % j == 0:
            counter += 1   
    if counter > greaterCounter:
        numbers.append(i)
        greaterCounter = counter
    counter = 0
print numbers
