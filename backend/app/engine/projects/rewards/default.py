from decimal import Decimal
from typing import List

from app.engine.projects.rewards import (
    ProjectRewardsPayload,
    ProjectRewards,
    AccountFunds,
)


class DefaultProjectRewards(ProjectRewards):
    def calculate_project_rewards(
        self, payload: ProjectRewardsPayload
    ) -> (List[AccountFunds], int):
        allocated_by_addr = payload.allocated_by_addr

        total_allocated_above_threshold = sum(
            [
                allocated
                for _, allocated in allocated_by_addr
                if allocated >= payload.threshold
            ]
        )

        project_rewards_sum = 0
        project_rewards: List[AccountFunds] = []

        for address, allocated in allocated_by_addr:
            if allocated >= payload.threshold:
                matched = int(
                    Decimal(allocated)
                    / Decimal(total_allocated_above_threshold)
                    * payload.matched_rewards
                )
                project_rewards_sum += allocated + matched
                project_rewards.append(
                    AccountFunds(address, allocated + matched, matched)
                )

        return (
            sorted(project_rewards, key=lambda r: r.amount, reverse=True),
            project_rewards_sum,
        )