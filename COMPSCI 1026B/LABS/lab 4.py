def factorial(n):
    result= n
    m=1
    for i in range (1,n+1):
         m=(m)*i
    result=m
    return result
print("result is")
print(factorial(3))



#######
def helloWorld():
     print("hello World")


def  helloworldNTimes(n):
     for i in range (n):
          helloWorld()

def main():
    helloworldNTimes(1)
    helloworldNTimes(2)
    helloworldNTimes(3)


main()

def countVowels (word):   
    numVowels = 1       #this numVowels needs to be set to 0, not 1
    for letter in string:   #change string to word
        if letter in "aeiou":  # convert the word to lowercase before counting vowels OR change aeiou to aeiouAEIOU
             numVowels+=1
return letter   ####return numVowels, not letter

