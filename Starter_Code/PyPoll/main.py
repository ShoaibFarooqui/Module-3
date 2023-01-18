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

    total_vote = []
    results = {}
    percentages = []

    for row in csv_reader:
        vote = row[2]
        total_vote.append(vote)
        #counting votes for each candidate
        if vote in results:
            results[vote] += 1
        else:
            results[vote] = 1

    
    vote_count = len(total_vote)



    #sorted() seemed to be the only feasible way to order the dictionary "results" by the values rather than keys
    podium = sorted(results.items(), key=lambda x:x[1], reverse=True)
   # number_of_votes_received = count[1] for count in podium
    election = f'''
    Election Results
    ----------------------------------
    Total Votes: {vote_count}
    ----------------------------------
    Candidates: {podium} with {[count[1]/vote_count*100 for count in podium]}%, respectively
    ----------------------------------
    Winner: {podium[0][0]} with {round((podium[0][1])/vote_count*100, 3)}% of the vote for a total of {podium[0][1]} votes!
    '''
print(election)

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