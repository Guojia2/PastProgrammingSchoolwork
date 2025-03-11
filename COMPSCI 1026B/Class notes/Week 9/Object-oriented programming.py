## objects are lke humans. humans have a name, height, weight, date of birth, eye color, etc.
# Humans HAVE things and humans CAN do things
#humans can grow, eat, walk, etc.
# likewise, objects have DESCRIPTIONS and ACTIONS
#  difficult to answer questions pertaining to all humans
# there are descriptions of humans that do describe all normal humans, though
 
# if we are talking about a specific human, though, we can answer questions like name, dob, etc.
# this is because we all understand whihc specific person we are referring to

# this is GENERIC vs SPECIFIC
# for objects: CLASS vs  OBJECT
# we can create any number of objects from a single class

# we are all objects of the class human

# JOHN is a human
#JOHN's initial values at birth are can change over time
# objects created from a class has initial values, set at the time of its creation.
# self name is JOHN
#  an object can have multiple names

# JOHN is a BAKER
# Object name is BAKER 
# an object can point to itself using JOHN
#but other objects will refer to JOHN as BAKER



class Human:
    numHands = 2 #hardcoded
    def __init__(self, name, dob,mom,dad, friends):# this method is called the contructor method because it is used to contruct objects
        self._name = name  ## take the parameter 'name' and attach it to self
        self._dob = dob
        self._langs = langs
        self._friends = friends
        self._mom = mom
        self._dad = dad
        # self._health = health
    def getMom(self): # getter
        return self._mom
    def getDad(self): # getter






        return self._dad
    def getName(self): # getter
        return self._name
    
    def getFriends(self): # getter
        return self._friends
    def setName(self, newValue): # setter
        self._name = newValue
    def getLangs(self):
        return self._langs
    def setLangs(self, newLang):
        self._langs = newLang
    # def addLangs(self, newLangs):
    #     for l in newLangs:
    #         self._langs.append(l)
        print(self.speak())
    def run(self,distance):
        self._health = self._health + distance
       
    def speak(self, word = "hello"):  # we always start with the paramter "self", which wll be ignored when it runs
        print(word+"! my name is" + " "+  self._name+ " " +"my health is"+ " "+ str(self._health))
 # skip self and start with name
# appleCEO = Human("Jobs", "1-1-1970", 150, 180, "white", ["En",'Fr'], 80)
# msCEO = Human('Gates', "1-1-1970", 150, 180, "white", '', 80)


# print(prime.getLangs())
# prime.addLangs(['Es','Ma'])

# print(prime.getLangs())
# govHead = prime
# print(govHead.getName())



people = []
for i in range(3):
    name =  "friend"+ str(i)
    dob = str(i)
    langs = str(i)
    friends = []
    newHuman = Human(name, dob)  ## this part wont run properly bc we are missing psoitional rguments, but I dont want to make changes to the human class just for this one example.
    people.append(newHuman)
    print(newHuman.getName())
for i in range (3):
    print(people[i].getName())

# community = people

pmMom = Human("Margaret", 1955)
pmDad = Human('Pierre', 1945)

prime = Human("Justin", "1-1-1970",pmMom, pmDad, friends = people)
# f0=prime.getFriends()[0]
# print(f0)
# f0.setName('Adam')
# print(f0.getName())
# print(people[0].getName())
# print(prime.getFriends()[0].getName())


print(prime.getDad().getName())
# we dont always want to give main() the ability to set values
# sometimes we only want to give it getting permissions
# we do this by using setter and getter functions
# convention: if an _ is used, that means it's meant to be hidden outside of  its object
    # this includes hiding it from functions like main()
    # these are called private, as opposed to public
# in this example, we want _name = justin to be private
# and we can have run() or speak() be public
#our goal is such that, if we type prime._name into main(),
#it will return an error bc it does not recognize it
# this is called ENCAPSULATION


# def main():
#     prime = Human("Justin", "1-1-1970", 150, 180, "white", '', 80)
#     print(prime._name) # this is not the preferred way to do this
#     print(prime.getName()) # we like this
#     prime._name = "Ford" # this is also not preferred
#     prime.setName('Singh') #we like this
#     print(prime.getName()) #we like thiis







# 




# when changing values, it is preferred to use a function rather than to do so directly
# the functions above are called setters and getters


# self points to one instance, and therefore self.name, self.health,
# etc. are called INSTANCE VARIABLES.
#self.instanceVariable format


# a METHOD is just a FUNCTION of a CLASS.
# a function on its own is just  afunction


# print(prime._name)
# print(msCEO._dob)
# print(appleCEO._health)

# # edit values of an object like this:
# prime._dob = '12-12-1990'
# print(prime._dob)


# print(prime._health)
# prime.run(1)
# print(prime._health)


# print(msCEO._health)
# msCEO.run(3)
# print(msCEO._health)

# print(appleCEO._health)
# appleCEO.run(10)
# print(appleCEO._health)
#The main lesson here is the differnce between a class and an object.
#Value CANNOT be assigned to a class, only to objects


# an OBJECT of a CLASS is also called an INSTANCE of a CLASS














