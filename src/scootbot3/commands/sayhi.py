from __future__ import annotations

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest

from scootbot3.handlers import Handler
from scootbot3.util.user import user_name

SAYHI_REGEX = r"^!sayhi$"


def sayhi(
    client: BaseSocketModeClient, req: SocketModeRequest, matches: dict[str, str]
) -> str:
    return f"hello @{user_name(client, req)}"


Handler(regex=SAYHI_REGEX, func=sayhi).register()
