from typing import Any, Dict, List, Text
from rasa.shared.constants import DEFAULT_NLU_FALLBACK_INTENT_NAME

from rasa.shared.core.constants import (
    ACTION_DEFAULT_ASK_AFFIRMATION_NAME,
    ACTION_DEFAULT_ASK_REPHRASE_NAME,
    USER_INTENT_OUT_OF_SCOPE,
    ACTION_DEFAULT_FALLBACK_NAME,
)
from rasa.shared.nlu.constants import INTENT_NAME_KEY, INTENT_RANKING_KEY
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    FollowupAction,
    UserUtteranceReverted,
    ConversationPaused,
)
import logging

UPPER_BOUND = 0.95
LOWER_BOUND = 0.50


def get_non_fallback_intent(intent_ranking):
    _, intent_name, intent_confidence = (
        intent_ranking[1].values()
        if len(intent_ranking) > 1
        else intent_ranking[0].values()
    )
    return intent_name, intent_confidence


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

        intent_name, intent_confidence = get_non_fallback_intent(intent_ranking)
        logging.debug(
            f"Top non nlu_fallback intent is: {intent_name}({intent_confidence})"
        )

        if intent_confidence <= LOWER_BOUND:
            logging.debug(f"Going straight to {ACTION_DEFAULT_FALLBACK_NAME}")
            return [
                UserUtteranceReverted(),
                FollowupAction(ACTION_DEFAULT_FALLBACK_NAME),
            ]

        if (
            intent_to_affirm == DEFAULT_NLU_FALLBACK_INTENT_NAME
            and len(intent_ranking) > 1
        ):
            intent_to_affirm = intent_ranking[1][INTENT_NAME_KEY]

        affirmation_message = (
            f"I don't understand what you just said\nDid you mean '{intent_to_affirm}'?"
        )

        dispatcher.utter_message(
            text=affirmation_message,
            buttons=[
                {"title": "Yes", "payload": f"/{intent_to_affirm}"},
                {"title": "No", "payload": f"/{USER_INTENT_OUT_OF_SCOPE}"},
            ],
        )

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


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return ACTION_DEFAULT_FALLBACK_NAME

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("I'm sorry I could not help you")
        dispatcher.utter_message("I will pass you to a human")
        return [ConversationPaused()]
