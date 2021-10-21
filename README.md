# Introduction

This repo shows a bug to when calling the callback endpoint

# Steps
1. Open this project in a container in VS Code
2. Run `make run-bot`
3. Execute:
```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"sender":"test_user", "message":"/greet"}' \
     http://localhost:5005/webhooks/callback/webhook
```
# References
1. [Bug report](https://github.com/RasaHQ/rasa/issues/9951)