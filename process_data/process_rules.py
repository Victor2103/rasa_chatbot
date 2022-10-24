import pandas as pd

df = pd.read_csv("Customer_data.csv", sep=",")

count = 0
present = []

print(df.info())

for i in df["intent"]:
    if i not in present:
        present.append(i)
        count += 1


# Transform in the table the space with an underscore
for i in range(len(present)):
    present[i] = present[i].replace(" ", "_")
print(present)


#In period of test use the first line of command else use the second line
#with open("yml_test/rules.yml", "w", encoding="utf-8") as f:
with open("../rasa_bot/data/rules.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\n\nrules:\n')
    for i in present:
        f.write(f'- rule: Detect {i} when the user want to do this \n  steps:\n  - intent: {i}\n  - action: utter_{i}\n\n')