# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import logging

class ActionValidateUserInput(Action):
    MAX_RETRIES = 3

    def name(self) -> Text:
        return "action_validate_user_input"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_input = int(tracker.latest_message["text"])
        num_retries = tracker.get_slot("num_retries")

        logging.info(f"Num retries is {num_retries}")

        # validation logic here
        if user_input >= 1 and user_input <= 10:
            
            return [SlotSet("num_retries", 0), SlotSet("user_number", user_input), SlotSet("is_validated", True)]

        elif num_retries <= self.MAX_RETRIES:
            
            dispatcher.utter_message(template="utter_try_again")
            
            return [SlotSet("num_retries", num_retries + 1)]

        else:
            return [SlotSet("is_retry_limit", True)]

        

        return []
