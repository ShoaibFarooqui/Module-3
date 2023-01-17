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
    change_initial = 1088983
    for financial_reporting in csv_reader:
        date = financial_reporting[0]
        month_counter.append(date)
        
        change_final = int(financial_reporting[1])
        net += change_final

        change = change_final - change_initial
        change_initial = change_final
        change_ls.append(change)
    

    total_months = len(month_counter)
    change_ls.remove(change_ls[0])

    avg_change = st.mean(change_ls)

    results = f'''
    Total Months: {total_months}
    Total: ${net}.00
    Average Changes: ${round(avg_change, 2)}
    Greatest increase in profits: {month_counter[(change_ls.index(max(change_ls)))+1]} (${max(change_ls)}.00)
    Greatest decrease in profits: {month_counter[change_ls.index(min(change_ls))+1]} (${min(change_ls)}.00)
    '''

print(results)
with open("Starter_Code/analysis/PyBank_Output.txt", 'w') as out:
    out.write(results)

