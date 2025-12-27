import numpy as np
import pandas as pd
import csv

dataFrame = pd.read_csv(r"Projects\Smart Expense Tracker & Analyzer\expenses.csv")
print(dataFrame)

np_arr_amount = dataFrame["amount"]. to_numpy()
print(np_arr_amount)
print(type(np_arr_amount))


#Total Spending:
Total_Spending = np_arr_amount.sum(axis=None)
print(f"Total amout of spending is: {Total_Spending} ")

#Average Spending:
Average_Spending = np_arr_amount.mean()
print(f"Average spending is {Average_Spending}")

#Highest Spending:
Highest_Spending = np_arr_amount.max()
print(f"Highest spending: {Highest_Spending}")

#Lowest Spending
Lowest_Spending = np_arr_amount.min()
print(f"Lowest spending is: {Lowest_Spending}")


#Category
category_grp = dataFrame.groupby("category")["amount"].sum()
print(category_grp)



#Highest Spending Category
highest_spending_category = category_grp.idxmax()
print("You spend most money on:", highest_spending_category)

#Lowest Spending Category
lowest_spending_category = category_grp.idxmin()
print("You spend lowest money on:", lowest_spending_category)

#For food
food_total = dataFrame[dataFrame["category"] == "Food"]["amount"].sum()
print(f"Total amount spend in food is {food_total}")

#For Travel
Travel_total = dataFrame[dataFrame["category"] == "Travel"]["amount"].sum()
print(f"Total Travel amount is: {Travel_total}")

#Shopping
Shopping_total = dataFrame[dataFrame["category"] == "Shopping"]["amount"].sum()
print(f"Total shopping amount is: {Shopping_total}")


final_report = pd.DataFrame({
    "Category" : ["Food", "Travel", "Shopping"],
    "Total_spent" : [food_total, Travel_total, Shopping_total]
})

final_report.to_csv("final_report.csv", index=False)
print("Final report generated to final_report.csv")





