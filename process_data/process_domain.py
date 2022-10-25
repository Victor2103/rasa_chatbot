import pandas as pd

df = pd.read_csv("Customer_data.csv", sep=",")

count = 0
present = []

# print(df)

for i in df["intent"]:
    if i not in present:
        present.append(i)
        count += 1


# Transform in the table the space with an underscore
for i in range(len(present)):
    present[i] = present[i].replace(" ", "_")
print(present)

#with open("yml_test/domain.yml", "w", encoding="utf-8") as f:
with open("../rasa_bot/domain.yml", "w", encoding="utf-8") as f:
    f.write('version: "3.1"\nintents: \n')
    for j in present:
        f.write(f'  - {j}\n')
    f.write('\nresponses:\n')
    for j in present:
        f.write(
            f'  utter_{j}:\n  - text: "We detect this kind of intent : {j}."\n\n')
    f.write("session_config:\n  session_expiration_time: 60\n  carry_over_slots_to_new_session: true")
