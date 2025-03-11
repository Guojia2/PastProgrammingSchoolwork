




# dictionary = {}

# even = set()
# for i in range (21):
#     if i%2 == 0:
#         even.add(i)

# odd = set()
# for i in range (21):
#     if i%2 != 0:
#         odd.add(i)

# threeMultiples = set()

# for i in range (21):
#     if i%3 == 0:
#         threeMultiples.add(i)


# dictionary =  {'even':even, "odd":odd,"threeMultiples":threeMultiples}
# print(dictionary)






# f = open("LABS/rawdata.txt", 'r')

# incomeDict = {}
# countryDict = {}

# countryList= []
# incomeList = []
# initialList = []

# for line in f:
#     line= line.upper().strip("\n").split(':')
#     initialList.append(line[1][0])
#     countryList.append(line[1])
#     incomeList.append(line[2])

# for i in range(0,len(countryList)):
#     incomeDict[countryList[i]] = incomeList[i]
#     if initialList[i] in countryDict:
#         countryDict[initialList[i]].add(countryList[i])
#     else:
#         countryDict[initialList[i]] = {countryList [i]}
# done = False
# while not done:
#     text = input ("Enter an initial or a country name: ")
#     text = text.upper
#     if text == "QUIT":
#         done= True
#     elif text in countryDict:
#         print(countryDict[text])
#     elif text in incomeDict:
#         print(incomeDict[text])
#     else: 
#         print("Does not exist.")


sentence ="I had such a horrible day It was awful so bad sigh It could not have been worse but actually though it was such a terrible horrible awful bad day"

makeItHappy ={"horrible":"amazing", "bad": "good", "awful": "awesome", "worse": "better"  , "terrible": "great"}


spsentence = sentence.split()
for word in range(0,len(spsentence)): # removed the -1
    if spsentence[word] in makeItHappy:  
       spsentence[word] = makeItHappy[spsentence[word]]  #now takes the element at the spot equal to the element present in list 'spsentence' at index 'word', instead of taking the element of 'makeitHappy" at index 'word'
newString= ""
for word in spsentence:
    newString = newString + word + " "


print(newString)





