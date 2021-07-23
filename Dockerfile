FROM rasa/rasa:latest

USER root
RUN apt update && \
    apt install -y git

RUN pip install black