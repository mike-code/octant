from decimal import Decimal

from app import database
from app.database.models import PendingEpochSnapshot

from app.core.epochs.epochs_registry import EpochsRegistry


def calculate_total_rewards(
    eth_proceeds: int, locked_ratio: Decimal, pending_epoch: int
) -> int:
    registry = EpochsRegistry.get_epoch_settings(pending_epoch)
    return registry.rewardsStrategy.calculate_total_rewards(eth_proceeds, locked_ratio)


def calculate_all_individual_rewards(
    eth_proceeds: int, locked_ratio: Decimal, pending_epoch: int
) -> int:
    registry = EpochsRegistry.get_epoch_settings(pending_epoch)
    return registry.rewardsStrategy.calculate_all_individual_rewards(
        eth_proceeds, locked_ratio
    )


def calculate_matched_rewards(snapshot: PendingEpochSnapshot) -> int:
    return int(snapshot.total_rewards) - int(snapshot.all_individual_rewards)


def get_matched_rewards_from_epoch(epoch: int) -> int:
    snapshot = database.pending_epoch_snapshot.get_by_epoch_num(epoch)

    return calculate_matched_rewards(snapshot)


def calculate_matched_rewards_threshold(
    total_allocated: int, proposals_count: int
) -> int:
    return int(total_allocated / (proposals_count * 2))