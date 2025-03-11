

### Quiz 2 at the end of this class

### this class is very important for assignments 3 and 4

# name = "adam" ## hardcoded
# name = input()   

# file= open('Class notes/data.txt',"r") ## r means read and this file path notation is for mac. For windows use Class notes\\data.txt
# name = file.read()

# print(name)

# file.close()


# file= open('Class notes/data.txt',"r")
# name = file.readline()
# print(name)
# name = file.readline()
# print(name)
# name = file.readline()
# print(name)
# name = file.readline() ####### there is a hidden \n at every line
# print(name)

# file= open('Class notes/data.txt',"r")
# for whateverAkaLine in file:
#     print(whateverAkaLine, end="")


## print() has a new line built into it, but the file lines also have a new line built into them. Use end = "" to alleviate this


# file= open('Class notes/data.txt',"r")
# listOfLines = file.readlines()
# for line in listOfLines:
#     print(line, end = "")


# file= open('Class notes/data.txt',"r")
# line = "literally put any value here, it's just to initialize it "
# while line != "":
#     line = file.readline()
#     print(line, end="")

# file= open('Class notes/data.txt',"r")
# text = file.read()
# print(text)



# file= open('numbers.txt','r')
# sum= 0
# for line in file:
#     sum = sum + int(line)    ## need to not count the \n in every line
# print(sum)

# outFile= open('sum.txt', 'w') # w means writing
# outFile.write(str(sum)   )   ## this tells us what to write into outFile
# outFile.close()




# def border(text):
#     print("["+text+"]")

# name = "   Kwiwi apple orange     "
# res = name
# border(res)


# res = name.lstrip()
# border(res)

# res = name.rstrip()
# border(res)


# # res = name.strip
# # border(res)


# name = name.strip()
# print(name)


# lst = name.split()

# print(len(lst))
# print(lst[1])


# name = "   Kwiwi, apple  orange     "
# lst=name.split(",")
# print(lst)

# name = "kiwi,apple,orange,a,s,d,f"
# lst = name.split(",",2)  # this means split only 2 commas. Any commas after that will not be split

# print(lst)

# lst = name.rsplit(",",2)   ### count it from the right instead of the left
# print(lst)

# def stripList(list):
#     clean = []
#     for item in list:
#         clean.append(item.strip())
#         return clean

# file = open('Class notes/food.txt', 'r')
# for line in file.readlines():
#     parts = line.split("&")
#     cleanParts = stripList(parts)
#     print(cleanParts)


##################

# read expenses in expenses.txt and collect total expenses per day in a list

def stripList(list):
    clean = []
    for item in list:
        clean.append(item.strip())
        return clean
    
def listToFloat():
    for 
    return intList


def getTotals(filename):
    totals = []
    expenses = open(filename,'r')
    for line in expenses:
        parts = line.split(',')
        cleanParts = stripList(parts)
        floatParts = listToFloat(cleanParts[1:])
        totals.append(sum(floatParts))

    return totals

print (getTotals('Class notes/expenses.txt'))
