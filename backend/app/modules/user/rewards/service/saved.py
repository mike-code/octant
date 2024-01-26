from dataclasses import dataclass
from typing import Dict, Protocol, List

from app.context.manager import Context
from app.modules.user.rewards.core import get_unused_rewards


class UserAllocations(Protocol):
    def get_all_donors_addresses(self, context: Context) -> List[str]:
        ...


class UserBudgets(Protocol):
    def get_all_budgets(self, context: Context) -> Dict[str, int]:
        ...


class UserPatronMode(Protocol):
    def get_all_patrons_addresses(self, context: Context) -> List[str]:
        ...


@dataclass
class SavedUserRewards:
    allocations: UserAllocations
    user_budgets: UserBudgets
    patrons_mode: UserPatronMode

    def get_unused_rewards(self, context: Context) -> Dict[str, int]:
        budgets = self.user_budgets.get_all_budgets(context)
        donors = self.allocations.get_all_donors_addresses(context)
        patrons = self.patrons_mode.get_all_patrons_addresses(context)

        return get_unused_rewards(budgets, donors, patrons)
