import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #Create Lists
    profit = []
    monthly_changes = []
    date = []

    #Set variables
    months = 0
    total_profit = 0
    total_change_profits = 0
    initial_profit = 0

    for row in csvreader:
        print(row)
        #Count months
        months = months + 1 

        date.append(row[0])

       #Figure out total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

       #Monthly P/L change & Total P/L change
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

       #Average change in P/L (NOT CORRECT)
        average_change_profits = (total_change_profits/months)
      
       #Max/Min changes & Dates
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
      
    print("Financial Analysis")
    print("Total Months: ", str(months))
    print("Total Profits: ", "$", str(total_profit))
    print("Average Change: ", "$", str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

with open('financial_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("    Total Months: " + str(months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
