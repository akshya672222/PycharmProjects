# n = int(input(''))
# for i in range(n):
#     a = str(input('')).lower()
#     b = str(input('')).lower()
#     if b in a:
#         print('YES')
#     else:
#         print('NO')

#python3
from collections import Counter

def checker(a, b):
    print('a:', a, 'b: ', b)
    if len(a) >= len(b):
        string_diff = Counter(a) - Counter(b)
        print('counter a : ', Counter(a), 'counter b: ', Counter(b), 'string diff: ', string_diff)
        upper_diff = Counter(a.upper()) - Counter(b)
        print('upper string diff: ', upper_diff)
        for letter in string_diff.keys():
            print('letter : ', letter)
            if letter.isupper():
                return "NO"
            if letter.upper() in upper_diff:
                a = a.replace(letter, "")
                print(a)
        if a.upper() != b:
            return "NO"
    return "YES"

num_queries = int(input())
for _ in range(num_queries):
    a = input()
    b = input()
    print(checker(a, b))


# 10
# Pi
# P
# YES
# AfPZN
# APZNC
# NO
# LDJAN
# LJJM
# NO
# UMKFW
# UMKFW
# YES
# KXzQ
# K
# NO
# LIT
# LIT
# YES
# QYCH
# QYCH
# YES
# DFIQG
# DFIQG
# YES
# sYOCa
# YOCN
# NO
# JHMWY
# HUVPW
# NO