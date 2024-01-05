from decimal import Decimal

from app.engine.user.budget import UserBudgetPayload, UserBudget


class DefaultUserBudget(UserBudget):
    def calculate_budget(self, payload: UserBudgetPayload) -> int:
        individual_share = Decimal(payload.user_effective_deposit) / Decimal(
            payload.total_effective_deposit
        )

        return int(payload.all_individual_rewards * individual_share)