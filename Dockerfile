FROM rasa/rasa:3.0.0-full
# FROM rasa/rasa:2.8.15-full

USER root
RUN apt update && \
    apt install -y git \
        make