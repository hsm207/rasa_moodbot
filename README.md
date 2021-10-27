# Introduction

Checks what effect long running actions have on rasa shell.

# Usage

1. Open project in a container
2. Run `make build-shell` and `build-rest` to talk to the bot using the shell and REST channel respectively.
3. Trigger a long running custom action with `/trigger_sleep_sync{"sleep_time":15}` in both channels with varying sleep times and observe the results.

# Notes

1. The shell will timeout after 10 seconds by default. To configure this, set the `RASA_SHELL_STREAM_READING_TIMEOUT_IN_SECONDS` environment variable.
2. The timeout only happens in the shell channel because the bot just freezes if it runs into an error when making predictions.