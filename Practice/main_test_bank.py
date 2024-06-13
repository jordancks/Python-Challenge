#Define Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]
changes = []

# Load and read CSV
file_path = "/Users/jordancks/Python-Challenge/PyBank/Resources/budget_data.csv"
with open(file_path, "r") as file:
    next(file)  # Skip the header
    for line in file:
        data = line.strip().split(",")
        date = data[0]
        profit_loss = int(data[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate changes in profit/losses
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            total_change += change
            changes.append(change)

            # Find the greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)

#Analysis outcome
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print analysis
print(results)



# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as file:
    file.write(results)
file.close()
