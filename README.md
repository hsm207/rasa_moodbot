# Introduction

This repo shows how to view the Rasa events that get passed to a RabbitMQ event broker.


# Usage
1. Run `docker-compose up`
2. Use the [rest_calls.http](./rest_calls.http) with the `humao.rest-client` VS Code extension to talk to the bot
3. Goto `localhost:1572` to view the RabbitMQ queue console. The username and password is `guest`.