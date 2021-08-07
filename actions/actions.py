# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Dict, List, Optional, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecutionRejected, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict


class ActionPrefillPhoneCallForm(Action):
    """
    Fills the `number` slot with `mobile_number` or `fixedline_number`
    """

    def name(self) -> Text:
        return "action_prefill_phonecall_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        fixedline_number = tracker.slots["fixedline_number"]
        mobile_number = tracker.slots["mobile_number"]

        number = mobile_number if mobile_number else fixedline_number
        return [SlotSet("number", number)]


class ValidatePhoneCallForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_phonecall_form"

    def _is_valid_number(self, phonenumber: Text) -> bool:
        """
        Checks if phonenumber is a valid number
        """
        return phonenumber == "110"

    def validate_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        retries = tracker.slots["retries"]

        if self._is_valid_number(slot_value):
            return {"number": slot_value, "is_valid_number": True}
        elif retries >= 3:
            dispatcher.utter_template("utter_giveup_number_validation", tracker)
            return [ActionExecutionRejected, {"is_valid_number": False}]
        else:
            dispatcher.utter_template("utter_invalid_number", tracker)
            return {"number": None, "retries": retries + 1, "is_valid_number": False}
