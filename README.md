# README

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
docker build . -t <yourdockerhubId>/big_chatbot:latest
docker push <yourdockerhubId>/big_chatbot:latest
```

# Create 2 tokens

One token is for operate the notebook and all of the work related to the rasa chatbot, the other to see the work I have done. One token is in read only and the other is only for the administrator.

```bash
ovhai token create -l model=rasabotRO --role read token-RO-chatbot
ovhai token create -l model=rasabotRW --role operator token-RW-chatbot
```

For each line, a value of the token is written. Don’t forget to save it because you can’t get it after this. Now when we create all of are product in OVH, we just have to add the label as options to have only access with the tokens and not with users. With this option, our connection is more secure.

# Create a VS code notebook and connect to remote on it (Not neccessarily).

Here is the command to create the notebook. We add two tokens. One for RO only and the other for read and write.

```bash
ovhai notebook run conda vscode \
--name vscode-ovh-machine \
--framework-version conda-py39-cuda11.2-v22-4 \
--volume <read-only-name-of-container>@<region>/nb-data:/workspace/data:RO:cache \
--volume <write-name-container>@<region>/:/workspace/saved_models:RW \
--volume https://github.com/Victor2103/rasa_chatbot.git:/workspace/public-repo-git:RO \
--cpu 10 \
--token <token> \
--label model=rasabotRO \
-s ~/.ssh/id_rsa.pub
```

You can also of course stop the notebook when you want. It is really advice to stop the notebook when you don’t using it. With the CLI command, you can restart the notebook when you want. To do this, get the ID of your notebook with “ovhai notebook ls” and then run

```bash
ovhai notebook stop <jobid>
```

To re run the notebook just launch

```bash
ovhai notebook start --token <token> <jobid>
```

Once your notebook is running, open a terminal and go into the folder public-repo-git. Then install pip with conda and install the requirements for rasa with the file requirements_rasa.txt. Here are the command to do so. You can after this train the model. To do this, you can connect in a terminal by ssh in your machine or connect on the browser with the token we create before.

```bash
ssh <notebook-id>@<region>.training.ai.cloud.ovh.net
```

```bash
conda install pip
python3 -m pip install --no-cache-dir -r requirements_rasa.txt
cd rasa_bot/
rasa train
```

If you want to save the model in your object storage, put your model on the folder saved_model. Then, he will be available on the private container <writenamecontainer> at the root. 

# Train the model on the cloud with the tool AI Training

Here is the command to launch on the cli command. You must have the cli command install. You also have to create a public cloud project and an user connected with the ovhai command. See further information in user management on the ovhcloud control panel. Here is the command to launch :

```bash
ovhai job run <yourdockerhubId>/big_chatbot:latest \
--gpu 2 \
--volume <containerwithdata>@<region>/:/workspace/data:RO \
--volume <containerforsavingthemodel>@<region>/rasa-models:/workspace/rasa_bot/models:RW \
-- bash -c "cd rasa_bot && rasa train --force --fixed-model-name customer-model"
```

Once the job is over, your model will be in the object storage <containerforsavingthedata> mounted in rasa-models. You can download it and put it in the folder rasa_bot/models. With this, you will be able to have a model in your machine. You can test it locally by running “rasa shell” directly in your machine in the directory rasa_bot. 

If you want to launch the job again to get a new model because your model is note precise, run :

```bash
ovhai job rerun <jobid> \
--gpu 4 \
--volume <containerwithdata>@<region>/:/workspace/data:RO \
--volume <containerforsavingthemodel>@<region>/rasa-models:/workspace/rasa_bot/models:RW \
-- bash -c "cd rasa_bot && rasa train --force --fixed-model-name customer-model"
```

Now that you have a model, we can deploy it to use it with a framework. 

# Deploy your model

Rasa framework provides an api with your model. So, we have to make only the front end if we want to use our model. To deploy the rasa model, you have to create a docker file, push it to your dockerhub and then run an app with the ovhai control command. Here is the command to create and push the docker image. 

```bash
docker build . -f deploy.Dockerfile -t <yourdockerhubId>/rasa-model:latest
docker push <yourdockerhubId>/rasa-model:latest
```

Once you docker image is pushed, you can create the app by running this command which use the ovhai control command. 

```bash
ovhai app run –name rasa-model \
–token <token> \
–default-http-port 5005 \
–cpu 4 \
<yourdockerhubId>/rasa-model:latest
```

Now, you can wait that your app is started. Once she is started, you can go into the url and connect with the token you provide juste before. 

To use the API, we can make some post requests or some get requests to use the model and predict some message. Here are some examples of get and post requests with curl. The output will be save in a file called “output.json”. Verify that the response in rasa is send in json, for example the get request of the base url is not a json file.  

## Get request

Here are two examples of get request, one will give us the response when we go to the url and the other will give us the version of the rasa model. 

```bash
curl -H “Authorization: Bearer <token>" \
https://<appid>.app.gra.training.ai.cloud.ovh.net/ > output.txt
```

```bash
curl -H “Authorization: Bearer <token>" \
https://<appid>.app.gra.training.ai.cloud.ovh.net/version > output.json
```

## Post request

```bash
curl -X POST \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"sender":"test_user","message":"I go with my bike at work"}' \
https://<appid>.app.gra.training.ai.cloud.ovh.net/webhooks/rest/webhook \
> output.json
```

```bash
curl -X POST \
-H 'Authorization: Bearer <token>' \
-H 'Content-Type: application/json' \
-d ‘{“text”:“I go to work with my bike”}’ \
https://<appid>.app.gra.training.ai.cloud.ovh.net/model/parse > output.json
```

If you want to use more functionnality, please fill free to go into this link provide by Rasa, which show all of the requests we can do with the api. 

[Rasa & Rasa Pro Documentation](https://rasa.com/docs/rasa/pages/http-api/)

Here is also a link to postman who shows us how to use the restfull api with some littles examples. 

[Official Rasa Workspace | Postman API Network](https://www.postman.com/rasahq/workspace/official-rasa-workspace/overview)

# Stop your app when unused

When you finish to use your model, don’t forget to stop the app. To do this simply run in the terminal : 

```bash
ovhai app stop <appid>
```

If you want to restart the rasa api, simply run again in a terminal : 

```bash
ovhai app start --token <token> \
<appid>
```