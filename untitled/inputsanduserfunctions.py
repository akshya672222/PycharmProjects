# input functions
import random
import sys
import os

print("Hello start work on input functions...")

# name = input("Please, enter your name : ")
# # input always returns the string type value, we have to type cast the value as required.
# age = input("Please, enter your age : ")
# email = input("Please, enter your email address : ")
# hobbies = input("Please, enter your hobbies : ")
#
# wanttoshowinfo = input("Do you want to see your information back? Yes or no.")

# if wanttoshowinfo = "Yes"
#     print("Name = ", name, end="", "Age = ", age, end="", "Email = ", email, end="", "Hobbies = ", hobbies, end="")
# else
#     print("You have choosen not to see information.", end="", "Thank you.")

print("Hello ", input("Please enter your first name : "), input("Please enter your last name : "))

number1 = int(input("enter number 1 : "))
'''
when user tries to enter any other value apart from interger exception is generated
ValueError: invalid literal for int() with base 10: 'a'
'''
number2 = int(input("enter number 2 : "))
number3 = float(input("enter number 3 : "))

sumofstrings = number1 + number2 + number3
'''
When try to add string value with string values
sumofstrings = number1 + number2 + number3
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
# + operator on string concat the attached strings
print("sum of number = ", number1+number2)
print("sub of number = ", number1-number2)
print("multiplication of number = ", number1*number2)
print("div of number = ", number1/number2)
print("modulus of number = ", number1%number2)
print("exponent of number = ", number1**number2)
print("floor division of number = ", number1//number2)
