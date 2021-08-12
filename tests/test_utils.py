from typing import Any, Text, Dict, List


def extract_slots_from_events(events: List[Dict[Text, Any]]) -> List[Dict[Text, Any]]:
    """Returns slot events given a list of events from a tracker"""
    return [e for e in events if e["event"] == "slot"]


def is_same_slots(slotsA: List[Dict[Text, Any]], slotsB: List[Dict[Text, Any]]) -> bool:
    """Checks a list of slot events are identical"""
    f = lambda x: x["name"]
    slot_pairs = zip(sorted(slotsA, key=f), sorted(slotsB, key=f))
    return all(s1 == s2 for s1, s2 in slot_pairs)
