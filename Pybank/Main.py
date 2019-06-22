#importing stuff
import os
import csv

#importing CSV
budget_date_csv = os.path.join("C:\\Users\\mehar\\Documents\\Python\\budget-data.csv")

#creating output file
outfile = os.path.join("..", "..", "Data", "PyBank_Financial_Summary.txt")

months = []
revenue = []

with open("budget_date_csv", 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#find total months

total_months = len(months)

#greatest increase, decrease variables
#set to 0 
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

#calculate average_change
average_change = round(total_revenue/total_months, 2)

#sets path for output file
output_dest = os.path.join("C:\\Users\\mehar\\Documents\\Python\\pybank_output.txt")

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())
