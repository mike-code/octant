from decimal import Decimal

import pytest
from eth_account import Account

from app import database
from app.controllers.allocations import allocate, get_allocation_nonce
from app.controllers.rewards import (
    get_allocation_threshold,
    get_rewards_budget,
    get_proposals_rewards,
)
from app.core.allocations import (
    AllocationRequest,
)
from app.core.rewards.rewards import (
    calculate_total_rewards,
    calculate_all_individual_rewards,
    get_matched_rewards_from_epoch,
    calculate_matched_rewards_threshold,
)
from .conftest import (
    allocate_user_rewards,
    deserialize_allocations,
    MOCKED_PENDING_EPOCH_NO,
    MOCK_PROPOSALS,
)
from .test_allocations import (
    sign,
    create_payload,
    build_allocations_eip712_data,
)


@pytest.fixture(autouse=True)
def before(
    proposal_accounts,
    patch_epochs,
    patch_proposals,
    patch_has_pending_epoch_snapshot,
    patch_user_budget,
    patch_matched_rewards,
):
    MOCK_PROPOSALS.get_proposal_addresses.return_value = [
        p.address for p in proposal_accounts[0:5]
    ]


@pytest.mark.parametrize(
    "eth_proceeds,locked_ratio,pending_epoch,expected",
    [
        (4_338473610_477382755, Decimal("0.0000004"), 1, 5487783_271057070),
        (4_338473610_477382755, Decimal("0.0000004"), 2, 2743891_635528535),
        (
            600_000000000_000000000,
            Decimal("0.0003298799699"),
            1,
            21_795117725_215434128,
        ),
        (
            600_000000000_000000000,
            Decimal("0.0003298799699"),
            2,
            10_897558862_607717064,
        ),
        (10_000000000_000000000, Decimal("0.2"), 1, 8_944271909_999158784),
        (10_000000000_000000000, Decimal("0.2"), 2, 4472135954999579392),
        (10_000000000_000000000, Decimal("0.2"), 3, 4472135954999579392),
        (10_000000000_000000000, Decimal("0.25"), 1, 10_000000000_000000000),
        (10_000000000_000000000, Decimal("0.25"), 2, 5_000000000_000000000),
        (10_000000000_000000000, Decimal("0.25"), 3, 5_000000000_000000000),
        (10_000000000_000000000, Decimal("0.43"), 1, 10_000000000_000000000),
        (10_000000000_000000000, Decimal("0.43"), 2, 6_557438524_302000652),
        (10_000000000_000000000, Decimal("0.43"), 3, 6_557438524_302000652),
        (1200_000000000_000000000, Decimal("1"), 1, 1200_000000000_000000000),
        (1200_000000000_000000000, Decimal("1"), 2, 1200_000000000_000000000),
        (1200_000000000_000000000, Decimal("1"), 3, 1200_000000000_000000000),
    ],
)
def test_calculate_total_rewards(eth_proceeds, locked_ratio, pending_epoch, expected):
    result = calculate_total_rewards(eth_proceeds, locked_ratio, pending_epoch)
    assert result == expected


@pytest.mark.parametrize(
    "eth_proceeds,locked_ratio,pending_epoch,expected",
    [
        (4_338473610_477382755, Decimal("0.0000004"), 1, 3470_778888380),
        (4_338473610_477382755, Decimal("0.0000004"), 2, 1735_389444190),
        (600_000000000_000000000, Decimal("0.0003298799699"), 1, 395855963_880000000),
        (600_000000000_000000000, Decimal("0.0003298799699"), 2, 197927981_940000000),
        (10_000000000_000000000, Decimal("0.2"), 1, 4_000000000_000000000),
        (10_000000000_000000000, Decimal("0.2"), 2, 2_000000000_000000000),
        (10_000000000_000000000, Decimal("0.2"), 3, 2_000000000_000000000),
        (10_000000000_000000000, Decimal("0.25"), 1, 5_000000000_000000000),
        (10_000000000_000000000, Decimal("0.25"), 2, 2_500000000_000000000),
        (10_000000000_000000000, Decimal("0.25"), 3, 2_500000000_000000000),
        (10_000000000_000000000, Decimal("0.43"), 1, 5_000000000_000000000),
        (10_000000000_000000000, Decimal("0.43"), 2, 4_300000000_000000000),
        (10_000000000_000000000, Decimal("0.43"), 3, 4_300000000_000000000),
        (1200_000000000_000000000, Decimal("1"), 1, 600_000000000_000000000),
        (1200_000000000_000000000, Decimal("1"), 2, 1200_000000000_000000000),
        (1200_000000000_000000000, Decimal("1"), 3, 1200_000000000_000000000),
    ],
)
def test_calculate_all_individual_rewards(
    eth_proceeds, locked_ratio, pending_epoch, expected
):
    result = calculate_all_individual_rewards(eth_proceeds, locked_ratio, pending_epoch)
    assert result == expected


