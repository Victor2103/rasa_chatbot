import json

with open("output/train/output.json") as f:
    data = json.load(f)

# print(data["rasa_nlu_data"]["common_examples"])

# Take only the example we need.
my_data = data["rasa_nlu_data"]["common_examples"]


# Make a table with the name of the intents.
intents = []
for i in my_data:
    if i["intent"] in intents:
        pass
    else:
        intents.append(i["intent"])

# Make a table with the name entities to add it in the domain
entities = []
for i in my_data:
    if (len(i["entities"]) != 0):
        if i["entities"][0]["entity"] not in entities:
            entities.append(i["entities"][0]["entity"])

# print(entities)


with open("../rasa_bot/domain.yml", "w", encoding="utf-8") as f:
    # with open("yml_test/domain.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\nintents: \n')
    # Write the intents
    for j in intents:
        f.write(f'  - {j}\n')
    # Write the entities
    f.write('\nentities:\n')
    for j in entities:
        f.write(f"- {j}\n")
    # Write the slots for the memory of the bot.
    f.write('\nslots:\n')
    for j in entities:
        f.write(f"  {j}:\n    type: text\n    influence_conversation: false\n    mappings:\n    - type: from_entity\n      entity: {j}\n")
    # Write the response of the bot for each intent.
    f.write('\nresponses:\n')
    for j in intents:
        f.write(
            f'  utter_{j}:\n  - text: "Write here the response of the chatbot."\n\n')
    f.write("session_config:\n  session_expiration_time: 60\n  carry_over_slots_to_new_session: true")
