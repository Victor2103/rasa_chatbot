import pandas as pd

df = pd.read_csv("topical_chat.csv", sep=",")

count = 0
present = []

#print(df)

for i in df["sentiment"]:
    if i not in present:
        present.append(i)
        count += 1