FROM rasa/rasa:2.3.5-full

USER root
RUN apt update && \
    apt install -y git \
        make