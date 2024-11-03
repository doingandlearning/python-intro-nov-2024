import csv

data = []
filename = 'temperatures.csv'

print('Loading file', filename)
with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

print('Finished reading file')
print(data)
