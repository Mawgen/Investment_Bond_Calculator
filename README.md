Financial Calculator
This Python project provides two essential financial calculators to help you make informed decisions.

Features

Investment Calculator
Calculate earnings for both simple and compound interest options.
Inputs:
Initial deposit amount
Interest rate (percentage)
Investment period (years)
Interest type (simple or compound)
Home Loan (Bond) Calculator
Calculate monthly bond repayments.
Inputs:
House value
Annual interest rate (percentage)
Repayment period (months)
Dependencies

Python (3.x recommended)
math module (built-in)
How to Use

Clone the repository:

Bash
git clone https://github.com/[your-username]/[financial-calculator-repo-name]
Use code with caution.
Run the script:

Bash
python financial_calculator.py  # (Assuming financial_calculator.py is your main script)
Use code with caution.
Follow the menu:

Select "investment" to calculate investment returns.
Select "bond" to calculate home loan repayments.
Understanding the Formulas

Simple Interest:  A = P(1 + rt)

A = total accrued amount (principal + interest)
P = principal amount
r = interest rate per period
t = number of periods
Compound Interest: A = P(1 + r/n) ^(nt)

A = total accrued amount (principal + interest)
P = principal amount
r = annual interest rate
n = number of times interest is compounded per year
t = time in years
Bond Repayment:  x = (i * P)/(1 - (1 + i)^(-n))

x = monthly repayment amount
P = present value of house (loan amount)
i = monthly interest rate
n = number of months over which bond is repaid
Future Development

Incorporate a visual interface for ease of use (e.g., a web interface or a GUI)
Add more financial calculators:
Mortgage affordability calculator
Retirement savings calculator
Contributing

We welcome contributions! Please consider:

Forking the repository.
Creating a feature branch.
Committing your changes.
Pushing the branch.
Submitting a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
