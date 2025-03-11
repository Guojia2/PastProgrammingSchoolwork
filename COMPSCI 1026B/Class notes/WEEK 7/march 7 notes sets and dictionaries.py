
### today we are learning about sets

# x = 1
# print(type(x))
# x = 2.3
# print(type(x))   ## this will print int and then float and then str
# x = "hi"
# print(type(x))


# tf=isinstance(x,str)   ## asks true/false: is x a string?
# print (tf)         ## prints the answer

#A set is a container thaty stores a collection of unique values
# different from list because items in sets are not stored in any particular order
# operations are same as operations performed on sets in mathematics
#set operations are much faster than list operations because they do not need to maintain a particular order
# Examples of a set: The colour of a flag. Canada is red and white, not red white red white from left to right

# cast = ('luigi', 'gumby', 'apples')
# ## to create a set, you can convert a list to a set
# set(cast)

# ## converting to a set will remove any duplicates in the list

# # you cannot use {} to make an empty list in python. 

# newList = []
# set = ()
# ## you can use the len() function to count the elements in a set.
# can also ask things like "if 'luigi' in cast:"
# can still use for and while loops
# sets can be sorted to convert it into a list
# sets are mutable so you can add elemtns by using .add() instead of .append(). Use .discard() to remove an element 
# if you add a duplicate element to a set, it will not affect the size of the set
#  .remove() will remove an item and return an error if the item is not in the set
# .clear() clears the whole set, thus making its length == 0

# a set is a subset of another set if and only if every element in the subset is also in the main set
#.issubset() can be used to return true or false statement to check if one set is subset of anoither
# two sets are equal if they have the exact same items . British == french and canadian is subset of british
# set1.union(set2) will create a NEW SET that is a combination of two sets and discard all duplicates. 
# THE ORIGINAL SETS REMAIN UNCHANGED. UNION() CREATES A NEW SET
# canadian.union(british) is the same as british
# set1.intersection(set2) will create a new set with the all the share elements between two sets
# 
# .difference() creates a NEW SET containing the elements that are only present in the first set but not the other.
#  The order of the sets matters for .difference()
# x.difference(y) != y.difference(x)


# f = open("Class notes/data", 'r')
# text = f.read()
# print(text)

# rawWords = text.split(" ")
# cleanWords = []
# for word in rawWords:
#     cleanWords.append(word.strip())
# wordsSet = set(cleanWords)
# print(len(cleanWords))
# print(len(wordsSet))

####  DICTIONARIES
# conatins keys and values
#each key can only be associated with one value, but values can be associated with multiple keys
#like a function, x must be unique, but y can be duplicate vertical line test

# THIS IS HOW YOU CREATE A DICTIOANRY:

# names = {'Adam':226, 'Bob':519,'Carlos':123,'Dan':222}   # key:value

# print(names['Adam'])  # this is very similar to accessing using an index, except we use Adam instead of 0
# names['Bob']= 555     ## can reassign values just like this
# print(names['Bob'])

# nums = {1:"one",2:"two"}    # in some ways, a list could be said to be a type of dictionary
# print(nums[1])

# #  lists and tuple are refernce-based, as are sets and dictionaries
# # a simple assignment just creates a new pointer

# # you can make a copy of a dictionary using x = dictionary(y)



# # default values: you can have a default value that will be retrieved if the key is not
# numbers = names.get('Fred',911)  ### if Fred's number can be foound, retrieve fred's number. If it cannot be found, retrieve 911 instead
# print("dial"+"911")
# # adding to a dictionary: 
# names["Emma"] = 536

# ## removing elements:
# if 'Fred' in names:
#    fredsnumber=  names.pop('Fred')   # this removes both the key and the value and also retrieves the value

# for key in names:
#    print(key, names[key])


# # you can sort a dictionary using sort()

# # you can iterate trough a dicitonary using a for loop
# for item in names.items():
#    print(item[0],item[1])



f = open('Class notes/records.txt', 'r')
students = []
i = 0
for line in f:
    student = {}
    if i >0:
        if line.strip != "":
            parts = line.split(':')  # each part is a list of one student's ID, name, gpa, grade
            others =parts[1].split(',')   # others is the 
            student['ID'] = parts[0]
            student['Name'] = others[0].strip()
            student['GPA'] = others[1].strip()
            student['Grade'] = others[2].strip()
            print(student)
            students.append(student)
    i +=1

# print(students[1]['Name'])
print(type(students))
print(type(students[1]))
print(type(students[1]["Name"]))
print(students[1]["Name"])

for i in range(len(students)):
    print(students[i]['Name'])

for name in students:
    print(name['Name'])
