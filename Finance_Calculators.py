import math

# Initial display to the user showing the selections available:
print(f"Choose either 'investment' or 'bond' from the menu below to proceed:")
print("")
print(f"investment   -   to calculate the amount of interest you'll earn on your investment")
print(f"bond         -   to calculate the amount you'll have to pay on a home loan")

#Requesting user input into the program; Using While and if loop to check that.. 
# they have input the required words, else to print an error message; 
# Utilized .lower to account for variations in input received
print("")
while True:
    user_input = str(input(f"Input either 'investment' or 'bond' to proceed: ").lower())
    if user_input != "investment" and user_input != "bond":
        print("You have entered an incorrect choice")  
        continue  

# If user inputs "investment", proceed to ask other details and provide the interest calculation
    elif user_input == "investment":
        user_principal = int(input(f"Enter the amount to deposit: "))
        user_interest_percent = float(input("Enter the interest rate: "))
        user_years = int(input("Enter the number of years planned on investing: "))
        interest = str(input(f"Enter if you want 'simple' or 'compound' interest: "))
        if interest == "simple":
            Simple_earned = user_principal * (1 + (user_interest_percent/100) * user_years)
            print(f" The amount you will earn after {user_years} years at {user_interest_percent} is {Simple_earned}")
            break
        elif interest == "compound":
            Compound_earned = user_principal * math.pow((1 + (user_interest_percent/100)), user_years)
            print(f" The amount you will earn after {user_years} years at {user_interest_percent} interest rate is {round(Compound_earned,2)}")
        break
# If user inputs "bond", proceed to ask other details and provide the interest calculation
    elif user_input == "bond":
        house_value = float(input("Enter the present value of the house: "))
        bond_interest_percent = float(input("Enter the interest rate: "))
        # dividing by 100 not mentioned in the task, but adding here so the math makes sense
        bond_month_rate = float((bond_interest_percent/12)/100)
        bond_repay_months = float(input("Enter the number of months planned for repayment: "))
        bond_repmt = (bond_month_rate*house_value)/(1-(1+bond_month_rate)**(-bond_repay_months))
        print(f"The amount you will have to repay each month is {round(bond_repmt,2)}")
        break