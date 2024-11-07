import csv

with open("movies.csv") as f:
    reader = csv.reader(f)

    next(reader)  # skips a line  - we have to skip the header row!
    for row in reader:
        print(f"{row[0]} was made in {row[1]}")  # each row is a list

with open("movies.csv") as f:
    reader = csv.DictReader(f)  # needs a header and uses the header to create a Dict for each row
    for row in reader:
        print(f"{row["Title"]} was made in {row["Year"]}")  # each row is a dict
