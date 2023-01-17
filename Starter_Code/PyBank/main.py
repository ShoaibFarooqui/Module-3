'''
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:
'''
import os
import csv

abs_path = os.path.dirname(__file__)
file = os.path.join(abs_path, "Resources", "budget_data.csv")

#header = Date, Gain/Loss
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    month_counter = []
    profit = []
    revenue = 0
    for budget in csv_reader:
        date = budget[0]
        month_counter.append(date)

        money = int(budget[1])
        revenue += money
    
    #calculating average change (assuming no numpy package allowed)

    total_months = len(month_counter)
    print(f'{total_months} months')
    print(f'${revenue}.00')
