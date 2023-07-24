from collections import defaultdict
from dataclasses import dataclass
from itertools import groupby
from operator import itemgetter
from typing import Dict, List

from eth_utils import to_checksum_address

from app.infrastructure import qraphql
from app.infrastructure.qraphql.locks import get_locks_by_timestamp_range
from app.infrastructure.qraphql.unlocks import get_unlocks_by_timestamp_range


@dataclass(frozen=True)
class WeightedDeposit:
    """
    Class representing a weighted deposit.

    Attributes:
        amount: The deposit amount.
        weight: The duration the deposit remained locked.
    """

    amount: int
    weight: int

    def __iter__(self):
        yield self.amount
        yield self.weight


def get_weighted_deposits(epoch_no: int) -> Dict[str, List[WeightedDeposit]]:
    """
    Get a list of weighted deposits per user for a given epoch number. The weight of the deposit
    is calculated based on the time duration it remained locked in a given epoch.
    """
    epoch = qraphql.epochs.get_epoch_by_number(epoch_no)
    start, end = int(epoch["fromTs"]), int(epoch["toTs"])
    events = _get_events_from_subgraph(start, end)

    weighted_deposits = defaultdict(list)

    for user_address, user_events in events.items():
        weighted_amounts = []

        # Calculate deposit from the epoch start to the first event
        first_event = user_events[0]
        amount = int(first_event["depositBefore"])
        weight = first_event["timestamp"] - start
        weighted_amounts.append(WeightedDeposit(amount, weight))

        # Calculate deposit between all events
        for prev_event, next_event in zip(user_events, user_events[1:]):
            amount = int(next_event["depositBefore"])
            weight = next_event["timestamp"] - prev_event["timestamp"]
            weighted_amounts.append(WeightedDeposit(amount, weight))

        # Calculate deposit from the last event to the epoch end
        last_event = user_events[-1]
        amount = _calculate_deposit_after_event(last_event)
        weight = end - last_event["timestamp"]
        weighted_amounts.append(WeightedDeposit(amount, weight))

        weighted_deposits[to_checksum_address(user_address)] = weighted_amounts

    return weighted_deposits


def _get_events_from_subgraph(start: int, end: int) -> Dict[str, Dict]:
    """
    Get all lock and unlock events from the subgraph within the given timestamp range, sort them by user and timestamp,
    and group them by user.

    Args:
        start: The start timestamp.
        end: The end timestamp.

    Returns:
        A dictionary where keys are user addresses and values are lists of event dictionaries sorted by timestamp.
    """
    events = get_locks_by_timestamp_range(start, end) + get_unlocks_by_timestamp_range(
        start, end
    )
    sorted_events = sorted(events, key=itemgetter("user", "timestamp"))
    return {k: list(g) for k, g in groupby(sorted_events, key=itemgetter("user"))}


def _calculate_deposit_after_event(event: dict) -> int:
    if event["__typename"] == "Locked":
        return int(event["depositBefore"]) + int(event["amount"])
    else:
        return int(event["depositBefore"]) - int(event["amount"])