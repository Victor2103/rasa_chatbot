FROM python:3.8

WORKDIR /workspace
ADD . /workspace


RUN pip install --no-cache-dir -r rasa_bot/requirements_rasa.txt

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

