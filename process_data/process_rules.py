import pandas as pd

df = pd.read_csv("topical_chat.csv", sep=",")

count = 0
present = []

# print(df)

for i in df["sentiment"]:
    if i not in present:
        present.append(i)
        count += 1


# Transform in the table the space with an underscore
for i in range(len(present)):
    present[i] = present[i].replace(" ", "_")
print(present)

with open("../rasa_bot/data/rules.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\n\nrules:\n')
    for i in present:
        f.write(f'- rule: Detect {i} when it is the right sentiment\n  steps:\n  - intent: {i}\n  - action: utter_{i}\n\n')