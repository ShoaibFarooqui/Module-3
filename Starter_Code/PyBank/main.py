'''
The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:
'''
import os
import csv

abs_path = os.path.dirname(__file__)
file = os.path.join("Resources/budget_data.csv")

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file)
    months = 0
    for budget in csv_reader:
        months += csv_reader[budget]

print(months)
