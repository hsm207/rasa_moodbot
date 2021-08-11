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
    """Load the domain and return it as a dictionary"""
    domain = Domain.load("domain.yml")
    return domain.as_dict()


@pytest.fixture
def tracker() -> Tracker:
    """Load a tracker object"""
    return Tracker(
        sender_id="test_user",
        slots={},
        latest_message={},
        events=[{}],
        paused=False,
        followup_action="",
        active_loop={},
        latest_action_name="",
    )
