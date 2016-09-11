print("Start coding with python!")  # my first line in python
print("Second line in python")
print("Third line with numeric value", 1, 2, 3, 4, 1.2, 1.22)  # data types in python and how to print them

message1 = "Hello, I am Akshay and my age is :"
number1 = 23
message2 = "I was born in year :"
number2 = 1993.23

print(message1, number1)
print(message2, number2)
print("Type of variable message1 is :", type(message1))
print("Type of variable number1 is :", type(number1))
print("Type of variable message2 is :", type(message2))
print("Type of variable number2 is :", type(number2))

newVariable = number1 + number2

print("result of sum is :", newVariable)

___newVariable_2 = 2234
# naming in python is case sensitive, name can only be start from alphabet, number or underscore (_) and
# can only be followed by the same no special character is allowed.

print("new variable starting with underscore (_) :", ___newVariable_2)

# index number in python can be both positive and negative

newlist1 = [1, ",Hello in list,", 3, 4, 5, 6]  # list, lists are mutable, can be considered as mutable array of ios
                                               # lists are decelared using [] brackets

newtupple1 = (1, 2, 3, 4, 5, 6)  # tupple, tupple are immutable version of lists, can be considered as immutable array
                                 # of ios, accessed in same way as of lists, also tupple is decelared using () brackets

newset1 = {1, 2, 3, 4, 5, 6}  # set or dictionaries, dictionaries are decelared using {} brackets and work on key value
                              # approach instead of indexes similar to ios, we can use any type of unique key value in
                              # dictionaries which is not available in list or tupple

newdict2 = {"key1" : "value1", "key2" : "value2", "key3" : "value3", "key4" : "value4"}

newdict1 = {"key" : "value1", "set" : newset1, "tupple" : newtupple1, "list" : newlist1, "dictionary" : newdict2}

sample1 = 'string value with single qoute,'
sample2 = "string value with two qoutes,"
sample3 = """string value with triple qoutes,
hello this is new line in triple qoutes
this is third line in same triple qoutes,"""
sample4 = '''string value with 2nd type of triple qoutes,'''
# with help of triple qoutes one can enter multi line string

newlist2 = [sample1, sample2, sample3, sample4]

print("value for string sample value :", newlist2[1], "and its type is :", type(newlist2[1]))

sample5 = "Akshay"

# positive index and its value in string
print("value at 0 = ", sample5[0], 'value at 1 = ', sample5[1], "value at 2 = ", sample5[2], 'value at 3 = ',
      sample5[3], "value at 4 = ", sample5[4], 'value at 5 = ', sample5[5])

# negative index and its value in string
print("value at -1 = ", sample5[-1], 'value at -2 = ', sample5[-2], "value at -3 = ", sample5[-3], 'value at -4 = ',
      sample5[-4], "value at -5 = ", sample5[-5], 'value at -6= ', sample5[-6])

# positive and negatice index and its value in string
print("value at 0 = ", sample5[0], 'value at 1 = ', sample5[1], "value at 2 = ", sample5[2], 'value at 3 = ',
      sample5[3], "value at 4 = ", sample5[4], 'value at 5 = ', sample5[5], "value at -1 = ", sample5[-1],
      'value at -2 = ', sample5[-2], "value at -3 = ", sample5[-3], 'value at -4 = ', sample5[-4],
      "value at -5 = ", sample5[-5], 'value at -6= ', sample5[-6])

print("value in new list is : ", newlist1[1], "and its type is : ", type(newlist1))
print("value in new tupple is : ", newtupple1, "and its type is : ", type(newtupple1))
print("value in new set is : ", newset1, "and its type is : ", type(newset1))

print("list values before mutating list : ", newlist1)

newlist1[1] = ",this value is after mutating list,"

newlist1[2] = [1, 2, 3, 4]

print('list from list is : ', newlist1[2])

newlist1.append("new addition")
# append is used to insert value at last index in the list

newlist1.insert(2,"new additon in list before position 2")
# insert is used to insert value at user intended index in the list

print("value in new list after mutating is : ", newlist1, "and its type is : ", type(newlist1))

newlist1.pop(len(newlist1)-1)
# pop is used to remove object at intended index from the list

newlist1.__delitem__(0)
# __delitem__ works similar to pop

# newlist1.remove("dadadad")
# remove is used to remove particular object from the list, the object must be present in the list

newlist_copy = newlist1.copy()

newlist1.clear()
# deletes all items from list at once

print("value in new list after mutating is : ", newlist_copy, "and its type is : ", type(newlist_copy))

print("value in new dictionary is ", newdict1, ", and its type is : ", type(newdict1))

print("value of dictionary according to key list is : ", newdict1["list"], "and type is : ", type(newdict1["list"]))
print("value of dictionary according to key set is : ", newdict1["set"], "and type is : ", type(newdict1["set"]))
print("value of dictionary according to key tupple is : ", newdict1["tupple"], "and type is : ",
      type(newdict1["tupple"]))
print("value of dictionary according to key key1 is : ", newdict1["key"], "and type is : ", type(newdict1["key"]))
print("value of dictionary according to key dictionary is : ", newdict1["dictionary"], "and type is : ",
      type(newdict1["dictionary"]))

print("all keys in a dictionary are : ",newdict1.keys())
print("all values in a dictionary are : ",newdict1.values())
print("length of dictionary : ",len(newdict1))

# newtupple1[1] = "try to mutate tupple"
#
# print("tupple value after mutating : ",newtupple1)
