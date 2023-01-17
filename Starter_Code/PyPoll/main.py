'''
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote'''

import os
import csv

absolute_path = os.path.dirname(__file__)
relative_path = os.path.join(absolute_path, "Resources", "election_data.csv")

with open(relative_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    total_id = []
    total_county = []
    total_vote = []

    for row in csv_reader:
        id = row[0]
        county = row[1]
        vote = row[2]
        
        total_vote.append(vote)
    
    vote_count = len(total_vote)
    print(vote_count)


'''
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''