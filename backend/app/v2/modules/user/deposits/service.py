from dataclasses import dataclass
from typing import Tuple, List

from flask import current_app as app

from app.core.deposits.events import EventGenerator
from app.v2.context.context import EpochContext, CurrentEpochContext
from app.v2.engine.user.effective_deposit import (
    UserDeposit,
    UserEffectiveDepositPayload,
)


@dataclass
class UserDepositsCalculator:
    events_generator: EventGenerator

    def calculate_effective_deposits(
        self, context: EpochContext
    ) -> Tuple[List[UserDeposit], int]:
        epoch_details = context.epoch_details
        start = epoch_details.start_sec
        end = epoch_details.end_sec
        events = self.events_generator.get_all_users_events()
        app.logger.debug(
            f"Calculating effective deposits for epoch {epoch_details.epoch_no}"
        )

        effective_deposit_calculator = context.epoch_settings.user.effective_deposit

        return effective_deposit_calculator.calculate_users_effective_deposits(
            UserEffectiveDepositPayload(
                epoch_start=start, epoch_end=end, lock_events_by_addr=events
            )
        )


@dataclass
class UserDepositsEstimator:
    user_deposits_calculator: UserDepositsCalculator

    def estimate_total_effective_deposit(self, context: CurrentEpochContext) -> int:
        _, total = self.user_deposits_calculator.calculate_effective_deposits(context)
        return total
