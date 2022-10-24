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





with open("yml_test/domain.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\nintents: \n')
    for j in intents:
        f.write(f'  - {j}\n')
    f.write('\nresponses:\n')
    for j in intents:
        f.write(
            f'  utter_{j}:\n  - text: "Write here the response of the chatbot."\n\n')
    f.write("session_config:\n  session_expiration_time: 60\n  carry_over_slots_to_new_session: true")