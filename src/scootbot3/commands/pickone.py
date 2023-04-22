from __future__ import annotations

import random

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest

from scootbot3.handlers import Handler

PICKONE_REGEX = r"^!pickone (?P<one>.+) or (?P<two>.+)$"


def pickone(
    client: BaseSocketModeClient, req: SocketModeRequest, matches: dict[str, str]
) -> str:
    return random.sample([matches["one"], matches["two"]], 1)[0]


Handler(regex=PICKONE_REGEX, func=pickone).register()
