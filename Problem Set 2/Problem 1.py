# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of Remaining balance: 813.4141998135 
# So your program only prints out one thing: the remaining balance at the end of the year in the format:

# Remaining balance: 4784.0
# A summary of the required math is found below:

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# (below: 3 ways to reach the outcome)

balance = 5000
for i in range(12):
     minPayment = balance * 0.02
     unpaidBalance = balance - minPayment
     interest = 0.18/12.0 * unpaidBalance
     balance = unpaidBalance + interest
print('Remaining balance: '+ str(round(balance, 2)))

def remaining(balance, month = 0):
    month += 1
    minPayment = balance * 0.02
    monthlyBalance = balance - minPayment
    interest = (0.18/12.0)*monthlyBalance
    updatedBalance = monthlyBalance + interest
    balance = updatedBalance
    if month == 12:
        return round(balance,2)
    else:
        return remaining(balance, month)
print('Remaining balance:', remaining(5000))

month = 12
b = 5000
while month >=1:
    p = 0.02*b
    ub = b - p
    b = (1 + 0.18/12.0)*ub
    month -= 1
print('Remaining balance:', round(b,2))