import json
import logging
from collections import ChainMap
from typing import Any, Dict, List, Text
from unittest import result

from rasa.shared.core.constants import (ACTION_DEFAULT_ASK_AFFIRMATION_NAME,
                                        USER_INTENT_OUT_OF_SCOPE)
from rasa.shared.nlu.constants import INTENT_RANKING_KEY
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


def get_non_fallback_intent(intent_ranking):
    _, intent_name, intent_confidence = (
        intent_ranking[1].values()
        if len(intent_ranking) > 1
        else intent_ranking[0].values()
    )
    return intent_name, intent_confidence


def extract_entities(entities):

    results = [{e["entity"]: e["value"]} for e in entities]
    results = dict(ChainMap(*results))
    results = json.dumps(results)

    return results


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

        entities = extract_entities(latest_message["entities"])
        logging.debug(f"Entities are {entities}")

        intent_ranking = latest_message.get(INTENT_RANKING_KEY) or []

        intent_name, intent_confidence = get_non_fallback_intent(intent_ranking)
        logging.debug(
            f"Top non nlu_fallback intent is: {intent_name}({intent_confidence})"
        )

        affirmation_message = (
            f"I don't understand what you just said\nDid you mean '{intent_name}'?"
        )

        dispatcher.utter_message(
            text=affirmation_message,
            buttons=[
                {"title": "Yes", "payload": f"/{intent_name}{entities}"},
                {"title": "No", "payload": f"/{USER_INTENT_OUT_OF_SCOPE}"},
            ],
        )

        return []
