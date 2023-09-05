from flask import current_app as app, g as request_context
from gql import gql


def get_user_locks_history(user_address: str, from_timestamp: int, limit: int):
    query = gql(
        """
        query GetLocks($userAddress: Bytes!, $fromTimestamp: Int!, $limit: Int!) {
          lockeds(
            orderBy: timestamp
            orderDirection: desc
            where: {user: $userAddress, timestamp_lte: $fromTimestamp}
            first: $limit
          ) {
            __typename
            amount
            timestamp
          }
        }
        """
    )
    variables = {
        "userAddress": user_address,
        "fromTimestamp": from_timestamp,
        "limit": limit,
    }
    app.logger.debug(f"[Subgraph] Getting user {user_address} locks")

    partial_result = request_context.graphql_client.execute(
        query, variable_values=variables
    )["lockeds"]

    result = []

    if len(partial_result) > 0:
        limit_timestamp = partial_result[-1]["timestamp"]
        events_at_timestamp_limit = get_locks_by_address_and_timestamp_range(
            user_address, limit_timestamp, limit_timestamp + 1
        )
        result_without_events_at_timestamp_limit = list(
            filter(lambda x: x["timestamp"] != limit_timestamp, partial_result)
        )
        result = result_without_events_at_timestamp_limit + events_at_timestamp_limit

    app.logger.debug(f"[Subgraph] Received locks: {result}")

    return result


def get_locks_by_timestamp_range(from_ts: int, to_ts: int):
    query = gql(
        """
        query GetLocks($fromTimestamp: Int!, $toTimestamp: Int!) {
          lockeds(
            orderBy: timestamp
            where: {timestamp_gte: $fromTimestamp, timestamp_lt: $toTimestamp}
          ) {
            __typename
            depositBefore
            amount
            timestamp
            user
          }
        }
        """
    )

    variables = {
        "fromTimestamp": from_ts,
        "toTimestamp": to_ts,
    }
    app.logger.debug(f"[Subgraph] Getting locks in timestamp range {from_ts} - {to_ts}")
    result = request_context.graphql_client.execute(query, variable_values=variables)[
        "lockeds"
    ]
    app.logger.debug(f"[Subgraph] Received locks: {result}")

    return result


def get_locks_by_address_and_timestamp_range(
    user_address: str, from_ts: int, to_ts: int
):
    query = gql(
        """
        query GetLocks($userAddress: Bytes!, $fromTimestamp: Int!, $toTimestamp: Int!) {
          lockeds(
            orderBy: timestamp
            where: {timestamp_gte: $fromTimestamp, timestamp_lt: $toTimestamp, user: $userAddress}
          ) {
            __typename
            depositBefore
            amount
            timestamp
            user
          }
        }
        """
    )

    variables = {
        "userAddress": user_address,
        "fromTimestamp": from_ts,
        "toTimestamp": to_ts,
    }

    app.logger.debug(
        f"[Subgraph] Getting user {user_address} locks in timestamp range {from_ts} - {to_ts}"
    )
    result = request_context.graphql_client.execute(query, variable_values=variables)[
        "lockeds"
    ]
    app.logger.debug(f"[Subgraph] Received locks: {result}")

    return result
