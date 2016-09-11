# Program to calculate grades on basis of user input of score


# method to ask user grade from input method
def askuserforgrade():
    # calling of method to calculate grade on depending of input marks.
    gradescalculated = getgrades(input("Enter score between 0 to 100 in order to calculate grades : "))
    #    gradescalculated = calculategradefor(input("Enter score between 0 to 100 in order to calculate grades : "))

    print(gradescalculated)
    # if statement to check last return statement and handle program accordingly to continue.
    if gradescalculated == "Grade for your score is : A" \
            or gradescalculated == "Grade for your score is : A-" \
            or gradescalculated == "Grade for your score is : B+" \
            or gradescalculated == "Grade for your score is : B" \
            or gradescalculated == "Grade for your score is : B-" \
            or gradescalculated == "Grade for your score is : C" \
            or gradescalculated == "Grade for your score is : F":
        # call method to ask if user wants to calculate more grades.
        askuserifwanttocalculatemoregrades()
    else:
        askuserforgrade()


# method to ask if user wants to calculate more grades or exit.
def askuserifwanttocalculatemoregrades():
    userrespone = input("Do you want to calculate more grades? Yes or No : ")
    # if statement to check user response to continue or not.
    if userrespone == "Yes" or userrespone == "yes" or userrespone == "YES":
        askuserforgrade()
    elif userrespone == "No" or userrespone == "NO" or userrespone == "no":
        print("Thank you for using this program.")
        exit()
    else:
        print("Enter a valid keyword response.")
        askuserifwanttocalculatemoregrades()


def getgrades(score):
    try:
        score = float(score)
        grades = [(100, 'Grade for your score is : A'), (93, 'Grade for your score is : A-'),
                  (90, 'Grade for your score is : B+'), (87, 'Grade for your score is : B'),
                  (83, 'Grade for your score is : B-'), (80, 'Grade for your score is : C'),
                  (70, 'Grade for your score is : F'), (0, 'Please enter a number between 0 to 100.')]
        for i in range(len(grades) - 1):
            if grades[i][0] >= score >= grades[i + 1][0]:
                return grades[i][1]
        return "Please enter a number between 0 to 100."
    except ValueError:
        return "Please enter a numeric value."


# calling of initial method to start grade calculation
askuserforgrade()
