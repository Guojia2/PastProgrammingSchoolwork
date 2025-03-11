#Developed by Guojia La
#Date: March 7 2023
#Desc: A program to sell prebuilt  and custom-built computers and record the price.
#Inputs: User's choice of computer parts and prebuilt computers
#Outputs: Cost of purchase 


SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]] 
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]] 
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]] 
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]

PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]




####defining the function to choose parts for a custom pc

def buildCustomPC():  #defining a helper function to be embedded within pickItems() that will allow user to build a custom pc
    print("Great! Let's start building your PC!")
     # this stuff picks the CPU and determines which motherboard is compatible:
    print("First, let's pick a CPU.")
    print("1 : Intel Core i7-11700K, $499.99 \n2 : AMD Ryzen 7 5800X, $312.99")
    validChoice = False
    customPrice= 0
    compatibleMotherboards = []
    while not validChoice:
        choice = input("Choose the number that corresponds with the part you want:")
        if choice == "1" or choice == "2":
            validChoice = True
            if choice == "1":
                compatibleMotherboards.append(MOTHERBOARD[1])   ### if choice is Intel CPU, add  MSI Z490-A PRO to compatibleMotherboards
                customPrice= customPrice + CPU[0][2] ## add price of Intel CPU to customPrice
            elif choice == "2": 
                    compatibleMotherboards.append(MOTHERBOARD[0])# if choice is AMD CPU, add MSI B550-A PRO to comaptibleMotherbards
                    customPrice=customPrice+CPU[1][2] #add price of AMD CPU to customPrice

    #User selects motherboard
    print ("Next,let's pick a compatible motherboard.")
    validChoice = False
    while not validChoice:   
        print(compatibleMotherboards[0][0] +' : '+ compatibleMotherboards[0][1])
        choice = input("Choose the number that corresponds with the part you want: ")
        if choice == compatibleMotherboards[0][0]:
            customPrice = customPrice + compatibleMotherboards[0][2]
            validChoice = True

# User selects RAM
    print("Next, let's pick your RAM.")
    print("1: 16 GB, $82.99")
    print("2: 32 GB, $174.99")
    validChoice = False
    while not validChoice:
        choice = input("Choose the number that corresponds with the part you want:")
        for ram in RAM:
            if choice == ram[0]:
                customPrice += ram[2]
                validChoice = True

    #user selects PSU:
    print("Please choose a PSU:")      
    print('1 : Corsair RM750, $164.99') 
    validChoice = False
    while validChoice == False: ## the while loop will keep asking user for input until they enter '1'
        choice = input("Choose the number that corresponds with the part you want:")  ## prompt user for input
        if choice == "1":
            validChoice = True    
            customPrice = customPrice + PSU[0][2]  

    ## user selects case :
    print("Next, let's pick your case.")
    print('1 : Full Tower (black), $149.99')
    print('2 : Full Tower (red), $149.99')
    validChoice = False   
    while validChoice == False:
        choice = input("Choose the number that corresponds with the part you want:")
        if choice == '1':
            customPrice = customPrice +  CASE[0][2] 
            validChoice = True
        elif choice == '2':
            customPrice = customPrice + CASE[1][2]
            validChoice = True
# User seelcts SSD. 

    noStorage = True  ## this variable will force the user to pick a HDD if no SSD was chosen
    print("Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
    for ssd in SSD:
        print(ssd[0] + " : " + ssd[1] + ", $" + str(ssd[2]))
        validChoice = False 
    while validChoice == False:
        choice = input("Choose the number that corresponds with the part you want:")    
        if choice.lower() == 'x':
            validChoice = True
        elif choice.isdigit() and int(choice) in [1,2,3]:
            customPrice = customPrice  + SSD[int(choice)-1][2] 
            validChoice = True
            noStorage = False
    # Select HDD
    print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
    print("1 : 500 GB, $106.33")
    print("2 : 1 TB, $134.33")
    
    validChoice = False
    while not validChoice:
        choice = input("Choose the number that corresponds with the part you want (or X to not get an HDD):")
        if choice == '1' or choice == '2': ## taking choice.lower so that program will recognize X and x as valid
           validChoice = True
        if choice == '1':
            customPrice = customPrice + HDD[0][2]
        if choice == '2':
            customPrice = customPrice + HDD[1][2]
        if noStorage == False:  ## this conditional statement allows user to skip HDD if SSD has already been chosen
            if choice == choice.lower() == 'x':
                validChoice = True


    # Select graphics card
    print("Finally, let's pick your graphics card (or X to not get a graphics card).")
    print("1 : MSI GeForce RTX 3060 12GB, $539.99")
    validChoice = False
    while validChoice == False:
        choice = input("Choose the number that corresponds with the part you want:")
        if choice.lower() == 'x':
            validChoice = True
        if choice == '1':
            customPrice = customPrice + GRAPHICS_CARD[0][2]
            validChoice = True
        
    return customPrice

def prebuiltPicker():  
    print( "Great! Let's pick a pre-built PC! \n\nWhich prebuilt would you like to order?\n1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99\n2 : SkyTech Prism II Gaming PC, $2839.99\n3 : ASUS ROG Strix G10CE Gaming PC, $1099.99")
    validChoice=False
    prebuiltPrice = 0
    while not validChoice:
        prebuiltChoice = (int(input("Choose the number that corresponds with the part you want:")))
        if prebuiltChoice == 1:
            prebuiltPrice= prebuiltPrice + PREBUILTS[0][2] 
            validChoice=True
        if  prebuiltChoice == 2:
            prebuiltPrice=prebuiltPrice+ PREBUILTS[1][2]
            validChoice= True
        if prebuiltChoice == 3:
            prebuiltPrice=prebuiltPrice + PREBUILTS[2][2]
            validChoice = True
    return prebuiltPrice    



def pickItems():
    shoppingCart = []
    print("Welcome to my PC shop!\n")
    choice=1 #default
    while choice == 1 or choice ==2 or choice ==3:
        choice = int(input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?"))
        if choice == 1:
            price = buildCustomPC()
            shoppingCart.append(price)
            print("You have selected all of the required parts! Your total for this PC is $",price)
        elif choice == 2:
            price = prebuiltPicker()
            shoppingCart.append(price)
            print("You have selected all of the required parts! Your total for this PC is $",price)
        elif choice == 3:
            return shoppingCart
        else:
            choice=1

    print()

print(pickItems())

# TEST 1 : PASSED
# TEST 2: PASSED
#TEST 3: PASSED
#TEST 4: PASSED
# TEST 5: PASSED


