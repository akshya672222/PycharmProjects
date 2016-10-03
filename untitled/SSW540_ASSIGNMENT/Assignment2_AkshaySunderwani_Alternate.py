# Program to calculate grades on basis of user input of score


# method to ask user grade from input method
def askuserforgrade():
    # calling of method to calculate grade on depending of input marks.
    gradescalculated = calculategradefor(input("Enter score between 0 to 100 in order to calculate grades : "))
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


# method defination for calculating grades from input score
def calculategradefor(user_score):
    # Return the user's grade based on the following table.
    # Score  | Grade
    # -------+------
    # >= 93 | A
    # 90 <= | A-
    # 87 <= | B+
    # 83 <= | B
    # 80 <= | B-
    # 70 <= | C
    # <70   | F

    # try for handling non interger values from input as input always return string value and its needed to type cast
    # to int, and a non int value in string coverted to int throws exception.
    try:
        score = float(user_score)
        if score > 100 or score < 0:
            return "Please enter a number between 0 to 100."
        elif score >= 93:
            return "Grade for your score is : A"
        elif score >= 90:
            return "Grade for your score is : A-"
        elif score >= 87:
            return "Grade for your score is : B+"
        elif score >= 83:
            return "Grade for your score is : B"
        elif score >= 80:
            return "Grade for your score is : B-"
        elif score >= 70:
            return "Grade for your score is : C"
        else:
            return "Grade for your score is : F"
    except ValueError:
        # to handle non int value exception.
        return "Please enter a numeric value."


# calling of initial method to start grade calculation
askuserforgrade()
