from typing import List

from app.context.manager import Context
from app.infrastructure import database
from app.modules.common.time import Timestamp, from_datetime
from app.modules.dto import AccountFundsDTO, AllocationItem
from app.pydantic import Model


class SavedUserAllocations(Model):
    def get_all_donors_addresses(self, context: Context) -> List[str]:
        return database.allocations.get_users_with_allocations(
            context.epoch_details.epoch_num
        )

    def get_all_users_with_allocations_sum(
        self, context: Context
    ) -> List[AccountFundsDTO]:
        return database.allocations.get_users_alloc_sum_by_epoch(
            context.epoch_details.epoch_num
        )

    def get_user_allocation_sum(self, context: Context, user_address: str) -> int:
        return database.allocations.get_user_alloc_sum_by_epoch(
            context.epoch_details.epoch_num, user_address
        )

    def has_user_allocated_rewards(self, context: Context, user_address: str) -> bool:
        allocation_signature = (
            database.allocations.get_allocation_request_by_user_and_epoch(
                user_address, context.epoch_details.epoch_num
            )
        )
        return allocation_signature is not None

    def get_user_allocations_by_timestamp(
        self, user_address: str, from_timestamp: Timestamp, limit: int
    ) -> List[AllocationItem]:
        return [
            AllocationItem(
                project_address=r.proposal_address,
                epoch=r.epoch,
                amount=int(r.amount),
                timestamp=from_datetime(r.created_at),
            )
            for r in database.allocations.get_user_allocations_history(
                user_address, from_timestamp.datetime(), limit
            )
        ]
