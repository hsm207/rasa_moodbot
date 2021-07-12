# Introduction

Working with Telemetry:

1. Implicit telemetry:
   ```bash
   rasa train
   ```
2. To view the telemetry data:
   ```bash
   RASA_TELEMETRY_DEBUG=true rasa train --force
   ```
3. To tell telemetry it is in CI:
   ```bash
   RASA_TELEMETRY_DEBUG=true CI=true rasa train --force
   ```
4. Not defining the CI variable is still `ci: true`!:
   ```bash
   RASA_TELEMETRY_DEBUG=true CI=${CI} rasa train --force
   ```