import sys
import string

h = [int(h_temp) for h_temp in input().strip().split(' ')]
alpha_d = dict ( zip ( string.ascii_lowercase , h ) )
word = str(input().strip())
int_max = 0
for i in range(0, len(word)):
    if int_max < alpha_d[word[i]]:
        int_max = alpha_d[word[i]]
print(int_max*len(word)*1)
