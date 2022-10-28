FROM python:3.8

WORKDIR /workspace
ADD . /workspace

RUN pip install --no-cache-dir -r requirements_rasa.txt


RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace



EXPOSE 5005
CMD rasa run -m models --enable-api --cors '*' -i 127.0.0.1