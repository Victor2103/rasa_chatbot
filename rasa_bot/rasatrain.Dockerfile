FROM python:3.8

WORKDIR /workspace
ADD . /workspace


RUN pip install --no-cache-dir -r requirements_rasa.txt

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

CMD rasa train --force --out trained-models