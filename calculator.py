def start(): # Start the program
    print("\n// -- Calculator CLI -- \\")
    print("\n enter 'C' to close the program\n enter '<' to go back")
    number1()

# Defining the variables
n1=0
n2=0
eq=0
n3=0

def result(): # Show final result
    global n1,n2,eq,n3
    if eq==1: n3=n1+n2
    elif eq==2: n3=n1-n2
    elif eq==3: n3=n1*n2
    else: n3=n1/n2

    print(" The result is: ",str(n3))
    number1()


def function(num,fun):
    if num.upper()=="C":
        # Close the program if the user enters "C" or "c"
        print("\n Closed the program")
    elif num.upper()=="<":
        fun-=1
        if fun==0 or fun==1: number1()
        elif fun==2: number2()
    else:
        # Retry if the user enters an invalid character
        print("It is not a number, please try again")
        if fun==1: number1()    # Return to the select of the first number
        elif fun==2: number2()
        elif fun==3: equation()



def equation(): # Select equation
    global eq,n2
    print("\n 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division")

    eq = input("\n Equation: ")
    try:
        eq=int(eq)
        if eq==4 and n2==0:
            print(" It is not possible division by zero, please try again")
            equation()
        else:
            result()
    except:
        print("\n")
        function(eq,3)
            


def number2(): # Select number 2
    global n2
    n2 = input(" Number 2: ")

    try:
        n2=int(n2)
        equation()
    except:
        function(n2,2)


def number1(): # Select number 1
    global n1
    n1 = input("\n Number 1: ")
    try:
        n1=int(n1)
        number2()
    except:
        function(n1,1)




start()