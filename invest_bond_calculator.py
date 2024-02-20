import math

''' 
Program that allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator.
'''

print("investment   - to calculate the amount of interest you'll earn on your investment") 
print("bond         - to calculate the amount you'll have to pay on a home loan")
user_choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_choice == "investment":
    deposit_amount = P = float(input("Deposit amount?: ")) #Using 'P' for the formula. Same for 'r' and 't' below.
    interest_rate_input = float(input("Interest rate (as a percentage)?: ")) 
    interested_rate_divided = r = interest_rate_input / 100 #Percentage calculation
    number_years = t = float(input("Number of years for investment?: "))
    interest = input("Please type 'simple' or 'compound' interest (simple/compound): ").lower()
    if interest == "simple":
        simple_interest = round(P *(1 + r*t),2)
        print(f"The total is {simple_interest}")
    elif interest == "compound":
        compound_interest = round(P * math.pow((1+r),t),2)
        print(f"The total is {compound_interest}")
    else:
        print("Please choose 'simple' or 'compound' next time.")

elif user_choice == "bond":
    house_value = P = float(input("What is the present value of the house?: "))
    annual_interest_rate = float(input("Interest rate (as a percentage)?: ")) #User input annual interest rate
    interested_rate_divided = annual_interest_rate / 100 #Perecentage calculation
    monthly_interest_rate = i = interested_rate_divided / 12 #Divide annual interest rate by 12 to get monthly interest rate
    number_months = n = float(input("Number of months to repay the bond?: "))
    repayment = round((i * P)/(1 - (1 + i)**(-n)),2) #Rounded to two decimals
    print(f"The mothly repayment is {repayment}")

else:
    print("Please choose 'investment' or 'compound' next time.")
    