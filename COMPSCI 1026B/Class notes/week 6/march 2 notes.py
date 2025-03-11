
def withdraw(balance, amount):
    if balance > amount:
        return balance - amount
    else: 
        raise ValueError("We have called the police to shoot your kids!") # red flag, will terminate program

print(withdraw(100,20))
print('done')        ## done is not printed because the ValueError crashes the code. No further code is executed.
# print(withdraw(100,150))   ## ValueErrors are also called Exceptions
# print('done2')

try:
    print(withdraw(100,150))
    print('done2')
except ValueError as ve:
    print("somthjing went wrong",ve)
print("done3")

try:
    file = open('data.csv','r')
    text = file.read()
    list = [1,3,5]
    print(list[10])     ## this list is not printed because all code inside the try function has been crashed. 
except IOError as io:
    print("io:", io)    ### io is the default message 
except IndexError as ie:
    print("ie:",ie)
 
except Exception as ex:
    print("ex:",ex)

finally:
    file.close ### anything inside the "finally" will be executed whetehr we have an exception or not


print("rest of code here")

