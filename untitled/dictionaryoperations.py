newlist1 = [1, ",Hello in list,", 3, 4, 5, 6]  # list, lists are mutable, can be considered as mutable array of ios
                                               # lists are decelared using [] brackets

newtupple1 = (1, 2, 3, 4, 5, 6)  # tupple, tupple are immutable version of lists, can be considered as immutable array
                                 # of ios, accessed in same way as of lists, also tupple is decelared using () brackets

newset1 = {1, 2, 3, 4, 5, 6}  # set or dictionaries, dictionaries are decelared using {} brackets and work on key value
                              # approach instead of indexes similar to ios, we can use any type of unique key value in
                              # dictionaries which is not available in list or tupple

newdict2 = {"key1" : "value1", "key2" : "value2", "key3" : "value3", "key4" : "value4"}

newdict1 = {"key" : "value1", "set" : newset1, "tupple" : newtupple1, "list" : newlist1, "dictionary" : newdict2}

# print("value in new dictionary is ", newdict1, ", and its type is : ", type(newdict1))
# print("value of dictionary according to key list is : ", newdict1["list"], "and type is : ", type(newdict1["list"]))
# print("value of dictionary according to key set is : ", newdict1["set"], "and type is : ", type(newdict1["set"]))
# print("value of dictionary according to key tupple is : ", newdict1["tupple"], "and type is : ",
#       type(newdict1["tupple"]))
# print("value of dictionary according to key key1 is : ", newdict1["key"], "and type is : ", type(newdict1["key"]))
# print("value of dictionary according to key dictionary is : ", newdict1["dictionary"], "and type is : ",
#       type(newdict1["dictionary"]))

newdict_copy = newdict1.copy()

newdict_copy2 = newdict1.fromkeys(newdict1.keys(),1)

print("dictionary from keys before update :", newdict_copy2)

newdict_copy2.update(newdict_copy)

newdict_copy2.update({"check 1" : "new check"})

print("dictionary from keys :", newdict_copy2)

# newdict_copy.popitem()
# newdict_copy.popitem()
# newdict_copy.popitem()
# newdict_copy.popitem()
# newdict_copy.popitem()

newdict1.clear()

print("all keys in a dictionary are : ",newdict_copy2.keys())
print("all values in a dictionary are : ",newdict_copy2.values())
print("length of dictionary : ",len(newdict_copy2))
# print("items from dictionary = ",newdict_copy.items(), "items type : ",type(newdict_copy.items()))


str1 = 'hello string'
print("string before reverse === ", str1)
str2 = str1[::-1]

# [begin:end:step] for reversing of string
'''
hello this is a multi line comment

for -1 : [end:begin:step(-ve)]
for +1 : [begin:end:step(+ve)]

There is no issue if we increase the max +ve or decrease -ve value as it will always show one result that is its starting word either from begining or end depending on step value

[::-1] : output:
string before reverse ===  hello string
string after reverse ===  gnirts olleh

[0::-1] : output:
string before reverse ===  hello string
string after reverse ===  h

[1::-1] : output:
string before reverse ===  hello string
string after reverse ===  eh

[2::-1] : output:
string before reverse ===  hello string
string after reverse ===  leh

[2:0:-1] : output:
string before reverse ===  hello string
string after reverse ===  le

[2:1:-1] : output:
string before reverse ===  hello string
string after reverse ===  l

[::-2] : output:
string before reverse ===  hello string
string after reverse ===  git le

[::-3] : output:
string before reverse ===  hello string
string after reverse ===  gr l

[::0] : output: error: slice step cannot be zero

[::1] : output:
string before reverse ===  hello string
string after reverse ===  hello string

[::2] : output:
string before reverse ===  hello string
string after reverse ===  hlosrn

[1::2] : output:
string before reverse ===  hello string
string after reverse ===  el tig

[1:5:2] : output:
string before reverse ===  hello string
string after reverse ===  el

'''

print("string after reverse === ", str2)

str1, str2 = str2, str1

print("string 1 after swap === ", str1)

print("string 2 after swap === ", str2)
