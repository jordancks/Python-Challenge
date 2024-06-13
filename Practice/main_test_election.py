# Define variables
import csv


total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Load and read CSV
file_path = "/Users/jordancks/Python-Challenge/PyPoll/Resources/election_data.csv"
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    
    next(csvreader) # Skip the header
    
    # Iterate through each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {"votes": votes, "percentage": percentage}
    
    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes


#Poll outcome
results=(
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, data in candidates.items():
    results += f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n"
results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print Poll
print(results)

# Export to text file
output_file = "election_results.txt"
with open(output_file, 'w') as file:
    file.write(results)
file.close()