from typing import Any, Dict, List, Text
from rasa.shared.constants import DEFAULT_NLU_FALLBACK_INTENT_NAME

from rasa.shared.core.constants import ACTION_DEFAULT_ASK_AFFIRMATION_NAME, ACTION_DEFAULT_ASK_REPHRASE_NAME, USER_INTENT_OUT_OF_SCOPE
from rasa.shared.nlu.constants import INTENT_NAME_KEY, INTENT_RANKING_KEY
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDefaultAskAffirmation(Action):
    def name(self) -> Text:
        return ACTION_DEFAULT_ASK_AFFIRMATION_NAME

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        latest_message = tracker.latest_message

        intent_to_affirm = latest_message["intent"].get(INTENT_NAME_KEY)

        intent_ranking = latest_message.get(INTENT_RANKING_KEY) or []
        if (
            intent_to_affirm == DEFAULT_NLU_FALLBACK_INTENT_NAME
            and len(intent_ranking) > 1
        ):
            intent_to_affirm = intent_ranking[1][INTENT_NAME_KEY]

        affirmation_message = f"I don't understand what you just said\nDid you mean '{intent_to_affirm}'?"

        dispatcher.utter_message(text = affirmation_message, buttons=[
                {"title": "Yes", "payload": f"/{intent_to_affirm}"},
                {"title": "No", "payload": f"/{USER_INTENT_OUT_OF_SCOPE}"},
            ])
        
        return []

class ActionDefaultAskRephrase(Action):
    def name(self) -> Text:
        return ACTION_DEFAULT_ASK_REPHRASE_NAME

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Please rephrase")
        dispatcher.utter_message("Thanks")

        return []