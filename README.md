# test

# Documentation chat bot to the cloud

I decided here to create a chat bot from scratch with the framework rasa. My first chatbot will an assistant chatbot for a customer. It is a kind of help where a client want for example information with a command he made on the website or want to complaint. So I have to found some data about this topic. 

The problem was the data was in a format where we can’t directly use it. Rasa framework use “.yml” files. Most of the dataset I found are in “.csv” files. To transform the files, I use some files organize in the folder “process_data”. 

Here is the main file of data in rasa. It is called by default the “nlu.yml” files. In this file, we found specific intent with the name. For example, an intent can be “ask_for_a_command”. In one intent, we have examples of how the customer will be able to speak about the intent. An example of “ask_for_a_command” could be “Hi, i want to know if my command has been delivered.” More we provide some examples of intents, more the rasa chat bot will be efficient and useful. 

After provided all of the examples for the all of the intents, we have to provide a response to the intent of the customer. To do this, we also use a file called process_domain.py. This file will created the file “domain.yml” file. We can found the response of the intents provided. In my example, the response of the chatbot will just be “Hi we detect the intent : ask_for_a_command” if the user ask for a command. 

The last file to create is the “rules.yml”. This one specify what the chat bot do every time he found a specific intent. It can be for example when a user say hello respond with hello. In this file, I decided to say to the chatbot, if you found a intent respond with I detect this intent. The file to do this is named “process_rules.py”. 

Here is a small diagram to understand the concept of the rasa files. 

# Create the docker image

Here is the commande to create the Docker Image and to push it on my private docker directory. The image will be by default public on your private directory.

```bash
docker build . -t vvitcheff/big_chatbot:latestdocker push vvitcheff/big_chatbot:latest
```

# Train the model on the cloud with the tool AI Training

Here is the command to launch on the cli command. You must have the cli command install. You also have to create a public cloud project and an user connected with the ovhai command. See further information in user management on the ovhcloud control panel. Here is the command to launch :

```bash
ovhai job run vvitcheff/big_chatbot:latest \
--gpu 4 \
--volume myprivatecontainer@GRA/:/workspace/data:RO \
--volume models-to-save@GRA/rasa-models:/workspace/rasa_bot/models:RW \
-- bash -c "cd rasa_bot && rasa telemetry disable && rasa train --force --fixed-model-name customer-model"
```