import pytest
from scootbot3.client import make_client
from slack_sdk.socket_mode.request import SocketModeRequest


@pytest.fixture
def client():
    return make_client()


@pytest.fixture
def make_request():
    """
    pytest fixture factory to create a SocketModeRequest.

    This fixture factory returns a function with signature:

        make_request(text: str) -> SocketModeRequest

    The returned SocketModeRequest will have the following properties:
    - type: "events_api"
    - envelope_id: "test_envelope_id"
    - payload: {"event": {"channel": "test_channel", "text": text}}
    - accepts_response_payload: True
    """

    def _make_request(text):
        return SocketModeRequest(
            type="events_api",
            envelope_id="test_envelope_id",
            payload={"event": {"channel": "test_channel", "text": text}},
            accepts_response_payload=True,
        )

    return _make_request
