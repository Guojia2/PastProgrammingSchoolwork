



#Write a program that asks the user to enter ten unique numbers. The program must add each number to a list if they aren’t already contained in the list. When the list contains ten unique numbers, the program displays the contents of the list and quits.

# list = []

# while len(list) < 10:
#     number = int(input("Please add ten unique numbers"))
#     if list.__contains__(number):
#         print("please enter a unique number") 
#     elif number not in list:
#         list.append(number)
# print(list)





#Write a program that returns the number of strings where the first and last character in a string are the same, 
# and the length of the string is 2 or longer. 

#For example, if this is the list you use, ['bgh', wer, yuy, 1661] 
# the output should be 2 because the last 2 elements are longer than 1 char, and start and end with the same char. 

#Hint: If you have a string such as word = “abc”, you can use word[-1] to access the last element in the string.



#For example, if this is the list you use, ['bgh','wer','yuy','1661'] 
#bgh, wer, yuy, '1661'
# List = ['bgh','wer','yuy','1661'] 
# # inputList = input("ENTER A LIST OF STRINGS")
# # for item in inputList:
# #      List.append(item)
# counter= 0
# for string in List:
#     if len(string)>=2 and string [0] == string[-1]: 
#           counter = counter +1
# print (counter)





# def zFirst(words):
#     zresult = []
#     result = []
#     for word in words:
#         if word.lower()[0] =='z':
#             zresult.append(word)
#         else:
#             result.append(word)
#     zresult.sort()
#     result.sort()
#     return zresult+ result

# words= ["hello", "good", "nice", "as", "at", "baseball", "absorb", "sword", "a","tall", "so", "bored", "silver", "hi%", "pool", "we", "am", "seven", "do", "you", "want" , "ants", "because", "that's",
# "how", "you", "get", "zebra", "zealot", "zoo", "xylophone", "asparagus"]

# print(zFirst(words))



values = [1,2,3,4,5]
newValues = values  ## this sets both lists to be the same, so any changes will be copied
for i in range(len (values)+1): ## the +1 means that the first value in the list will not be affected
    values[i] +=1  ## 
print("Old Value at index {} is: {} ".format (i, newValues [i])) 
print("New Value at index {} is: {} \n". format (i, newValues [i]))  ## these two lines cant both use newValues

values = [1,2,3,4,5]
newValues = list(values)
for i in range (len(values)):
    newValues[i] +=1
    print("Old Value at index {} is: {} ".format (i, values [i])) 
    print("New Value at index {} is: {} \n". format (i, newValues [i]))