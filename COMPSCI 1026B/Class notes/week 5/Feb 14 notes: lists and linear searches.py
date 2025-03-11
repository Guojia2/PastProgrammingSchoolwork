
word = "hello"
numbers=[1,5,8,90] 
print(numbers[2])


numbers[1]=10 #reassigning a number in the list
print(numbers[1])




#numbers=[] #means 0. You can add values to this later 

#these are called lists. In other languages, sometimes called array.
#group of numbers accesssible at an index


things=[1,2,"sunday",True,4.6700] #lists can be heterogenous
print(things[0]) #referencing: using the value but not changing it



#remember: Indices start at 0\




print("after--->", numbers)
# word[0]= "j"  
# # strings in a list are immutable. This means that they cannot be changed or reassigned
# print(word)

# print(numbers[100]) #list index out of range. This is called a runtime error

print(numbers[-1]) #this prints the last part  in the list
print("length=",len(numbers))



marks=numbers
print("marks=",numbers)
print("numbers=",marks)


marks[0]= 100


print("marks=",numbers)
print("numbers=",marks)




#the danger here is that both numbers and marks now point toward the same place.
#this is called aliasing. One files now has two names. Assignments are the same thing.
#aliasing the wrong way can cause serious issues




#access list elements by index
for i in range(len(numbers)):
    print(numbers[i])

#this is an easier way to do it
for part in numbers:
    print(part)


#you can append lists using lists.append("value")

#you can insert using lists.insert("element")

# list.pop(element) will delete the index at a position i and 
# shift all other elements one spot over


# you can use == to check if two lists have the same number of elements, same elements, and same order of elements





#value.sort() will sort the numbers in ascending order


#you can copy a list. prices=list(values). Different from aliasing.


#you can slice a list using temperature=temperatures[6:9].
# or (:9) to go from 0th to 8th element
# First number is inclusive, last is exclusive. ALWAYS.

##########common list algorithms:
# 


#let's try filling a list of 0,10,20,30...500
# #
numbers=[]
for i in range(0,51):
    numbers.append(i*10)
print(numbers)




#convert a string into a list of characters

text= "I need to get money"

arr=[]
for ltr in text:
    arr.append(ltr)
print(text)
print(arr)


newText=""
for ch in arr:     # this combines the list back into a string
    newText+=ch
print(newText)




##print elements separated by a delimiter
# 1,2,3,4,  the comma is a delimiter

friends= ["Harry", "Emily", "bob","Adam","Emily"]
combined=""
for name in friends:
    combined+=","+name

combined=combined[1:]

print(combined)





# print the max number that is a multiple of 5 within a list

arr=[1,0,4,9,10,-1,-5,5,50,6,1,15,99]
#assume the max is at index=0
max=arr[0]
for n in arr:
    if n%5==0 and n>max:
        max=n
print("the max is",max)


##print how many numbers in a list
arr=["1","nana","4","^","r","3"]
count=0
for part in arr:
    if part.isdigit():
        count=count+1
print("there are this many numbers in the list:",count)



# ############    LINEAR SEARCH


#finding the first value in a list that is greater than 100


values= [1,222,5,6,-4,200,9,99]
foundAt=0
isFound=False

while foundAt<len(values)  and not isFound:
    if values[foundAt]>100:
     isFound=True
    else:
     foundAt=foundAt+1
if isFound:
    print("Found at position",foundAt)
else:
    print("Not Found")

## Collect the names that start with a vowel and are shorter than 6 characters






names= ["Harry", "Emma", "bob","Adam","Emily", "Sunday"]

collected=[]

for name in names:
    if name[0] in "aeiouoAEIOU" and len(name)<6:
        collected.append(name)
        
print(collected)

### collect the position of all positive numbers from 10 random numbers
#between [-5,5]




from random import *
numbers=[]
for i in range(10):
    numbers.append(randint(-5,5))
positions=[]
for index in range(10):
    if numbers[index]>0:
        positions.append(index)

print("numbers are", numbers)
print("we found positive nums at:", positions)



##remove all strings of length <4 from a list

words= ["Harry", "Emma", "bob","Adam","Emily", "Sunday"]

print("before-->>",words)
while i<len(words):

    for word in words:
        word=words[i]
        if len(word)<4:
            words.pop(i)
        else:
            i= i+1
print("after--->", words)



# assume that you need a



