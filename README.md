# Documentation chat bot to the cloud

I decided here to create a chat bot from scratch with the framework rasa. My first chatbot will an assistant chatbot for a customer. It is a kind of help where a client want for example information with a command he made on the website or want to complaint. So I have to found some data about this topic. 

The problem was the data was in a format where we can’t directly use it. Rasa framework use “.yml” files. Most of the dataset I found are in “.csv” files. To transform the files, I use some files organize in the folder “process_data”. 

Here is the main file of data in rasa. It is called by default the “nlu.yml” files. In this file, we found specific intent with the name. For example, an intent can be “ask_for_a_command”. In one intent, we have examples of how the customer will be able to speak about the intent. An example of “ask_for_a_command” could be “Hi, i want to know if my command has been delivered.” More we provide some examples of intents, more the rasa chat bot will be efficient and useful. 

After provided all of the examples for the all of the intents, we have to provide a response to the intent of the customer. To do this, we also use a file called process_domain.py. This file will created the file “domain.yml” file. We can found the response of the intents provided. In my example, the response of the chatbot will just be “Hi we detect the intent : ask_for_a_command” if the user ask for a command. 

The last file to create is the “rules.yml”. This one specify what the chat bot do every time he found a specific intent. It can be for example when a user say hello respond with hello. In this file, I decided to say to the chatbot, if you found a intent respond with I detect this intent. The file to do this is named “process_rules.py”. 

Here is a small diagram to understand what contains the nlu file.

