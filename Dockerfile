FROM rasa/rasa:latest-full

USER root
RUN apt update && \
    apt install -y git
    
RUN pip install black \
    pytest \
    tox