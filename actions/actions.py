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
from datetime import datetime


class ActionMakeBooking(Action):
    def name(self) -> Text:
        return "action_make_booking"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        c = datetime.now()
        current_date = str(c.date())
        current_time = str(c.time())

        dispatcher.utter_message(f"Made a booking on {current_date} at {current_time}")

        return [SlotSet("book_date", current_date), SlotSet("book_time", current_time)]

class ActionRepeat(Action):
    def name(self) -> Text:
        return "action_repeat"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(f"Repeat previous utterance")

        return []