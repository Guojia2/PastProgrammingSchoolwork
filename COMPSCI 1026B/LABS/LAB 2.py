########TASK 1
# age=int(input("Enter your age:"))
# if age>=9:
#     height=float(input("Please enter your height in cm:"))
#     if height>130:
#         print("You may go on this ride!")
#     else:
#         print ("You are too short for this ride.")
# else:
#     print("You are too young for this ride.")   








# IDEAL_CREDIT_SCORE = 720

# userScore = int(input("Please enter your credit score: "))
# housePrice = int(input( "Please enter the price of the house: "))  #the code fails if the dollar sign is included in the input. Must prompt user to exclude the symbol. Also must change int to float input.
# if userScore => IDEAL_CREDIT_SCORE:    #error here: the => should be changed to >=
#     downPayment = 0.1 * housePrice
# else if userScore < IDEAL_CREDIT_SCORE and userScore > "600": #else if need to be changed to elif here and the quotations need to be removed around 600
#  downPayment = 0.2 * housePrice
# else: 
#     downPayment = 0.3 * housePrice
# print("Your down payment is: ${}".format(downPayment))


IDEAL_CREDIT_SCORE = 720

userScore = int(input("Please enter your credit score: "))
housePrice = float(input( "Please enter the price of the house. Please omit the dollar sign: "))  
if userScore >= IDEAL_CREDIT_SCORE:   
    downPayment = 0.1 * housePrice
elif userScore < IDEAL_CREDIT_SCORE and userScore > 600: 
 downPayment = 0.2 * housePrice
else: 
    downPayment = 0.3 * housePrice
print("Your down payment is: ${}".format(downPayment))
