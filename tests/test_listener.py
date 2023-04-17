from scootbot3.listener import listen
from slack_sdk.socket_mode.response import SocketModeResponse


def test_listener(mocker, client, make_request):
    # mock
    post_mock = mocker.patch.object(client.web_client, "chat_postMessage")
    make_response_mock = mocker.patch.object(
        SocketModeResponse, "__init__", return_value=None
    )
    mocker.patch.object(client, "send_socket_mode_response")

    # send a request to the listener
    listen(client, make_request("!echo test"))

    # check mocks
    make_response_mock.assert_called_once_with(envelope_id="test_envelope_id")
    post_mock.assert_called_once_with(channel="test_channel", text="test")
