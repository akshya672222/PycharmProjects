import math
n = int(input(''))

# a.x + b.y = n

array = []
for i in range(0, math.ceil(n/2)):
    for j in range(0, math.ceil(n/4)):
        a = 1
        x = i + 1
        y = j + 1
        b = int((n - (a * x))/y)
        while a < b:
            if [a, b] not in array and int((a*x) + (b*y)) == n:
                array.append( [ a , b ] )
            a += 1
            b = int ( (n - (a * x)) / y )
print(len(array))
