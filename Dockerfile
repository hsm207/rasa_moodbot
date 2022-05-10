FROM rasa/rasa:2.8.27-full

USER root

RUN apt update && \
    apt install -y make

RUN pip install debugpy