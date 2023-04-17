from __future__ import annotations

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest

from scootbot3.handlers import Handler

ECHO_REGEX = r"^!echo (?P<text>.*)$"


def echo(
    client: BaseSocketModeClient, req: SocketModeRequest, matches: dict[str, str]
) -> str:
    return matches["text"]


Handler(regex=ECHO_REGEX, func=echo).register()
