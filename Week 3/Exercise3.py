budget_month=input("What is you budget for the month? : ")

total_budget=0
for expense in range(32):
    nbudget=float(input("How much did you spend today? : "))
    total_budget+=nbudget
print(total_budget)
if str(total_budget) <= str(budget_month):
    print("You are in budget")
else:
    print("You are over budget")