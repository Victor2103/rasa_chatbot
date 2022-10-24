import json

with open("output/train/output.json") as f:
    data = json.load(f)

# print(data["rasa_nlu_data"]["common_examples"])

# Take only the example we need.
intents = data["rasa_nlu_data"]["common_examples"]
print(intents[0])

# Count the number of intent in the json file.


with open("nlu.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\n')
    f.write('nlu:\n')
