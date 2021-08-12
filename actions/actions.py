# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_greet_with_name")

        return [SlotSet("is_logged_in", True)]


class ActionManyEvents(Action):
    def name(self) -> Text:
        return "action_return_many_events"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [
            SlotSet("is_logged_in", True),
            SlotSet("name", "John"),
            Restarted(),
            AllSlotsReset(),
        ]


class ActionAuthrorizeUser(Action):
    def name(self) -> Text:
        return "action_authorize_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        username = tracker.slots["name"]
        if username == "John":
            return [SlotSet("is_logged_in", True)]
        else:
            return [SlotSet("is_logged_in", False)]


class ActionAgentAvailable(Action):
    def name(self) -> Text:
        return "action_agent_available"

    def _is_agent_available(self):
        # call backend to check if an agent is available
        pass

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        if self._is_agent_available():
            return [SlotSet("is_agent_availble", True)]
        else:
            return [SlotSet("is_agent_available", False)]
