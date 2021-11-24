# Introduction

This repo shows how a FollowupAction event interacts with  UserUtteranceReverted event

# Usage

1. Run `make run-action-server` to start an action server
2. Run `make run-shell` to start a rasa shell
3. Input `/trigger_fallback` to trigger the demo

# Details

1. Read implementation of the custom `action_default_fallback` in [actions.py](./actions/actions.py)
2. Observe the logs of the action server to see which custom actions are being requested by rasa oss server