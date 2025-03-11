#Developed by Guojia La
#Date: Feb 7 2023
#Desc: A program to receive desired criteria for a meal order at a restaurant and assign dishes based on those criteria. Also calculates meal cost, including taxes and tips.
#Inputs: Number of invitees, dietary preferences, tip percent.
#Outputs: Order summary, price of order.




# Declaring variables. 
#More variables will be declared later because they will be dependent on these first ones
numPizza = 0
numFalafel = 0
numPasta = 0
numSteak = 0
numBeverage = 0
subTotalMeal = 0
subTotalBeverage = 0


# input the number of invitees


numInvitees = int(input("Please enter the number of invitees:"))
for i in range(numInvitees):  # looping through each invitee and asking for their preferences
    keto = input(
        "Please enter the order details for invitee Number %d/%d \nDo you want a keto friendly meal? " % (i+1, numInvitees))
    if keto == "y":
        keto = True  # using true and false statements for the desired food parameters
    else:
        keto = False
    vegan = input("Do you want a vegan meal?")
    if vegan == "y":
        vegan = True
    else:
        vegan = False
    glutenfree = input("Do you want a Gluten-free meal?")
    if glutenfree == "y":
        glutenfree = True
    else:
        glutenfree = False
    # These lines below determine which dish this invitee will receive and adjust subTotalMeal appropriately
    if keto and vegan and not glutenfree:
        numPizza = numPizza+1
        subTotalMeal = subTotalMeal+44.50
    elif not keto and vegan and not glutenfree:
        numPasta = numPasta+1
        subTotalMeal = subTotalMeal + 48.99
    elif keto and vegan and glutenfree:
        numFalafel = numFalafel+1
        subTotalMeal = subTotalMeal+52.99
    elif keto and not vegan and glutenfree:
        numSteak = numSteak+1
        subTotalMeal = subTotalMeal+49.60
    else:
        numBeverage = numBeverage+1
        subTotalBeverage = subTotalBeverage+5.99





total = subTotalMeal+subTotalBeverage
taxTotal = total*1.13

# Here the user chooses the tip as an integer value.
#  Some more assignments are made.

tipPercent = int(input("How much do you want to tip your server (% percent)?"))
tipTaxTotal = round(taxTotal*(100+tipPercent)/100)


subTotalPizza = round(numPizza*44.50, 2)
subTotalPasta = round(numPasta*48.99, 2)
subTotalFalafel = round(numFalafel*52.99, 2)
subTotalSteak = round(numSteak*49.60, 2)



# Printing a summarized  order for the user

print("You have %d invitees with the following orders:" % (numInvitees))
print("%d invitees ordered Pizza. The cost is: $%.2f" %
      (numPizza, subTotalPizza))
print("%d invitees ordered Pasta. The cost is: $%.2f" %
      (numPasta, numPasta*48.99))
print("%d invitees ordered Falafel. The cost is: $%.2f" %
      (numFalafel, numFalafel*52.99))
print("%d invitees ordered Steak. The cost is: $%.2f" %
      (numSteak, numSteak*49.60))
print("%d invitees ordered only beverage. The cost is: $%.2f" %
      (numBeverage, subTotalBeverage))




print("The total cost before tax is %.2f" % (total))
print("the total cost after tax is %.2f" % (taxTotal))
print("The total cost after %d%% tip is %d" % (tipPercent, tipTaxTotal))









