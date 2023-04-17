from __future__ import annotations

import logging
import signal
from threading import Event

from scootbot3.client import make_client
from scootbot3.handlers import HANDLERS, import_commands
from scootbot3.listener import listen


def main(timeout: int | None = None) -> None:
    # set up logging
    logging.basicConfig(level=logging.INFO)

    # import all commands
    import_commands()
    logging.info("imported commands:\n" + "\n".join([h.regex for h in HANDLERS]))

    # initialize SocketModeClient with an app-level token + WebClient
    client = make_client()
    logging.info("initialized SocketModeClient")

    # add a new listener to receive messages from slack
    client.socket_mode_request_listeners.append(listen)
    logging.info("added listener")

    # establish a websocket connection to the socket mode servers
    client.connect()
    logging.info("connected to socket mode servers")

    # set up signal handlers
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # wait
    Event().wait(timeout=timeout)


if __name__ == "__main__":
    main()
