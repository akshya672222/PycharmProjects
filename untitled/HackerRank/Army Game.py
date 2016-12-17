import math

# def get_no_of_supplies(n , m):
#     if n == m:
#         if n % 2:
#             x = n / 2
#             total = x * x
#             return total
#         else:
#             if n == 1:
#                 return 1
#             else:
#                 x = n - 1
#                 y = x / 2
#                 y_sq = y * y
#                 total = n * n
#                 remain_sq = x * x
#                 remainder = total - remain_sq
#                 num_of_twos = remainder // 2
#                 remains = remainder % 2
#                 return y_sq + num_of_twos + remains
#     else:
#         if n % 2 == 0 and m % 2 == 0:
#             mult = n * m
#             total = mult / 4
#             return total
#         elif n % 2 != 0 and m % 2 != 0:
#             x = n - 1
#             y = m - 1
#             mult = x * y
#             mult_total = n * m
#             num_of_fours = mult / 4
#             remainer = mult_total - mult
#             num_of_twos = remainer // 2
#             remains = remainer % 2
#             return num_of_fours + num_of_twos + remains
#         else:
#             if n % 2 == 0:
#                 x = m - 1
#                 mult_x_n = x * n
#             else:
#                 x = n - 1
#                 mult_x_n = x * m
#             mult_n_m = n * m
#             num_of_fours = mult_x_n / 4
#             remaining = mult_n_m - mult_x_n
#             num_of_twos = remaining / 2
#             total = num_of_fours + num_of_twos
#             return total


n = int ( input ( 'N: ' ) )
m = int ( input ( 'M: ' ) )
# print ( get_no_of_supplies ( n , m ) )
print(int(math.ceil(n/2)*math.ceil(m/2)))
