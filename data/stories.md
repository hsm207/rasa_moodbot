## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## happy path 1
* greet
  - utter_greet
* mood{"mood": "high"}
  - slot{"mood": "high"}
  - utter_happy

## sad path 3
* greet
  - utter_greet
* mood{"mood": "low"}
  - slot{"mood": "low"}
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

##  other path
* greet
  - utter_greet
* mood{"mood": "__other__"}
  - slot{"mood": "__other__"}
  - utter_other


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
