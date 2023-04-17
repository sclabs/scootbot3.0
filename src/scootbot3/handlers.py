from __future__ import annotations

import importlib
import logging
import pkgutil
import re
from dataclasses import dataclass
from typing import Callable

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest

import scootbot3.commands

HANDLERS: list[Handler] = []


@dataclass
class Handler:
    regex: str
    func: Callable[[BaseSocketModeClient, SocketModeRequest, dict[str, str]], str]

    def handle(
        self, client: BaseSocketModeClient, req: SocketModeRequest
    ) -> str | None:
        match = re.match(self.regex, req.payload["event"]["text"])
        if match:
            logging.info(
                "Matched regex!\n"
                f"  Regex: {self.regex}\n"
                f"  Message: {req.payload['event']['text']}\n"
                f"  Groupdict: {match.groupdict()}"
            )
            return self.func(client, req, match.groupdict())
        else:
            return None

    def register(self) -> None:
        HANDLERS.append(self)


def import_commands() -> None:
    for module in pkgutil.iter_modules(scootbot3.commands.__path__):
        importlib.import_module(
            name="." + module.name, package=scootbot3.commands.__name__
        )
