FROM rasa/rasa:2.8.28-full

USER root
RUN apt update && \
    apt install -y git