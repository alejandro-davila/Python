#PyBank and PyPoll

* PyBank: Analysis on monthly Profit/Loss data
* PyPoll: Analysis on election result

## Background

I created Python scripts for selecting, analyzing and saving the results of financial records of PyBank and the election result of PyPoll.

## PyBank

![](https://t4.ftcdn.net/jpg/05/69/85/25/240_F_569852518_DTYL4I1fcG19rAZkbQR7Aq01DgKr3qT9.jpg)

* I have developed a Python script to analyze the financial records of PyBank based on the prvoded dataset, [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset consists of two columns: `Date` and `Profit/Losses`. The script calculates the the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

[PyBank.py - Python script](https://github.com/alejandro-davila/python-challenge/blob/main/PyBank/main.py)

[Output.txt](https://github.com/alejandro-davila/python-challenge/blob/main/PyBank/analysis/output.txt)

  ```text
    Financial Analysis
    --------------------------------------
    Total Months: 86
    Total: $22564198
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```


## PyPoll

![](https://t4.ftcdn.net/jpg/02/75/85/11/240_F_275851129_21bPkkMY3xZiyIKxiBWlFy0XC3Wg91E2.jpg)

* I have developed a Python script to analyze the votes in the election results of PyPoll based on the provided dataset, [budget_data.csv](PyPoll/Resources/election_data.csv). The dataset consists of three columns: `Voter ID`, `County`, and 'Candidate'. The script calculates the the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

[PyPoll.py - Python script](https://github.com/alejandro-davila/python-challenge/blob/main/PyPoll/main.py)

[Output.txt](https://github.com/alejandro-davila/python-challenge/blob/main/PyPoll/analysis/output.txt)

  ```text
    Election Results
    --------------------------------------
    Total Votes: 369711
    --------------------------------------
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    --------------------------------------
    Winner: Diana DeGette
    --------------------------------------
  ```


## Alejandro Davila | Python | UTA_DATA_Module3
