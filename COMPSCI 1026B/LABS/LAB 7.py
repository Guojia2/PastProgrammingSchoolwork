# values = [1,2,3,4,5, "hello", 6,7,8,9, "10" ]
# for cur in values:
#     print("The value is :", values[cur])
#     if type(values[cur]) == str:
#         raise ValueError("This is a string!")
        

# values = [1,2,3,4,5, "hello", 6,7,8,9, "10" ]
# for cur in values:
#     try:
#         print("The value is :", values[cur])
#     finally:
#             if type(values[cur]) == str:
#                  raise ValueError("This is a string!")
        

# filename = input( "Enter filename: ") # this line fails if an inputted file name cannot be found
# infile = open(filename, "r")
# line = infile.readline()
# value = int(line)  # if the contents of a line are not digits, then this line will fail

# print (value)

#####  if the 

filename = input( "Enter filename: ") # this line fails if an inputted file name cannot be found
try:  
    infile = open(filename, "r")
    line = infile.readline()
except FileNotFoundError:
    print("sorry, the file could not be found")
try: 
    value = int(line)  # if the contents of a line are not digits, then this line will fail
    infile.close()
    print("file was closed")
except Exception:
    print ("something went wrong")

