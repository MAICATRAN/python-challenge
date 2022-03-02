<<<<<<< HEAD

import os
import csv

budget_data_csv = os.path.join("C:\MAICA\MONASH\Python\python-challenge\PyBank\Resources", "budget_data.csv")

months = []
profit_loss = []
count_month = 0
current_month = 0
net_change = 0
prev_month = 0
profit_loss_change = 0


with open(budget_data_csv) as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")


    for row in csvreader:
        count_month = count_month + 1

        current_month = int(row[1])
        net_change += current_month

        if (count_month) == 1:
            prev_month = current_month

        else:
            profit_loss_change = current_month - prev_month

            months.append(row[0])
            profit_loss.append(profit_loss_change)
            
            prev_month = current_month


    Total_profit_loss = sum(profit_loss)
    Average_profit_loss = round(Total_profit_loss/(count_month -1),2)

    max_value = max(profit_loss)
    min_value = min(profit_loss)

    highest_month_index = profit_loss.index(max_value)
    lowest_month_index = profit_loss.index(min_value)
    greatest_month = months[highest_month_index]
    lowest_month = months[lowest_month_index]


print("Financial Analysis")

print("-------------------------------")
print(f"Total Months: {count_month}")
print(f"Total: ${net_change}")
print(f"Average Change: ${Average_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_month} (${max_value})")
print(f"Greatest Decrease in Profits: {lowest_month} (${min_value})")


budget_file = os.path.join("C:\\MAICA\\MONASH\\Python\\python-challenge\\PyBank\\analysis", "budget_data.text")
with open(budget_file, "w") as outfile:
    outfile.write("Financial Analysis")

    outfile.write("-------------------------------\n")
    outfile.write(f"Total Months: {count_month}\n")
    outfile.write(f"Total: ${net_change}\n")
    outfile.write(f"Average Change: ${Average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_month} (${max_value})\n")
    outfile.write(f"Greatest Decrease in Profits: {lowest_month} (${min_value})\n")



    

        
=======

import os
import csv

budget_data_csv = os.path.join("C:\MAICA\MONASH\Python\python-challenge\PyBank\Resources", "budget_data.csv")

months = []
profit_loss = []
count_month = 0
current_month = 0
net_change = 0
prev_month = 0
profit_loss_change = 0


with open(budget_data_csv) as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")


    for row in csvreader:
        count_month = count_month + 1

        current_month = int(row[1])
        net_change += current_month

        if (count_month) == 1:
            prev_month = current_month

        else:
            profit_loss_change = current_month - prev_month

            months.append(row[0])
            profit_loss.append(profit_loss_change)
            
            prev_month = current_month


    Total_profit_loss = sum(profit_loss)
    Average_profit_loss = round(Total_profit_loss/(count_month -1),2)

    max_value = max(profit_loss)
    min_value = min(profit_loss)

    highest_month_index = profit_loss.index(max_value)
    lowest_month_index = profit_loss.index(min_value)
    greatest_month = months[highest_month_index]
    lowest_month = months[lowest_month_index]


print("Financial Analysis")

print("-------------------------------")
print(f"Total Months: {count_month}")
print(f"Total: ${net_change}")
print(f"Average Change: ${Average_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_month} (${max_value})")
print(f"Greatest Decrease in Profits: {lowest_month} (${min_value})")


budget_file = os.path.join("C:\\MAICA\\MONASH\\Python\\python-challenge\\PyBank\\analysis", "budget_data.text")
with open(budget_file, "w") as outfile:
    outfile.write("Financial Analysis")

    outfile.write("-------------------------------\n")
    outfile.write(f"Total Months: {count_month}\n")
    outfile.write(f"Total: ${net_change}\n")
    outfile.write(f"Average Change: ${Average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_month} (${max_value})\n")
    outfile.write(f"Greatest Decrease in Profits: {lowest_month} (${min_value})\n")



    

        
>>>>>>> 16cefa0361fdc1efdbbfa4c4a19743b570eb55b1
