FROM python:3.8

WORKDIR /workspace
ADD . /workspace

#RUN pip install --no-cache-dir -r requirements_rasa.txt
RUN pip install --no-cache-dir -r requirements_deploy.txt

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace


EXPOSE 5005
#EXPOSE 8000
#CMD cd rasa_bot; rasa run -m models --enable-api --cors '*'
CMD ./script.sh