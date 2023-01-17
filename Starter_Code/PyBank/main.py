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
import statistics as st

abs_path = os.path.dirname(__file__)
file = os.path.join(abs_path, "Resources", "budget_data.csv")

#header = Date, Profit/Loss
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    month_counter = []
    change_ls = []
    net = 0
    last_month_profit = 0

    for financial_reporting in csv_reader:
        date = financial_reporting[0]
        month_counter.append(date)
        
        current_month_profit = int(financial_reporting[1])
        net += current_month_profit

        #calculate change in profit/loss each entry 
        change = current_month_profit - last_month_profit
        last_month_profit = current_month_profit
        change_ls.append(change)
        
    #calculating average change (assuming no numpy package allowed
    total_months = len(month_counter)

    print(f'Total Months: {total_months}')
    print(f'Total: ${net}.00')    

    avg_change = st.mean(change_ls)
    #print(f'Changes in Profit/Loss over the entire period: ${change_ls}')
    print(f'Average Changes: ${avg_change}')

    #greatest increase/decrease
    print(f'Greatest increase in profits: {month_counter[change_ls.index(max(change_ls))]} (${max(change_ls)})')
    print(f'Greatest decrease in profits: {month_counter[change_ls.index(min(change_ls))]} (${min(change_ls)})')