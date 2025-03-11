####  NO  NEW  CONTENT TODAY, JUST WORKING THROUGH EXAMPLES


### function  that taekles list and returns total



def total(arr):
    sum = 0
    for num in arr:
        sum+= num
    return sum

values = [10,12,18]

print("total =", total(values))






# taxation function
# callinga  function by parameters
def addTax(price):
    price = price*1.13
    return price



price=100

print("price variable before functionc call =",price)
      
(addTax(price))  #### when we call a function like this, we are taking a copy of the price, not altering the price itself

print("price variable after functionc call =",price)




# calling a function by reference/alias
def addBonus(marks,bonus):
    for i in range (len(marks)):
        marks[i] += bonus

# grades  = [89,59,39,99]
# print ("before bonus:", grades)
# addBonus(grades,1)
# print("after bonus:", grades)


#### this function changes the value of the grades array
#marks and grades are aliased at line 46, which means both names refer to the same file
## SO if you send a list to a function, the list will be changed




# a function that extracst all names that start with a  title 
# and returns those names in a new list

def titles(names,title):
    new=[]
    for name in names:
        if name.startswith(title):
            new.append(name)
    return new


names = ["Alice", "Mr. Bob", "Carol", "Eng. DEbby", "Mr. Emo"]

newList= titles(names, "Mr.")

print (newList)




arr = [1,2,3]
arr.append(4)

tpl=(1,2,3)   ##tpl means tuple. 

#tuples cannot be appended using .append()
#print(tpl[0]) will print 1
#tpl[0]= 100 returns an error

#tuples are read-only lists. They are immutable.


def math(x,y):
    sum=x+y
    mul=x*y
    return (sum, mul)



tpl=math(9,2)

print(tpl[0])
print(tpl[1])
print(tpl)
print(tpl) 
print(tpl) # use shift + option to edit vertically 
print(tpl) # use shift + option to edit vertically 
print(tpl) # use shift + option to edit vertically 
print(tpl) # use shift + option to edit vertically 
print(tpl) # use shift + option to edit vertically 



(total, times)= math(5,7)

# total becomes sum and times becomes multiplication
print (total)
print(times)






arr= [ 1,["a","b",[55,66,77]], 2.2, True ,[1,2,3,4,5,6]] #integers, strings, floats, booleans, etc

###you can put an array in an array

print (arr[4])

newList=arr[4]
print(newList[0])  #calling a specific index in the inner array
print(arr[4][1])   # can also do it this way. 4 is the outer index, 1 is inner.

print(arr[1][2][2])


#usually we just make multiple separate arrays rather than array within array



#this is called nested lists, matrices, 2d lists, tables, etc.

table= [
    [1,'DAn',28],
    [2,'Bob',29],
    [3,'alice',18]
    ]

print(table[0][1])
print(len(table))
print(len(table[2]))


### let's store the multiplication table in a 10x10 matrix/table/2Dlist


table= []
for rowIdx in range (1,11):
    newRow=[]
    for colIdx in range(1,11):
        newRow.append(rowIdx*colIdx)
    table.append(newRow)

print(table)






def isIdentity(matrix):
    numRows=len(matrix)
    numCols=len(matrix[0])
    for rowIdx in range (numRows):
        for colIdx in range (numCols):
            if rowIdx==colIdx and matrix[rowIdx][colIdx] !=1:
                return False
            elif rowIdx!=colIdx and matrix[rowIdx][colIdx] !=0:
                return False




mat= [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]






