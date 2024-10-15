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

    grassFee = [0.05, 0.02, 0.01]
    
    houseNumber = 0
    propertyDepth = 0
    propertyWidth = 0
    grassType = 0

    charge = 0.0
    totalCharge = 0.0
    sqrFootage = 0

    #Welcome the user to the program

    print("Welcome to the Landscape Calculator!\n")

    #Get neccessary values

    houseNumber = int(input("Enter House Number: "))
    propertyDepth = int(input("Enter property depth (feet): "))
    propertyWidth = int(input("Enter property width (feet): "))
    grassType = int(input("--Grass Type Selection--\n 1 = Fescue \n 2 = bentgrass \n 3 = campus \n Enter the type of grass: "))
   
    #Apply base labour charge and Calculate sqr footage

    charge = BASE_LABOUR_CHARGE
    sqrFootage = propertyDepth * propertyWidth

    #Is the sqr footage over 5000?

    if sqrFootage > TOP_SQR_FEET:
        charge += OVER_TOP_SQR_FEET_CHARGE

    #Determine what to charge based on grass type then apply it

    charge += sqrFootage * grassFee[grassType]



    #Get the number of trees from the user

    #Final Calculations

    #Display cost to the user


    # YOUR CODE ENDS HERE

main()