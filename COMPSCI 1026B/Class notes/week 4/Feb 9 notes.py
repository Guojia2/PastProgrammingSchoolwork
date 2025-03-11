# name="bob"


# def bonus(mark):
#     mark = mark + 11
#     global name
#     print(name)
#     x=1
#     print("mark inside the function=",mark)

# def main():
#     mark=9
#     print(mark)
#     y=9
#     print("mark before calling the function= ",mark)
#     bonus(mark)
#     print("mark after calling the function= ",mark)

# main()


##################################################################################################
##################################################################################################
##################################################################################################
# Write a program that asks the user to enter a name. The program should check the following conditions first:
# - The name should be from 5 to 15 characters long
# - The name should start with the title Dr. or Mr. and ends with a period.
# - The name should consist of first and last name
# If any of the above conditions is not satisfied, the program should print an appropriate message and exit.
# The program then prints:
# - the initials of the name
# - The first name and last name separately

def isTwoPartsName(name):
    isValid = True
    if name.count(" ") != 1:
        isValid = False
    return isValid


def isValidLength(name):
    isValid = False
    if 5 <= len(name) <= 15:
        isValid = True
    return isValid


def isStartWithTitle(name):
    isValid = True
    if not name.startswith("Dr.") and not name.startswith("Mr."):
        isValid = False
    if not name.endswith("."):
        isValid = False
    return isValid


def getInitials(name):
    per = name.find('.')
    space = name.find(' ')
    return (name[per+1]+"."+name[space+1]).upper()


def getFirstName(name):
    per = name.find('.')
    space = name.find(' ')
    fname = ""
    for i in range(per+1, space+1):
        fname += name[i]
    return fname


def getLastName(name):
    last = len(name)
    space = name.find(' ')
    lname = ""
    for i in range(space+1, last-1):
        lname += name[i]
    return lname


def main():
    name = input("Please enter your full name:")
    if isStartWithTitle(name) == False:
        print("the name should start with a title and ends with a period.")
        return
    if not isValidLength(name):
        print("Please enter a name between 5 and 15 chars.")
        return
    if not isTwoPartsName(name):
        print("Please enter first and last name.")
        return

    print("Initials:", getInitials(name))
    print("First Name:", getFirstName(name))
    print("Last Name:", getLastName(name))


main()

##################################################################################################
##################################################################################################
##################################################################################################
# Turns a number into its English name.


def intName(number):
    part = number   # The part that still needs to be converted.
    name = ""   # The name of the number.
    if part >= 100:
        name = digitName(part // 100) + " hundred"
        part = part % 100
    if part >= 20:
        name = name + " " + tensName(part)
        part = part % 10
    elif part >= 10:
        name = name + " " + teenName(part)
        part = 0

    if part > 0:
        name = name + " " + digitName(part)
    return name

# Turns a digit into its English name.\n


def digitName(digit):
    if digit == 1:
        return "one"
    if digit == 2:
        return "two"
    if digit == 3:
        return "three"
    if digit == 4:
        return "four"
    if digit == 5:
        return "five"
    if digit == 6:
        return "six"
    if digit == 7:
        return "seven"
    if digit == 8:
        return "eight"
    if digit == 9:
        return "nine"
    return ""

# Gives the name of the tens part of a number between 20 and 99.


def tensName(number):
    if number >= 90:
        return "ninety"
    if number >= 80:
        return "eighty"
    if number >= 70:
        return "seventy"
    if number >= 60:
        return "sixty"
    if number >= 50:
        return "fifty"
    if number >= 40:
        return "forty"
    if number >= 30:
        return "thirty"
    if number >= 20:
        return "twenty"
    return ""

# Turns a number between 10 and 19 into its English name.


def teenName(number):
    if number == 10:
        return "ten"
    if number == 11:
        return "eleven"
    if number == 12:
        return "twelve"
    if number == 13:
        return "thirteen"
    if number == 14:
        return "fourteen"
    if number == 15:
        return "fifteen"
    if number == 16:
        return "sixteen"
    if number == 17:
        return "seventeen"
    if number == 18:
        return "eighteen"
    if number == 19:
        return "nineteen"
    return ""


print(intName(234))


