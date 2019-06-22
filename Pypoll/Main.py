import os
import csv

candidate_percentages ={}
winner_votes = 0
winner = ""
total_votes = 0
candidate = ""
candidate_votes = {}


# open csv file
election_csv = os.path.join('election_data.csv')
with open(election_csv,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1


for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# print out results

print("Election Results")
print(f"Total Votes: {total_votes}")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(f"Winner: {winner}")

# save 

filepath = os.path.join("pypoll_output.txt")
with open(filepath,'w') as text:
 
    text.write(f"Total Votes: {total_votes}" + "\n")

    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
 
    text.write(f"Winner: {winner}" + "\n")