# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import logging

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction, SlotSet, UserUtteranceReverted
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionTest(Action):
    """Test action."""

    def name(self) -> str:
        return "action_test"

    async def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="called action_test")
        return [SlotSet("home_city", "Berlin")]

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return "action_default_fallback"

    async def run(
        self,
        dispatcher,
        tracker,
        domain,
    ):
        dispatcher.utter_message("called action_default_fallback")

        results = await ActionTest().run(dispatcher, tracker, domain)

        return [
            SlotSet("age", "100"), # this will not be set because of UserUtteranceReverted()
            FollowupAction("action_test"), # won't be executed because of UserUtteranceReverted()
            UserUtteranceReverted(),
            results[0], # this will be set because it is after UserUtteranceReverted()
        ]