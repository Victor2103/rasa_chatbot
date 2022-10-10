import pandas as pd

df = pd.read_csv("topical_chat.csv", sep=",")

count = 0
present = []

#print(df)

for i in df["sentiment"]:
    if i not in present:
        present.append(i)
        count += 1

print(present)
        
with open("domain.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\nintents: \n')
    for j in present:
        f.write(f'  -   {j.replace(" ","_")}\n')