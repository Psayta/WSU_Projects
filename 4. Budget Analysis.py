# Inputs and Variables
MyBudget = float(input("Enter your budget for the month: "))
Expenses = 'y'
Totalexpenses = 0
# While statement that is looping to add expenses 
while Expenses == 'y':
    Yourexpenses = float(input("Enter an expense: "))
    Totalexpenses = Totalexpenses+Yourexpenses
    Expenses = input("More expenses? Press y or n:")
# Nested if to show conditions of the result of the budget and expenses
    if MyBudget > Totalexpenses:
        print("Your expenses of $",(Totalexpenses),"were under the budget by $",(MyBudget - Totalexpenses))
        if Totalexpenses > MyBudget:
            print("Your expenses of $",(Totalexpenses),"were over the budget by $",(Totalexpenses - MyBudget))
        else:
            print ("Your budget was on point with your expenses")
