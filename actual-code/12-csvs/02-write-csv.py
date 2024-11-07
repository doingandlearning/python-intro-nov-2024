import csv

new_movie = ["Inception 2", "2024", "Action, Sci-fi"]

with open("movies.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(new_movie)

new_movie_dict = {
    "Genre": "Sci-fi, Kids",
    "Year": 2012,
    "Title": "Wall-e"
}

with open("movies.csv", "a") as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Year", "Genre"])
    writer.writerow(new_movie_dict)
