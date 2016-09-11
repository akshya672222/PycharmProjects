# index number in python can be both positive and negative

newlist1 = [1, ",Hello in list,", 3, 4, 5, 6]  # list, lists are mutable, can be considered as mutable array of ios
                                               # lists are decelared using [] brackets

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

print("no of variable is list are : ",newlist1.count([1, 2, 3, 4]))
# pop is used to remove object at intended index from the list

newlist1.__delitem__(0)
# __delitem__ works similar to pop

# newlist1.remove("dadadad")
# remove is used to remove particular object from the list, the object must be present in the list

newlist_copy = newlist1.copy()

newlist_copy.reverse()

newlist1.clear()
# deletes all items from list at once

print("value in new list after mutating is : ", newlist_copy, "and its type is : ", type(newlist_copy))
