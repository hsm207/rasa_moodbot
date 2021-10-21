FROM rasa/rasa:2.8.11-full

USER root
RUN apt update && \
    apt install -y git \
        make