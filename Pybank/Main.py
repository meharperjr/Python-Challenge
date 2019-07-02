import os
import csv

month_count = 0
total_revenue = 0
this_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []


# open csv file
bank_csv = os.path.join("C:\\Users\\mehar\\Documents\\Python\\Python-Challenge\\Pybank\\budget-data.csv")

with open(bank_csv,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

  
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_revenue = int(row[1])
        total_revenue = total_revenue + this_month_revenue
        if month_count > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue


# analyze the month by month results
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

#Print to terminal

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Average Revenue Change: ${average_change:,.2f}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change:,.2f})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change:,.2f})")


file = os.path.join("C:\\Users\\mehar\\Documents\\Python\\Python-Challenge\\Pybank\\pybank_output.txt")
with open(file,'w') as pyb:
    pyb.write("Financial Analysis" + "\n")
    pyb.write("----------------------------------------" + "\n")
    pyb.write(f"Total Months: {month_count}" + "\n")
    pyb.write(f"Total Revenue: ${total_revenue:,.2f}" + "\n")
    pyb.write(f"Average Revenue Change: ${average_change:,.2f}" + "\n")
    pyb.write(f"Greatest Increase in Revenue: {max_month} (${max_change:,.2f})" + "\n")
    pyb.write(f"Greatest Decrease in Revenue: {min_month} (${min_change:,.2f})" + "\n")