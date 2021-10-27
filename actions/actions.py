# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import time
import asyncio
import logging

class ActionSleepSync(Action):

    def name(self) -> Text:
        return "action_sleep_sync"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sleep_time = tracker.slots["sleep_time"]

        logging.info(f"sleeping for {sleep_time} seconds ...")

        time.sleep(sleep_time)
        dispatcher.utter_message(text=f"I slept for {sleep_time} seconds synchronously!")

        return []

class ActionSleepAsync(Action):

    def name(self) -> Text:
        return "action_sleep_async"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sleep_time = tracker.slots["sleep_time"]

        logging.info(f"sleeping for {sleep_time} seconds ...")

        await asyncio.sleep(sleep_time)
        dispatcher.utter_message(text=f"I slept for {sleep_time} seconds asynchronously!")

        return []