[![](https://mermaid.ink/img/pako:eNpVkdtqwkAQhl9l2KsW1La3QRSPILS9sSdIRCbupFncQ9hsqqn67h2NtXZgYZmZ_5vTTqycJBGJT49FDi_jxALbIH5-fO3URkOmNC2g3e7tR84GVLbcw_BmZgPZABEMyvUyc36Jy5UzBq28bQDDk2SqfBmAtmgKTXsYxzPYIOuCg7V1G-jepb6nMjA1nOWNK8cSUiILkrT6Ik9ycY3tsMHklzqJR2ihdhUE0hoMNQxm2sqk5MFlF3r_H-cj5H_NTeP3nCsB8mNtmTsqod9lEszAoCQIOV1AGnmwDdG6sxAtYcgbVJLXuDvyE8GphhIR8VdShpUOiWhdhd7QK0w1lcecXdNTIjLe8Fx9n4UP98U2EU3skNgD18EquHltVyIKvqKWqAqJgcYK-XpGRBnqkr0kVXD-qbnr6byHHwI1oAA)](https://mermaid.live/edit#pako:eNpVkdtqwkAQhl9l2KsW1La3QRSPILS9sSdIRCbupFncQ9hsqqn67h2NtXZgYZmZ_5vTTqycJBGJT49FDi_jxALbIH5-fO3URkOmNC2g3e7tR84GVLbcw_BmZgPZABEMyvUyc36Jy5UzBq28bQDDk2SqfBmAtmgKTXsYxzPYIOuCg7V1G-jepb6nMjA1nOWNK8cSUiILkrT6Ik9ycY3tsMHklzqJR2ihdhUE0hoMNQxm2sqk5MFlF3r_H-cj5H_NTeP3nCsB8mNtmTsqod9lEszAoCQIOV1AGnmwDdG6sxAtYcgbVJLXuDvyE8GphhIR8VdShpUOiWhdhd7QK0w1lcecXdNTIjLe8Fx9n4UP98U2EU3skNgD18EquHltVyIKvqKWqAqJgcYK-XpGRBnqkr0kVXD-qbnr6byHHwI1oAA)

# Create the docker image

Here is the commande to create the Docker Image and to push it on my private docker directory. The image will be by default public on your private directory.

```bash
docker build . -t vvitcheff/big_chatbot:latest
docker push vvitcheff/big_chatbot:latest
```

# Create 2 tokens 

One token is for operate the notebook and all of the work related to the rasa chatbot, the other to see the work I have done. One token is in read only and the other is only for the administrator. 

```bash
ovhai token create -l model=rasabotRO --role read token-RO-chatbot
ovhai token create -l model=rasabotRW --role operator token-RW-chatbot
```

For each line, a value of the token is written. Don't forget to save it because you can't get it after this. Now when we create all of are product in OVH, we just have to add the label as options to have only access with the tokens and not with users. With this option, our connection is more secure. 

# Create a VS code notebook and connect to remote on it (Not neccessarily). 

Here is the comman to create the notebook. We add two tokens. One for RO only and the other for read and write. 

```bash
ovhai notebook run conda vscode \
--name vscode-ovh-machine \
--framework-version conda-py39-cuda11.2-v22-4 \
--volume myprivatecontainer@GRA/nb-data:/workspace/data:RO:cache \
--volume ai-notebook@GRA/:/workspace/saved_models:RW \
--volume https://github.com/Victor2103/rasa_chatbot.git:/workspace/public-repo-git:RO \
--cpu 10 \
--token ++9O7ZjOT8eEkAha1GywfOFQXnJvttgYXbmdBOxLS7sW/s4TqtdNJBVMqRav+vzO \
--label model=rasabotRO \
-s ~/.ssh/id_rsa.pub 
```

You can also of course stop the notebook when you want. It is really advice to stop the notebook when you don't using it. With the CLI command, you can restart the notebook when you want. To do this, get the ID of your notebook with "ovhai notebook ls" and then run 

```bash
ovhai notebook stop <jobid>
```

To re run the notebook just launch 

```bash
ovhai notebook start --token ++9O7ZjOT8eEkAha1GywfOFQXnJvttgYXbmdBOxLS7sW/s4TqtdNJBVMqRav+vzO <jobid>
```

Once your notebook is running, open a terminal and go into the folder public-repo-git. Then install pip with conda and install the requirements for rasa with the file requirements_rasa.txt. Here are the command to do so. You can after this train the model. To do this, you can connect in a terminal by ssh in your machine or connect on the browser with the token we create before. 

```bash
ssh 4eb28334-ff26-475f-8233-2a2769f8f3b2@gra.training.ai.cloud.ovh.net
```

```bash
conda install pip
python3 -m pip install --no-cache-dir -r requirements_rasa.txt
cd rasa_bot/
rasa train
```

If you want to save the model in your object storage, put your model on the folder saved_model. 

# Train the model on the cloud with the tool AI Training

Here is the command to launch on the cli command. You must have the cli command install. You also have to create a public cloud project and an user connected with the ovhai command. See further information in user management on the ovhcloud control panel. Here is the command to launch :

```bash
ovhai job run vvitcheff/big_chatbot:latest \
--gpu 2 \
--volume myprivatecontainer@GRA/:/workspace/data:RO \
--volume models-to-save@GRA/rasa-models:/workspace/rasa_bot/models:RW \
-- bash -c "cd rasa_bot && rasa telemetry disable && rasa train --force --fixed-model-name customer-model"
```

If you want to launch the job again to get a new model, run : 

```bash
ovhai job rerun a85c1179-49b9-4666-b988-95571e1f68c0 \
--gpu 4 \
--volume myprivatecontainer@GRA/:/workspace/data:RO \
--volume models-to-save@GRA/rasa-models:/workspace/rasa_bot/models:RW \
-- bash -c "cd rasa_bot && rasa telemetry disable && rasa train --force --fixed-model-name customer-model" 
```

docker build . -f deploy.Dockerfile -t vvitcheff/django-rasa:latest

docker push vvitcheff/django-rasa:latest

ovhai app run --name django-rasa --token ++9O7ZjOT8eEkAha1GywfOFQXnJvttgYXbmdBOxLS7sW/s4TqtdNJBVMqRav+vzO --default-http-port 8000 --cpu 4