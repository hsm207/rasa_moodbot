
## happy path 1
* greet: hi
  - utter_greet
* mood: my mood is [high](mood)
  - utter_happy

## sad path 3
* greet: hi
  - utter_greet
* mood: my mood is [low](mood)
  - utter_cheer_up
  - utter_did_that_help
* affirm: yes
  - utter_happy

##  other path 1
* greet: hi
  - utter_greet
* mood: my mood is [good](mood)
  - utter_other

##  other path 2
* greet: hi
  - utter_greet
* mood: my mood is [medium](mood)
  - utter_other

##  none path
* greet: hi
  - utter_greet
* mood: my mood is 
  - utter_none