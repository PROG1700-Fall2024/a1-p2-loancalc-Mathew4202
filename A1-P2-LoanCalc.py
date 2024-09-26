#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    """
Student Name:    Mathew Akunyili
Program Title:  Weekly loan Calculator
Description:    calculate the weekly payement somone would pay after taking a loan
"""

    #declare variables
    #This section declare the variables
    x = 5200
    y = -52
    # Identify type of program
    # this specifies what this proram does
    print("Weekly Loan Calculator")
    
    # Prompt user to enter the amount of loan
    #when the user inputs the value we have to store it in a variable and change it to float
    loan = float(input("Enter the amount of loan:"))

    # Ask user to enter the interest rate
    #when the user inputs the value we have to store it in a variable and change it to float
    interestRate = float(input("Enter the interest rate (%):"))

    # Ask user to enter the number of Years
    #when the user inputs the value we have to store it in a variable and change it to float
    years = float(input("Enter number of years:"))

    #perform calculations
    #firstly we calculate for i then we calculate the weekly payment given the formula
    i = interestRate / x
    weeklyPayment = ((i) / (1 - (1 + i)**(y*years)))*loan

    #print weekly payments
    # format it to 2 decimal places
    print(f"Your weekly payment will be: ${weeklyPayment:.2f}")








    # YOUR CODE ENDS HERE

main()
