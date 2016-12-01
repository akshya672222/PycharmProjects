def perform_commands(arr):
    n = arr[0]
    stack = []
    top_element = []
    for i in range(0, n):
        stack_list = arr[i+1].split()
        if stack_list[0] == 'push':
            stack.append(int(stack_list[1]))
            top_element.append(stack[-1])
        elif stack_list[0] == 'pop':
            if len(stack) == 0:
                top_element.append('ERROR: STACK EMPTY.')
            else:
                stack.__delitem__(-1)
                if len(stack) == 0:
                    top_element.append ( 'EMPTY' )
                else:
                    top_element.append(stack[-1])
        elif stack_list[0] == 'inc':
            index = int(stack_list[1])
            value = int(stack_list[2])
            if index <= len(stack):
                for i in range(0, index):
                    stack[i] = stack[i] + value
                top_element.append(stack[-1])
            else:
                top_element.append('ERROR: INDEX OUT OF RANGE.')
        else:
            top_element.append('ERROR: INVALID COMMAND.')
    return top_element


n_commands = int(input('Enter no of commands: '))
i = 0
command_list = []
command_list.append(n_commands)
while i < n_commands:
    command_list.append(input('Command: '))
    i = i + 1
for items in perform_commands(command_list):
    print(items)
