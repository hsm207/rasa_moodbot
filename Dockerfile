FROM rasa/rasa:2.8.15-full

USER root
RUN apt update && \
    apt install -y git \
        make

RUN pip install black \
    pytest