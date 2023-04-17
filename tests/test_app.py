import logging

from scootbot3.app import main

LOGGER = logging.getLogger(__name__)


def test_app(caplog):
    caplog.set_level(logging.INFO)
    main(timeout=2)
    assert "imported commands" in caplog.text
    assert "initialized SocketModeClient" in caplog.text
    assert "added listener" in caplog.text
    assert "connected to socket mode servers" in caplog.text
