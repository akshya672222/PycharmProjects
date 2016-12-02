n = int ( input ( ).strip ( ) )
div_list = [ ]
for i in range ( 1 , int ( (n / 2) ) + 1 ):
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
print(max(max_dict, key=max_dict.get))
