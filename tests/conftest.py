import json

import pytest
from rasa.shared.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


@pytest.fixture
def dispatcher() -> CollectingDispatcher:
    """Create a clean dispatcher"""
    return CollectingDispatcher()


@pytest.fixture
def domain() -> DomainDict:
    """Create an empty domain"""
    return {}


@pytest.fixture
def tracker(tmpdir) -> Tracker:
    """Create a tracker with a common start state"""
    initial_tracker = """
    {
    "sender_id": "unit_test_user",
    "slots": {
        "requested_slot": null
    },
    "latest_message": {
        "intent": {},
        "entities": [],
        "text": null,
        "message_id": null,
        "metadata": {}
    },
    "latest_event_time": 1612422342.865033865,
    "followup_action": null,
    "paused": false,
    "events": [
        {
            "event": "action",
            "timestamp": 1612422342.8649258614,
            "name": "action_session_start",
            "policy": null,
            "confidence": 1.0,
            "action_text": null
        },
        {
            "event": "session_started",
            "timestamp": 1612422342.8649988174
        },
        {
            "event": "action",
            "timestamp": 1612422342.865033865,
            "name": "action_listen",
            "policy": null,
            "confidence": null,
            "action_text": null
        }
    ],
    "latest_input_channel": null,
    "active_loop": {},
    "latest_action": {
        "action_name": "action_listen"
    },
    "latest_action_name": "action_listen"
}   
    """

    path = tmpdir.join("initial_tracker.json")
    path.write(initial_tracker)

    with open(path) as json_file:
        tracker = Tracker.from_dict(json.load(json_file))

    return tracker
