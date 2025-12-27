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

