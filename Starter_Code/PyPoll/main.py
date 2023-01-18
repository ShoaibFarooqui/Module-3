import os
import csv

absolute_path = os.path.dirname(__file__)
relative_path = os.path.join(absolute_path, "Resources", "election_data.csv")

with open(relative_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    total_vote = []
    results = {}

    for row in csv_reader:
        vote = row[2]
        total_vote.append(vote)
        #counting votes for each candidate
        if vote in results:
            results[vote] += 1
        else:
            results[vote] = 1

    vote_count = len(total_vote)

    #sorted() seemed to be the only feasible way to order the dictionary by the values rather than keys, calling lambda function
    podium = sorted(results.items(), key=lambda x:x[1], reverse=True)
    #podium is a list of tuples containing name and votes received in descending order (podium[0] is winner)

    election = f'''
    Election Results
    ----------------------------------
    Total Votes: {vote_count}
    ----------------------------------
    Candidates: 
    {podium[0][0]} with {round((podium[0][1])/vote_count*100, 3)}% ({podium[0][1]} votes)
    {podium[1][0]} with {round((podium[1][1])/vote_count*100, 3)}% ({podium[1][1]} votes)
    {podium[2][0]} with {round((podium[2][1])/vote_count*100, 3)}% ({podium[2][1]} votes)
    ----------------------------------
    Winner: {podium[0][0]} with {round((podium[0][1])/vote_count*100, 3)}% of the vote for a total of {podium[0][1]} votes!
    '''

print(election)

with open("Starter_Code/analysis/PyPoll_Output.txt", 'w') as out:
    out.write(election)
