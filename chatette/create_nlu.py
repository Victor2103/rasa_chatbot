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

# Count the number of intent in the json file.


with open("nlu.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\n')
    f.write('nlu:\n')
    for i in intents:
        f.write(f"- intent: {i}\n  examples: |\n")
        for j in my_data:
            if (j["intent"]==i):
                f.write(f"    - {j['text']}\n")