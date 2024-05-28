import pandas as pd

Income = input("Enter your income")
Expense = input("Enter your expense")

data = {
    'Type':['Income', 'Expense'],
    'Amount': [Income, Expense]
}

df = pd.DataFrame(data)
print(df)