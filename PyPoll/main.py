#PyPoll_Python-Challenge_Module3
#import dependencies
import os
import csv
import collections
from collections import Counter

#filepath of file (csv) we want to analyze
election_data_csv = os.path.join('Resources','election_data.csv')

#identify my lists
Candidates=[]
Candidate_Votes=[]
    
#opens csv (read only) file     
with open(election_data_csv, 'r') as csvfile:
    Pypoll_csv_reader = csv.reader(csvfile, delimiter= ",")
    Pypoll_csv_header = next(csvfile) #<----identifies the first row as a "header" then moves to next line.
    
    #instructions for the row after header.               
    for row in Pypoll_csv_reader:
        Candidates.append(row[2]) #<----data picked up in column3
        
    Candidate_Count= Counter(Candidates) #<----Counts elements from (arrange_list)   
    
    Candidate_Votes.append(Candidate_Count.most_common()) #<----Lists the votes and their counts from the most common to the least.
    #^---- returns ----[[('Diana DeGette', 272892) or [0,-3] ('Charles Casper Stockham', 85213) or [1,-2] ('Raymon Anthony Doane', 11606)]] or [2,-1]
    
    #returns individual items in the list of (Candidate_Votes)
    for item in Candidate_Votes: 
        
        #formating [list number (negative goes backward) table only has 3 items] .3f = %
                                        #/ ----votes per candidates (divided by) total count of votes
        first= format((item[-3][1])*100/(sum(Candidate_Count.values())),'.3f')
        second= format((item[-2][1])*100/(sum(Candidate_Count.values())),'.3f')        
        third= format((item[-1][1])*100/(sum(Candidate_Count.values())),'.3f')       
              
    
    print("Election Results")
    print('--------------------------------------')
    print(f"Total Votes: {sum(Candidate_Count.values())}")
    print('--------------------------------------')
    #candidate placement is off order to replicate the analysis results from UTA_Bootcamp_Module3
    print(f"{Candidate_Votes[0][-2][0]}: {second}% ({Candidate_Votes[0][-2][1]})")
    print(f"{Candidate_Votes[0][-3][0]}: {first}% ({Candidate_Votes[0][-3][1]})")   
    print(f"{Candidate_Votes[0][-1][0]}: {third}% ({Candidate_Votes[0][-1][1]})")    
    print('--------------------------------------')
    print(f"Winner: {Candidate_Votes[0][0][0]}")
    print('--------------------------------------')
    
#creating and printing new file in a different folder
Output_txt = os.path.join('analysis','output.txt')
with open(Output_txt,'w') as file: 
    file.write("Election Results"+"\n")
    file.write('--------------------------------------'+"\n")
    file.write(f"Total Votes: {sum(Candidate_Count.values())}"+"\n")
    file.write('--------------------------------------'+"\n")
    file.write(f"{Candidate_Votes[0][-2][0]}: {second}% ({Candidate_Votes[0][-2][1]})"+"\n")
    file.write(f"{Candidate_Votes[0][-3][0]}: {first}% ({Candidate_Votes[0][-3][1]})"+"\n") 
    file.write(f"{Candidate_Votes[0][-1][0]}: {third}% ({Candidate_Votes[0][-1][1]})"+"\n")   
    file.write('--------------------------------------'+"\n")
    file.write(f"Winner: {Candidate_Votes[0][0][0]}"+"\n")    
    file.write('--------------------------------------'+"\n")   
    file.close ()
    