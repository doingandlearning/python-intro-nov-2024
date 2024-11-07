import pandas as pd

score_data = pd.read_csv("scores.csv")
score_data["History_List"] = score_data["History"].map(eval)  # run the actual code
score_data["Score Lengths"] = score_data["History_List"].map(len)
print(score_data["Score Lengths"].describe())
print(score_data["Score Lengths"].plot())