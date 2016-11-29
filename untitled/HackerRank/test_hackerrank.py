n = int(input('enter height'))
i = 0
while i < n:
    j = n
    k = 0
    x = ''
    while j > i + 1:
        x += ' '
        j = j - 1
    while k <= i:
        x += '#'
        k = k + 1
    print(x)
    i = i + 1
