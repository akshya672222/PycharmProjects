def split(str):
    return list ( str )


str = split ( input ( ) )
out = [ ]
temp = [ ]
for i in range ( len ( str ) ):
    if i > 0 and str[ i ] != str[ i - 1 ]:
        out.append ( temp )
        temp = [ str[ i ] ]
    else:
        temp.append ( str[ i ] )
    if i == len ( str ) - 1:
        # temp.append(str[i])
        out.append ( temp )
count = 0
for i in range ( len ( out ) ):
    if i > 0:
        if len ( out[ i ] ) <= len ( out[ i - 1 ] ):
            count += len ( out[ i ] )
        else:
            count += len ( out[ i - 1 ] )
print ( count )
