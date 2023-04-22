def test_echo(test_listener):
    test_listener("!echo test", "test")


def test_pickone(test_listener):
    test_listener("!pickone test test or test test", "test test")
