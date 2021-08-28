FROM rasa/rasa:2.8.3-full

USER root
RUN apt update && \
    apt install -y git \
        wget

RUN pip install black