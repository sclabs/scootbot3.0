import logging

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse

from scootbot3.handlers import HANDLERS


def listen(client: BaseSocketModeClient, req: SocketModeRequest) -> None:
    """
    Socket Mode Request Listener.
    """
    if req.type == "events_api":
        logging.info('received event: "' + req.payload["event"]["text"] + '"')

        # acknowledge the request
        response = SocketModeResponse(envelope_id=req.envelope_id)
        client.send_socket_mode_response(response)

        # loop through all handlers
        for handler in HANDLERS:
            # handle the message
            response_text = handler.handle(client, req)
            if isinstance(response_text, str):
                client.web_client.chat_postMessage(
                    channel=req.payload["event"]["channel"],
                    text=response_text,
                )
    else:
        logging.info("ignoring request of type " + req.type)
