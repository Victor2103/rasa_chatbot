import pandas as pd

df = pd.read_csv("Customer_data.csv", sep=",")

count = 0
present = []

#print(df)

for i in df["intent"]:
    if i not in present:
        present.append(i)
        count += 1

# print(count)
#print(present)

for i in range(0, count):
    exec(f'table_{i} = []')

# print(df["message"].to_numpy())

# Transform all the message into an array
text = df["utterance"].to_numpy()

# Get the name of each sentiment and save all the conversation id related to the sentiment
for i in range(len(df["utterance"])):
    # We add the number of the conversation in the table corresponding to the sentiment
    for j in range(count):
        if (df["intent"].values[i] == present[j]):
            exec(f"table_{j}.append(i)")

# Save in a nlu file all of the entries.
# The most difficult was the indentation in this yml langage. 
#with open("nlu.yml", "w", encoding="utf-8") as f:
with open("../rasa_bot/data/nlu.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\n')
    f.write('nlu:\n')
    for i in range(count):
        #Don't forget to replace the space of intent with underscore
        f.write(f"- intent: {present[i].replace(' ','_')}\n  examples: |\n")
        for j in globals()[f"table_{i}"]:
            # print(df["message"].values[i])
            f.write(f"    - {df['utterance'].values[j]}\n")
    
