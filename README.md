# Documentation chat bot to the cloud

# Create the docker image

Here is the commande to create the Docker Image and to push it on my private docker directory. The image will be by default public on your private directory. 

```bash
docker build . -t vvitcheff/big_chatbot:latest
docker push vvitcheff/big_chatbot:latest
```

# Train the model on the cloud with the tool AI Training

Here is the command to launch on the cli command. You must have the cli command install. You also have to create a public cloud project and an user connected with the ovhai command. See further information in user management on the ovhcloud control panel. Here is the command to launch : 

```bash
ovhai job run vvitcheff/big_chatbot:latest \
--gpu 4 \
--volume myprivatecontainer@GRA/:/workspace/data:RO \
--volume models-to-save@GRA/rasa-models:/workspace/rasa_bot/models:RWD \
-- bash -c "cd rasa_bot && rasa telemetry disable && rasa train --force --fixed-model-name customer-model"
``` 