def test_get_allocation_threshold(app, tos_users, proposal_accounts):
    total_allocated = _allocate_random_individual_rewards(tos_users, proposal_accounts)

    assert get_allocation_threshold(None) == calculate_matched_rewards_threshold(
        total_allocated, 5
    )


def test_get_rewards_budget(app, tos_users, proposal_accounts):
    glm_supply = 1000000000_000000000_000000000
    eth_proceeds = 402_410958904_110000000
    total_ed = 22700_000000000_099999994
    locked_ratio = Decimal("0.000022700000000000099999994")
    total_rewards = 1_917267577_180363384
    all_individual_rewards = 9134728_767123337

    database.pending_epoch_snapshot.add_snapshot(
        MOCKED_PENDING_EPOCH_NO,
        glm_supply,
        eth_proceeds,
        total_ed,
        locked_ratio,
        total_rewards,
        all_individual_rewards,
    )

    expected_matched = get_matched_rewards_from_epoch(MOCKED_PENDING_EPOCH_NO)
    total_allocated = _allocate_random_individual_rewards(tos_users, proposal_accounts)

    rewards = get_rewards_budget(None)

    assert rewards.epoch == MOCKED_PENDING_EPOCH_NO
    assert rewards.allocated == total_allocated
    assert rewards.matched == expected_matched


@pytest.mark.parametrize(
    #     The structure of these parameters is as follows
    #
    #     dict { int : List[(str, int)] }
    #             \           \     \______ allocation amount
    #              \           \___________ account index of one of the accounts generated
    #               \                       by proposal_accounts() fixture
    #                \_____________________ account index of one of the accounts generated
    #                                       by user_accounts() fixture
    #
    #     dict { int : int }
    #             \      \__________________ calculated matched reward for the proposal
    #              \________________________ account index of one of the accounts generated
    #                                        by proposal_accounts() fixture
    "user_allocations, expected_matches",
    [
        (
            {
                0: [
                    (1, 3_000000000_000000000),
                    (2, 1_000000000_000000000),
                    (3, 1_000000000_000000000),
                ],
                1: [(1, 2_000000000_000000000), (3, 4_000000000_000000000)],
            },
            {
                1: 5_000000000_000000000,
                2: 0,
                3: 5_000000000_000000000,
            },
        ),
        # ------------------------------------
        (
            {
                0: [
                    (1, 3_000000000_000000000),
                    (2, 2_000000000_000000000),
                    (3, 1_000000000_000000000),
                ],
                1: [(1, 2_000000000_000000000), (3, 4_000000000_000000000)],
            },
            {
                1: 4_166666666_666666666,
                2: 1_666666666_666666666,
                3: 4_166666666_666666666,
            },
        ),
    ],
)
def test_proposals_rewards(
    app,
    tos_users,
    proposal_accounts,
    user_allocations: dict,
    expected_matches: dict,
):
    for user_index, allocations in user_allocations.items():
        user_account = tos_users[user_index]

        for allocation in allocations:
            proposal_account: Account = proposal_accounts[allocation[0]]
            allocation_amount = allocation[1]

            nonce = get_allocation_nonce(user_account.address)
            allocate_user_rewards(
                user_account, proposal_account, allocation_amount, nonce
            )

    expected_rewards = {}

    for proposal_index, expected_reward in expected_matches.items():
        proposal_address = proposal_accounts[proposal_index].address
        expected_rewards[proposal_address] = expected_reward

    proposals = get_proposals_rewards(MOCKED_PENDING_EPOCH_NO)
    assert len(proposals) == 5
    for proposal in proposals:
        assert expected_rewards.get(proposal.address, 0) == proposal.matched


def _allocate_random_individual_rewards(user_accounts, proposal_accounts) -> int:
    """
    Allocates individual rewards from 2 users for 5 projects total

    Returns the sum of these allocations
    """
    payload1 = create_payload(proposal_accounts[0:2], None, 0)
    signature1 = sign(user_accounts[0], build_allocations_eip712_data(payload1))

    payload2 = create_payload(proposal_accounts[0:3], None, 0)
    signature2 = sign(user_accounts[1], build_allocations_eip712_data(payload2))

    # Call allocate method for both users
    allocate(
        AllocationRequest(payload1, signature1, override_existing_allocations=True)
    )
    allocate(
        AllocationRequest(payload2, signature2, override_existing_allocations=True)
    )

    allocations1 = sum([int(a.amount) for a in deserialize_allocations(payload1)])
    allocations2 = sum([int(a.amount) for a in deserialize_allocations(payload2)])

    return allocations1 + allocations2
