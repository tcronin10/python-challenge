import os
import csv

PyPollcsv = os.path.join("Resources","election_data.csv")

#Generate Lists

count = 0
candidates = []
each_candidate = []

vote_count = []
vote_percent = []

#Open the CSV

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        #Total Votes
        count = count + 1
        #List candidates
        candidates.append(row[2])
       
    for x in set(candidates):
        each_candidate.append(x)
        #Set variable for total votes/candidate
        y = candidates.count(x)
        vote_count.append(y)
        #Set variable for percent of total votes/candidate 
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_total = max(vote_count)
    winner = each_candidate[vote_count.index(winning_vote_total)]
    

print("Election Results")   
print("Total Votes: " + str(count))    
for i in range(len(each_candidate)):
            print(each_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("The winner is: " + winner)


with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(count) + "\n")
    for i in range(len(set(each_candidate))):
        text.write(each_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("The winner is: " + winner + "\n")


