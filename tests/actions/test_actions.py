from actions import actions
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List, Set
import pytest

from tests.test_utils import is_same_slots, extract_slots_from_events

# Things to test in a custom action
def test_action_hello_world(dispatcher, tracker, domain):
    action = actions.ActionHelloWorld()
    actual_events = action.run(dispatcher, tracker, domain)

    assert actual_events[0] == SlotSet("is_logged_in", True)
    assert dispatcher.messages[0]["response"] == "utter_greet_with_name"


# Organizing for better error messages
class TestActionHelloWorld:
    def test_utterance_is_correct(self, dispatcher, tracker, domain):
        action = actions.ActionHelloWorld()
        action.run(dispatcher, tracker, domain)
        assert dispatcher.messages[0]["response"] == "utter_greet_with_name"

    def test_slots_are_set(self, dispatcher, tracker, domain):
        action = actions.ActionHelloWorld()
        actual_events = action.run(dispatcher, tracker, domain)
        assert actual_events[0] == SlotSet("is_logged_in", True)


# Extracting common methods
# Assume you will frequently extract the slots of the events returned by the custom actions
def test_action_many_events_ugly(dispatcher, tracker, domain):
    action = actions.ActionManyEvents()
    actual_events = action.run(dispatcher, tracker, domain)

    for e in actual_events:
        if e["event"] == "slot":
            if e["name"] == "is_logged_in":
                is_logged_in = e["value"]
            if e["name"] == "name":
                name = e["value"]

    assert is_logged_in == True
    assert name == "John"


def test_action_many_events_clean(dispatcher, tracker, domain):
    action = actions.ActionManyEvents()
    actual_events = action.run(dispatcher, tracker, domain)

    actual_slots = extract_slots_from_events(actual_events)
    expected_slots = [SlotSet("name", "John"), SlotSet("is_logged_in", True)]

    assert is_same_slots(actual_slots, expected_slots)


# use parameterised tests to test different outcome
def test_successul_login(dispatcher, tracker, domain):
    tracker.slots["name"] = "John"
    action = actions.ActionAuthrorizeUser()

    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events[0] == SlotSet("is_logged_in", True)


def test_unsuccessul_login(dispatcher, tracker, domain):
    tracker.slots["name"] = "Doe"
    action = actions.ActionAuthrorizeUser()

    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events[0] == SlotSet("is_logged_in", False)


@pytest.mark.parametrize(
    "test_input, expected_event",
    [("John", SlotSet("is_logged_in", True)), ("Doe", SlotSet("is_logged_in", False))],
)
def test_authrorize_user(test_input, expected_event, dispatcher, tracker, domain):
    tracker.slots["name"] = test_input
    action = actions.ActionAuthrorizeUser()

    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events[0] == expected_event


# using monkeypatch
def test_agent_unavailable(monkeypatch, dispatcher, tracker, domain):
    action = actions.ActionAgentAvailable()

    monkeypatch.setattr(action, "_is_agent_available", lambda: False)

    actual_events = action.run(dispatcher, tracker, domain)
    assert actual_events[0] == SlotSet("is_agent_available", False)
