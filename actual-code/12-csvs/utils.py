import ast
import csv
import datetime


def save_score(guess_history, username):
    new_score = {
        "Username": username,
        "History": guess_history,
        "Date": datetime.date.today()
    }
    with open("scores.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["Date", "Username", "History"])
        writer.writerow(new_score)

def average_number_of_guesses():
    # open the file
    lengths = []
    with open("scores.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lengths.append(len(ast.literal_eval(row["History"])))
    return sum(lengths)/len(lengths)

print(average_number_of_guesses())