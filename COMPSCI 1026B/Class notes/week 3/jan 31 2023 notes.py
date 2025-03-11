# Quiz 1 starts at 6 pm


# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

# # can also be expressed as

# counter = 10  # this line makes the counter start at 10
# while counter <= 30:
#     print("hello")
#     counter = counter+1  # this line makes the counter go up bny 1 each loop
# #counters can be made to count down with a - sign


###################


#print the letters of a word, each in a separate line

# word=("laptop")
      
# i=0      #i means index and is the same as counter
# last_i=len(word)-1   #remember we start at 0 and lapotp has 6 letters
# while i <=last_i:
#     print(word[i])
#     i+=1    #this line can also be written as i=i+1


#############

#let's print the time table of 8


# i=1
# while i<=10:
#     i+=1
#     print("8*%d=%d"%(i,i*8))   #remember, % means take the specified variable and place it here


##############

#Let's print the sum of all numbers from 1 to 150



# i=1
# sum=0
# while i<151:
#      sum=sum+i
#      i+=1
# print("avg=",sum/150)

#Now make it possible for a user to input a number "n"


# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print("average=", sum/n)



###let the user enter number n, and then let the user enter all n numbers and print their sum


# n=int(input("enter the number of grades:"))
# sum=0
# i=0
# while i<n:
#     grade=float(input("grade="))
#     sum= sum+grade
#     i+=1
# print("sum=",sum)



#########
###ask the user for 5 numbers, and then print only the positive ones
# i=1
# n=5
# while i<=n:
#     grade=float(input("grade="))
#     if grade>0:
#         print(grade)
#     i+=1


##Ask the user to enter grades until they enter -1, and then print only the positive ones, otherwise print "invalid input"




# grade= float(input("grade="))
# while grade!=-1:    #this means "is not equal to"
#     if grade>=0:
#         print(grade, "is positive")
#     else:
#         print(grade, "invalid input")
#     grade= float(input("grade="))




# word="laptop"
# for c in word:
#     print(c)    #c means first letter or something like that



#now let's try skipping the letter e

# word=""
# for c in word:
#     if c!="e":
#         print(c)

#now let's count the number of e in the word


# word="antelope"
# i=0
# j=0
# for c in word:
#     if c=="e":
#         i=i+1    #this means "add one to the counter"
#     if c=="p":
#         j=j+1

# print("%d e in this word"%i)
# print("%d p in this word"%j)


######## print the numbers 1-10 using loop like 1,3,5

for num in range(1,11,2):    #the first number is inclusive, the second number is exclusive.
    if num%2==1:
         print(num)              #the third number is the increment















