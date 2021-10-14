# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import logging
import re
from typing import Any, Dict, List, Optional, Text

from rasa_sdk import Action, FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ValidatePhonenumberForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_phonenumber_form"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        required_slots = ["phone_number"]
        return required_slots

    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value is None:
            return {"phone_number": None}

        if re.match(r"^\(\+\d{1,}\)", slot_value):
            return {"phone_number": slot_value}
        else:
            dispatcher.utter_message(
                "I said enter your phone number with country code!"
            )
            return {"phone_number": None}

    async def extract_phone_number(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:

        duckling_phone = [
            e.get("value")
            for e in tracker.latest_message["entities"]
            if e.get("entity") == "phone-number"
        ]

        if len(duckling_phone) == 0:
            return {"phone_number": None}
        else:
            return {"phone_number": duckling_phone[0]}
