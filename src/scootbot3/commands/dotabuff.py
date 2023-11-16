from __future__ import annotations

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest

from scootbot3.handlers import Handler
from scootbot3.util.dota.match import DOTABUFF_BASE_URL, OPENDOTA_BASE_URL, Match

DOTABUFF_REGEX = r"^!(?P<source>dotabuff|yasp|opendota) (?P<user>.*)$"


def dotabuff(
    client: BaseSocketModeClient, req: SocketModeRequest, matches: dict[str, str]
) -> str:
    base_url = (
        DOTABUFF_BASE_URL if matches["source"] == "dotabuff" else OPENDOTA_BASE_URL
    )
    return Match.most_recent_for_user(matches["user"]).message(
        matches["user"], base_url=base_url
    )


Handler(regex=DOTABUFF_REGEX, func=dotabuff).register()
