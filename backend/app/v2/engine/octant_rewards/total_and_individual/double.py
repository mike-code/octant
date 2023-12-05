from app.v2.engine.octant_rewards.total_and_individual import (
    TotalAndAllIndividualPayload,
    TotalAndAllIndividualRewards,
)


class DoubleTotalAndIndividualRewards(TotalAndAllIndividualRewards):
    DOUBLING_GLM_SUPPLY_LIMIT = 0.25
    REWARDS_MULTIPLY_RATIO_LIMIT = 0.5
    REWARDS_MULTIPLY_FACTOR = 2

    def calculate_total_rewards(self, payload: TotalAndAllIndividualPayload) -> int:
        if payload.locked_ratio < self.DOUBLING_GLM_SUPPLY_LIMIT:
            return (
                int(payload.eth_proceeds * payload.locked_ratio.sqrt())
                * self.REWARDS_MULTIPLY_FACTOR
            )
        else:
            return payload.eth_proceeds

    def calculate_all_individual_rewards(
        self, payload: TotalAndAllIndividualPayload
    ) -> int:
        if payload.locked_ratio < self.DOUBLING_GLM_SUPPLY_LIMIT:
            return (
                int(payload.eth_proceeds * payload.locked_ratio)
                * self.REWARDS_MULTIPLY_FACTOR
            )
        else:
            return int(payload.eth_proceeds * self.REWARDS_MULTIPLY_RATIO_LIMIT)
