import json

with open("output/train/output.json") as f:
    data = json.load(f)

# print(data["rasa_nlu_data"]["common_examples"])

# Take only the example we need.
my_data = data["rasa_nlu_data"]["common_examples"]


#Make a table with the name of the intents. 
intents=[]
for i in my_data:
    if i["intent"] in intents:
        pass
    else:
        intents.append(i["intent"])


with open("../rasa_bot/data/rules.yml", "w", encoding="utf-8") as f:
#with open("yml_test/rules.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\n\nrules:\n')
    for i in intents:
        f.write(f'- rule: Detect {i} when the user want to do this \n  steps:\n  - intent: {i}\n  - action: utter_{i}\n\n')