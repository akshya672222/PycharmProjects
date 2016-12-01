def get_coordinates(x, y, command, direc, xyaxis):
    ret_arr = []
    direction = direc
    a, b = x, y
    axis = xyaxis
    for i in range ( 0 , len ( command ) ):
        if len(command) == 1 and (command[i] == 'L' or command[i] == 'R'):
            ret_arr = [' YES ']
            return ret_arr
        elif len(command) == 1 and command[i] == 'G':
            ret_arr = [' NO ']
            return ret_arr
        else:
            if command[ i ] == 'G':
                if axis == '+y':
                    a , b = a , b + 1
                elif axis == '-y':
                    a , b = a , b - 1
                elif axis == '-x':
                    a , b = a - 1 , b
                else:
                    a , b = a + 1 , b
            elif command[ i ] == 'L':
                if direction == 'north':
                    direction = 'west'
                    axis = '-x'
                elif direction == 'south':
                    direction = 'east'
                    axis = '+x'
                elif direction == 'east':
                    direction = 'north'
                    axis = '+y'
                else:
                    direction = 'south'
                    axis = '-y'
            elif command[ i ] == 'R':
                if direction == 'north':
                    direction = 'east'
                    axis = '+x'
                elif direction == 'south':
                    direction = 'west'
                    axis = '-x'
                elif direction == 'east':
                    direction = 'south'
                    axis = '-y'
                else:
                    direction = 'north'
                    axis = '+y'
            else:
                ret_arr = [ 'NO' ]
                return ret_arr
    if len(ret_arr) == 0:
        ret_arr.append(a)
        ret_arr.append(b)
        ret_arr.append(direction)
        ret_arr.append(axis)
    return ret_arr



def run_robot(arr):
    num = arr[0]
    retrn_arr = []
    a, b = 0, 0
    direction = 'north'
    axis = '+y'
    for i in range(0, num):
        command = arr[i+1]
        if 1<= len(command) <= 2500:
            arr1 = get_coordinates(a, b, command, direction, axis)
            if len(arr1) > 1:
                arr2 = get_coordinates(arr1[0], arr1[1], command, arr1[2], arr1[3])
                arr3 = get_coordinates(arr2[0], arr2[1], command, arr2[2], arr2[3])
                arr4 = get_coordinates(arr3[0], arr3[1], command, arr3[2], arr3[3])
                arr5 = get_coordinates(arr4[0], arr4[1], command, arr4[2], arr4[3])
                if arr1[0] == arr5[0] and arr1[1] == arr5[1]:
                    retrn_arr.append('YES')
                else:
                    retrn_arr.append('NO')
            else:
                retrn_arr.extend(arr1)
        else:
            retrn_arr.append ( 'NO' )
    return retrn_arr



number_of_command = int(input('Enter number of commands: '))
if 1 <= number_of_command <= 10:
    command_arr = []
    command_arr.append(number_of_command)
    for i in range(0, number_of_command):
        command_arr.append(input('Command: '))
    for items in run_robot(command_arr):
        print(items)
else:
    print('ERROR: NUMBER OF COMMANDS ARE GREATER THAN FIXED AMOUNT.')
