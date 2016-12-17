import math

n = int ( input ( ).strip ( ) )
div_list = [ ]
for i in range ( 1 , int(math.ceil(n / 2) + 1)):
    if n % i == 0:
        div_list.append ( i )
div_list.append ( n )
max_dict = {}
for items in div_list:
    total = 0
    item_string = str ( items )
    for i in range ( 0 , len ( item_string ) ):
        item_int = int ( item_string[ i ] )
        total += item_int
    max_dict[ item_string ] = total
max_value = max(max_dict.values())
min_v = 0
for items in max_dict.keys():
    if max_dict[items] == max_value:
        min_v = items
        if min_v > items:
            min_v = items
print(min_v)
