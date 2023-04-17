import os

from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.web import WebClient


def make_client() -> BaseSocketModeClient:
    """
    Make a SocketModeClient, using tokens from environment variables.
    """
    return SocketModeClient(
        # this app-level token will be used only for establishing a connection
        app_token=os.environ["SCOOTBOT_APP_TOKEN"],
        # you will be using this WebClient for performing Web API calls in listeners
        web_client=WebClient(token=os.environ["SCOOTBOT_TOKEN"]),
    )
