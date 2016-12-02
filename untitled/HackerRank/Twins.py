import sys
x = input('n: ')

arr = x.split()
n = int(arr[0])
m = int(arr[1])

prime = []
for i in range(n, m+1):
    j = 2
    while j < int((i/2)+1):
        if i % j == 0:
            break
        j += 1
    if j == int((i/2)+1):
        prime.append(i)
prime.sort ( reverse=False )
count = 0
for i in range(0, len(prime)-1):
    for j in range(i+1, len(prime)):
        if abs(prime[j] - prime[i]) == 2:
            count += 1
print(count, file=sys.stdout)
