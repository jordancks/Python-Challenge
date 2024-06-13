import csv


'''
name = "James"
number = 2
result = number * 2
name2 = ["First", 5, result]
print(name2)

print(name2[0])
for x in name2:
    print(x)

counter = 0


for x in range(len(name2)):
    print(name2[x])
    counter += 1

print(counter)
'''

moneyvalue = []


with open("PyBank/Resources/budget_data.csv") as data:
    reader = csv.reader(data)
    print(reader)
#Skips header row
    header = next(reader)
    for row in reader:
        print(row)
        moneyvalue.append(int(row[1]))
        
print(moneyvalue)




