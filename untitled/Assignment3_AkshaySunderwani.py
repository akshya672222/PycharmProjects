def maxofthree(value1, value2, value3):
    if value1 > value2 and value1 > value3:
        return value1
    elif value2 > value1 and value2 > value3:
        return value2
    else:
        return value3


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
    try:
        a = float(value1)
        b = float(value2)
        c = float(value3)
        print("The maximum of", a, b, c, "is:", maxofthree(a, b, c))
        wanttocontinue()
    except ValueError:
        print("Please enter valid numeric values to compare.")
        starttheprogram()

starttheprogram()
