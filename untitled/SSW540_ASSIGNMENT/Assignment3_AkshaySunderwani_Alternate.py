import operator

def wanttocontinue():
    yesorno = input("Do you want to continue? Yes or No: ")
    if yesorno == "Yes" or yesorno == "yes" or yesorno == "YES":
        starttheprogram()
    elif yesorno == "No" or yesorno == "NO" or yesorno == "no":
        print("Thank you for using this program.")
        exit()
    else:
        print("Enter a valid keyword response.")
        wanttocontinue()


def starttheprogram():
    value1 = input("Enter first value: ")
    value2 = input("Enter second value: ")
    value3 = input("Enter Third value: ")
    listofvalues = [value1, value2, value3]
    index, value = max(enumerate(listofvalues), key=operator.itemgetter(1))
    print("The maximum of", value1, value2, value3, "is:", value,
          "and postition of this value is:", index)
    wanttocontinue()


starttheprogram()
