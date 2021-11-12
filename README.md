# Introduction

This repo demonstrates:
* how to write and test stories that call a form when there aren't any rules to activate deactivate the form
* rules do not need to mach all featurized slots at run time for it to trigger

Note that the bot's policy uses `MemoizationPolicy` and `RulePolicy` only.
# Usage

Run `make test` to run end-to-end test.
Run `make run-action-server` to start the action server.
Run `make shell` to talk to the bot in the shell.
