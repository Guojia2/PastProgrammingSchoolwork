
class Human:
    numHands = 2 # hard coded
    def __init__(self,newname,dob,mom=None,dad=None,friends=[],langs=[]):# this is a method, the constructor
        # self.instanceVariable 
        self._name = newname
        self._dob= dob
        self._languages = langs
        self._health=0
        self._friends = friends
        self._mom = mom
        self._dad= dad
    def getName(self): #getter
        return self._name   
    def setName(self, newValue): #setter
        self._name = newValue
    def getDob(self): #getter
        return self._dob   
    def setDob(self, newValue): #setter
        self._dob = newValue
    def getFriends(self): #getter
        return self._friends   
    def setFriends(self, newValue): #setter
        self._friends = newValue
    def getLanguages(self): #getter
        return self._languages   
    def setLanguages(self, newLang): #setter
        self._languages = newLang
    def getMom(self): #getter
        return self._mom 
    def getDad(self): #getter
        return self._dad 
    def addLanguages(self, langs):
        self._languages+= langs
        print(self.speak())  
    def run(self,distance):# this is a method
        self._health += distance
    def speak(self,word='hello'): # this is a method
        return word+"! my name is "+self._name+" my health is "+str(self._health)
    




people = []
# creating objects
for i in range(3):
    name= "friend"+str(i)
    dob= str(i)
    newHuman = Human(name,dob)
    people.append(newHuman)

# accessing objects
# for i in range(3):
#     print(people[i].getName())

# community = people
gp= Human("Trudeau",1900)
pmMom = Human('Margaret',1955)
pmDad = Human('Pierre',1945,None,gp)

prime= Human("Justin",'1970',pmMom,pmDad,friends= people)
f0 = prime.getFriends()[0]
print(f0.getName())
f0.setName('Adam')
print(f0.getName())

print(people[0].getName())
print(prime.getFriends()[0].getName())

print(prime.getDad().getName())
print(prime.getMom().getName())

print(prime.getDad().getDad().getName())

