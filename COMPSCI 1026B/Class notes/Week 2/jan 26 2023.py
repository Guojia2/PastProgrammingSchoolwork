
# wealth=str(input("are you rich or poor?"))



# if wealth =="rich":
#     print("welcome to the Lexington Hotel")
# else:
#     print ("get out of here hobo")



############ 

#Boolean vartiables and operators


# a="hi" #string
# a=3 #integer
# a=2.3 #float

# a=True #boolean integers. Not the same as a="true" or a="false" which are strings
# a=False

# age=int(input("age"))
# a=age>5

# if a:
#     print("yes")
# else:
#     print("no")




#Let's give a vaccine to kids aged 5 or 6 or [12 to 15]

#Let's let every number greater than 0 be expressed as 1

# 1+1 = 1
# 1+1+1 = 1
# 0+1=1
# 0+0=1


# age=int(input("please enter your age") )
# if age==5 or age==6 or age>=12 and age<=15:
#     print("eligible")
# else:
#     print("not eligible)



# age=int(input("please enter your age") )
# if age==5 or age==6 or age>=12 and age<=15:
#     print("eligible")
#     age=13
# else:
#     print("not eligible")
          
# if False or False or True and True: #0 +0+1*1
#     print("eligible")

#false means 0 and true means 1

#short circuit evaluation: if the statement "x and y" and x is false, we dont need to check y. If "x or y" and x is true, we dont need to check y.

#Analyzing strings like s.upper and s.lower
name= "John Wayne"
if "Way" in name:
    print("way found")
else:
    print("not found")
if name.endswith("ne"):
    print ("ne found")
else:
    print("ne not found")


if name.startswith("joh"):
    print("joh found")
else:
    print("joh not found")




age=input("age")
if age.isdigit():
    age=int(age)
    print(age)
else:
    print("please enter a numerical value")



age.isalnum
age.isalpha   #these are all various methods of testing strings
age.isdecimal
age.isupper
age.count



print(name.count("jo"))
#this will count the umber of times "jo" appears in name


print(name.find("Jo"))
#name.find will find the index number of the first occurance of "Jo" in name. In this case, 0





"john"<"JOhn"








