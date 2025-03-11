#### TODAY WE DO MORE EXAMPLES OF LOOPS

###print the numbers from 0 to 10 all in one line

# for i in range (11):  #same as writing (0,11) because ranges start at 0 by default
#     print(i, end="-")  ###this will make it print in one line because it has end=/n by default
    

# for i in range (3):        #outer for
#     for j in range (6,9):  #inner for
#         print(i,j)         #once this line executed, we return to the inner for

#you will need a pen and paper and draw out a table of values to understand this
#it prints i,j for every j in range (6,9) and then does that again for every i in  range (3)






###### Now let's print a 3x3 square of symbols 

# symbol=input("symbol:")
# for rowNum in range (3):
#     for colNum in range(3):
#         print (symbol, end="")
#     print()

### get the price per person for 3 dishes and then print the price per 2, 4,... 10 ppl for each dish

# for i in range (3):
#     price=int(input("price per person:"))
#     for j in range (2,11,2):
#         print ("price for %d people = $%d" %(j,j*price))  #the , between the j and j*price denotes different %d values



### now let's reverse a string

# string= input("pplease input word here")    
# lastInx= len(string)-1
# for idx in range (lastInx,-1,-1):     # setting the increment to -1 makes it go backwards
#     print(string[idx], end="")




# ## print the percentage of vowels and spaces ina  sentance entered by user

# sentence=input("type your sentence here").lower()
# vowelCount=sCount=0
# total=len(sentence)
# for ltr in sentence:  #ltr means letter
#     if ltr in "aeiou":
#         vowelCount +=1
#     if ltr in " ":
#         sCount+=1
# print ("vowel percentage is %d%%"%(vowelCount/total*100))
# print("space percentage is %d%%"%(sCount/total*100))


### print the index of each character in a sentence


# sent= "the jgoisfjoig7888f of ech number lmao"

# for index in range (len(sent)):
#     if sent[index].isdigit():
#         print ("found a number at ",index)

#### find the position/index of the firs tuppercase letter in a string

# string="oijgiowjiogjrewoihTjndgUIYTHNIgng"
# isFoundYet=False
# idx=0
# while not isFoundYet and idx<=len(string):
#     if string[idx].isupper():
#         isFoundYet=True
#     else:
#         idx+=1

# if isFoundYet==True:
#     print("found first upper at %d"%(idx))



######  extend a word by spaces. The user enters te nuber of spaces until they enter a nunmber. Then use need to enter the word.


# numSpaces=input("Number of spaces")
# while not numSpaces.isdigit():
#     print("This is not a number, bruh!")
#     numSpaces=input("Number of Spaces")
# numSpaces=int(numSpaces)
# word=input("Etner the word:")

# for ltr in word:
#     print(ltr + " "*numSpaces,end="")



from random import*
x=random()
print(x)

y=randint(2,5)  #alll inclusive

print(y)




