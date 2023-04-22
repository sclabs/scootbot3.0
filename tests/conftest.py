import pytest
from scootbot3.client import make_client
from scootbot3.listener import listen
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse


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


@pytest.fixture
def test_listener(mocker, client, make_request):
    """
    pytest fixture factory to test if the scootbot listener responds as expected
    to a given input.

    This fixture factory returns a function with signature:

        test_listener(input: str, output: str) -> None

    The listener will be presented with input message text and we will assert
    that it responds with the expected output text.
    """

    def _test_listener(input: str, output: str) -> None:
        # mock
        post_mock = mocker.patch.object(client.web_client, "chat_postMessage")
        make_response_mock = mocker.patch.object(
            SocketModeResponse, "__init__", return_value=None
        )
        mocker.patch.object(client, "send_socket_mode_response")

        # send a request to the listener
        listen(client, make_request(input))

        # check mocks
        make_response_mock.assert_called_once_with(envelope_id="test_envelope_id")
        post_mock.assert_called_once_with(channel="test_channel", text=output)

    return _test_listener
