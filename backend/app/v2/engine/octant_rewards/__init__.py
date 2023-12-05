from dataclasses import dataclass

from app.v2.engine.octant_rewards.locked_ratio import LockedRatio
from app.v2.engine.octant_rewards.locked_ratio.default import DefaultLockedRatio
from app.v2.engine.octant_rewards.matched import MatchedRewards
from app.v2.engine.octant_rewards.matched.default import DefaultMatchedRewards
from app.v2.engine.octant_rewards.total_and_individual import (
    TotalAndAllIndividualRewards,
)
from app.v2.engine.octant_rewards.total_and_individual.default import (
    DefaultTotalAndIndividualRewards,
)


@dataclass
class OctantRewardsSettings:
    locked_ratio: LockedRatio = DefaultLockedRatio()
    total_and_all_individual_rewards: TotalAndAllIndividualRewards = (
        DefaultTotalAndIndividualRewards()
    )
    matched_rewards: MatchedRewards = DefaultMatchedRewards()
