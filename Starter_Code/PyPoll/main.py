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

    for row in csv_reader:
        print(row)