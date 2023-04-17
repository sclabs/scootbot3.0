from __future__ import annotations

from typing import Any, cast

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest


def user_data_from_id(client: BaseSocketModeClient, user_id: str) -> dict[str, Any]:
    """
    Get the user object for a user ID.

    See https://api.slack.com/types/user
    """
    return cast(
        "dict[str, dict[str, Any]]", client.web_client.users_info(user=user_id).data
    )["user"]


def user_data(client: BaseSocketModeClient, req: SocketModeRequest) -> dict[str, Any]:
    """
    Get the user object for the user associated with a SocketModeRequest.
    """
    return user_data_from_id(client, req.payload["event"]["user"])


def user_name(client: BaseSocketModeClient, req: SocketModeRequest) -> str:
    """
    Get the user name of the user associated with a SocketModeRequest.
    """
    return cast(str, user_data(client, req)["name"])
