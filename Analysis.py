#Code to accept Income & Expense from user
import pandas as pd
import matplotlib.pyplot as plt

Income = input("Enter your income")
Expense = input("Enter your expense")

data = {
    'Type':['Income', 'Expense'],
    'Amount': [Income, Expense]
}

df = pd.DataFrame(data)
print(df)

#Income vs Expense Chart
plt.figure(figsize=(6, 4))
plt.bar(df['Type'], df['Amount'], color=['green', 'red'])
plt.xlabel('Type')
plt.ylabel('Amount')
plt.title('Income vs Expense')
plt.show()