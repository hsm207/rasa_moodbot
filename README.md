# Introduction

This repo shows how to view the concept of a "session" in rasa.


# Usage
1. Run `docker-compose up`
2. Use the [rest_calls.http](./rest_calls.http) with the `humao.rest-client` VS Code extension to talk to the bot
3. Modify the value of `carry_over_slots_to_new_session` in (domain.yml)[domain.yml] to `false` and repeat step 2.