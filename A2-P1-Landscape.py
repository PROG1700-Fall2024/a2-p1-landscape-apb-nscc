#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     W0487099
#Student Name:  Alex Barr

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Initialize variables

    BASE_LABOUR_CHARGE = 1000
    TOP_SQR_FEET = 5000
    OVER_TOP_SQR_FEET_CHARGE = 500
    TREE_CHARGE = 100 #Per tree

    grassFee = [0.05, 0.02, 0.01] #Price: [Fescue, Bentgrass, Campus]
    
    houseNumber = 0
    propertyDepth = 0
    propertyWidth = 0
    grassType = 0
    numberOfTrees = 0

    charge = 0.0
    totalCharge = 0.0
    sqrFootage = 0

    #Welcome the user to the program

    print("Welcome to the Landscape Calculator!\n")

    #Get neccessary values

    houseNumber = int(input("Enter House Number: "))
    print("")
    propertyDepth = int(input("Enter property depth (feet): "))
    print("")
    propertyWidth = int(input("Enter property width (feet): "))
    print("")
    grassType = int(input("--Grass Type Selection--\n 1 = Fescue \n 2 = bentgrass \n 3 = campus \n Enter the type of grass: "))
    print("")
    #Apply base labour charge and Calculate sqr footage

    charge = BASE_LABOUR_CHARGE
    sqrFootage = propertyDepth * propertyWidth

    #Is the sqr footage over 5000?

    if sqrFootage > TOP_SQR_FEET:
        charge += OVER_TOP_SQR_FEET_CHARGE

    #Determine what to charge based on grass type then apply it

    charge += sqrFootage * grassFee[grassType - 1] #This is where the if/elif/else statement would go, I just wanted to use a list because they are cool and I can do it in one line

    #Get the number of trees from the user

    numberOfTrees = int(input("Enter the number of trees: "))
    print("")

    #Final Calculations

    charge += numberOfTrees * TREE_CHARGE
    totalCharge = charge #redundant line of code but in there in case I would want to do my calculutions serperately from the total calculation

    #Display cost to the user
    
    print(f"Total Cost for house {houseNumber} is: ${totalCharge:.2f}")

    # YOUR CODE ENDS HERE


main()