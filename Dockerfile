FROM rasa/rasa:latest-full

USER root

RUN pip install locust
