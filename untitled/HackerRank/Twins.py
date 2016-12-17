import math

arr = input ( '' ).split ( )
n = int ( arr[ 0 ] )
m = int ( arr[ 1 ] )

a = 0
count = 0

full_list = list(range(n, m+1))

for p in range ( n , m + 1 ):
    for i in range ( 2 , math.ceil(p/2)+1 ):
        if p % i == 0:
            break
    else:
        if a == 0:
            a = p
        else:
            if abs ( p - a ) == 2:
                count += 1
            a = p
print ( count )


