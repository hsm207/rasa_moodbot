# Introduction

This repo demonstrates how to use [locust](https://locust.io/) to load test a Rasa bot.

See [locustfile.py](./locustfile.py) to find out what conversations get tested.

# Requirements

1. VS Code
2. Docker

# Usage

1. Open this project in VS Code inside a container using the [Dockerfile](./Dockerfile).
2. Train the bot with `rasa train`
3. Run the rasa server with `rasa run --enable-api -vv`
4. In another terminal, start the locust Web UI with `locust`.
5. Navigate to the Web UI and follow the prompts to start the load test