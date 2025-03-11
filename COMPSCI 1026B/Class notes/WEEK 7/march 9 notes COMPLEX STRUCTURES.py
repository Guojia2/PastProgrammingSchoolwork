
##  NO CLASS NEXT TWO WEEKS, VIDEOS WILL BE POSTED INSTEAD

### an ssd and cpu are just 2d lists

#### Goal: read this following info and collect it and clean it up and put it into a dictionary

GROC = 2

def main(filename):
    customers = readfile(filename)
    printNiceDict(customers)
    res = findPurchasesForCustomer(customers,"Bob")
    printNiceDict(res)
    print("Total number of groceries for ")
    

def readfile(filename):
    customers = {}
    f = open(filename, 'r')
    f.readline() ## skip teh title line
    print(" I HAET RETAIL WORK IAM GOING TO KILL MY MANAGER")
    for line in f.readline():
        line = line.strip()  ## strip off the spaces
        if line != "":  ## exclude empty lines
            parts = line.split(",") # split the line at every comma
            print(parts)            ## it's good to print the variable at every step to see if anyhting goes wrong
            cleanParts = [part.strip() for part in parts]  ## this is a shorthand for making a new loop and turning into a list
            print(cleanParts)
            name = cleanParts [1]  ## points to the name of the customer in the list
            print(name)
            purchase = cleanParts [2:]   # data is all the items in the list starting at index 2, aka the date
            print(purchase)
            if name not in customers:  ## if name is found that is not already not in the dictionary known as customers:
                customers[name] = []  ## creates a new list within the customers dictioanry to contain the customer name
            customers[name].append(purchase)  ## appends each purcahse to the customer's name
    return customers
def printNiceDict(dict):
    for customer in dict:
        print(customer+ '.')
        for purchase in dict[customer]:
            print(" ", end = "")
            for item in purchase:
                print(item, end = ' ')
                print()
# a function to return the purchaes for a customer as a dicionary
def findPurchasesForCustomer(customers, name):
    newdict = {}
    if name in customers:
        newdict[name] = customers[name]
    return newdict


# make a function that returns the total number of purchase made by a given customer

def function():
    for customer in customers:
        count = len(customers[customer])
    return count



## if name is specified, the functio n returns the total spend on froceries for this particukar customer,m otrherswise (name="")
def getTotalGroceries(customers, name = ''):
    sum  = 0
    if name == "":
        for customer in customers:
            for purchase in customers[customer]:
                sum += int(purchase[GROC])
    
    else:
        for purchase in customers[name]:
            sum+= int(purchase[GROC])
    return sum



print("i will fix this code later")


main('Class notes/WEEK 7/purchases.csv')






