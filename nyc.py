# Dennis O'Leary
# NYC Jobs Data

import os
import csv

# input file path
csvpath = os.path.join("Resources", "nyc.csv")

# lists to store data
agencies = []


# opens input file, removes header row and loops through the remaining rows
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        agencies.append(row[1])

# remove duplicates from agencies list
agencies = list( dict.fromkeys(agencies))

print(agencies)
print(str(len(agencies)))