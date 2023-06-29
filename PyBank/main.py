#PyBank_Python-Challenge_Module3
#import dependencies
import os
import csv

#filepath of file (csv) we want to analyze
budget_data_csv = os.path.join('Resources','budget_data.csv')

#identify my lists
Profit_Losses=[]
Month_Year=[]
revenue_change = []
    

#opens csv (read only) file   
with open(budget_data_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvfile) #<----identifies the first row as a "header" then moves to next line.
    
    #instructions for the row after header.
    for rows in csvreader:
        Profit_Losses.append(int(rows[1])) #<----data picked up as values after header and in column2
        Month_Year.append(rows[0]) #<----data picked up after header and in column1
   
    for ValueX in range(1,len(Profit_Losses)): #<---- x will be described as total number of "profit_losses" _ row2-row1=rowA _ rowA-lastrow= valueX
     
        #revenue_change = row2_column2(of range "ValueX") - row1_column2(of range "ValueX")
        revenue_change.append((int(Profit_Losses[ValueX])-int(Profit_Losses[ValueX-1])))
      
    #calculates the average    
    revenue_average = format(sum(revenue_change)/ len(revenue_change),'.2f')
    
    #calculates the number of values in column "Months_Years"
    total_months = len(Month_Year)
    
    #calculates the max & min change
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
    
    #printing instructions
    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$"+ str(sum(Profit_Losses)))
    print("Average Change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(Month_Year[revenue_change.index(max(revenue_change))+1])+" " + "($" + str(greatest_increase)+")")
    print("Greatest Decrease in Profits: " + str(Month_Year[revenue_change.index(min(revenue_change))+1])+" "+"($" + str(greatest_decrease)+")")
    
#creating and printing new file in a different folder
Output_txt = os.path.join('analysis','output.txt')
with open(Output_txt,'w') as file:   
    file.write("Financial Analysis" + "\n")
    file.write('--------------------------------------' + "\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: " + "$"+ str(sum(Profit_Losses)) + "\n")
    file.write("Average Change: " + "$" + str(revenue_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(Month_Year[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(Month_Year[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")" + "\n")
    file.close ()
    
    