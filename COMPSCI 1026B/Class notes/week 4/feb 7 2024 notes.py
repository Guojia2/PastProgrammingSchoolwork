##### Errors

#    2 types of errors
# #      Syntax errors. Code will not run unless syntax error is fixed

# input()
# print(x)
# while i in range(3) #should be "for" not "while"
# if 3>8
# print(0)

#########

#####      Logic error 
#This code should print all odd numbers from 1 to 11
# for i in range (1,11):
    # if i%2==0:
    #      print(i)
# It doesn't actually do that. Mismatch between expected output and intended output



##############

# a code that will ask the pizza shop owner for the weight of 3 types of cheese and the code will print the total price


# print("Tuesday")

# #implementation of the function

# def orderCheese():
#      print("happy cheese")
# price=10
# total=0
# for i in range(3):
#      w=int(input("weight of the cheese"))
#      total+= price*w
# print("The total is %d"%total)


#### giving a name to a code block
### this is how functions are defined


# print("Suesday")

# ### invoking/calling the function 
# orderCheese()

# print("Muesday")
# orderCheese()




# def sep(length):
#      print("-"*length)
# # you can also use length, sym and print(sym*length) to have more customizability
# #length is the PARAMETER, and 10 would be an ARGUMENT


# def main():
#     print("Suesday")
#  ### invoking/calling the function 
#     orderCheese()
#     sep(10)
#     print("Muesday")
#     orderCheese()
#     return total



# t= orderCheese()






# def cube(length):
#      v=length**3
#      return v
# vol=cube(4)
# print("volume =", vol)
# print(cube(4))




#####  write a function that takes two numbers and returns the smalllest

def check(n1, n2):
     if n1<n2:
          return n1
     else:      ## only one of these return lines will be executed because the conditions don't overlap
          return n2



x = 6
y =2
x+=2
x+=y

z= check(x,y)
     

print ("smallest=", z)


