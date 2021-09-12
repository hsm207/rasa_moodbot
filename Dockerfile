FROM rasa/rasa:latest-full

USER root
RUN apt update && \
    apt install -y git \
        make

# install the latest master of Haystack
RUN pip install grpcio-tools==1.34.1 \
    git+https://github.com/deepset-ai/haystack.git

RUN pip install black \
    jupyterlab \
    pytest