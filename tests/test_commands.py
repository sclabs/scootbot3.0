import re


def test_echo(test_listener):
    test_listener("!echo test", re.compile("test"))


def test_pickone(test_listener):
    test_listener("!pickone test test or test test", re.compile("test test"))


def test_dotabuff(test_listener):
    test_listener(
        "!dotabuff vindi",
        re.compile(
            r"vindi (won|lost) as (.*) going (\d+)\/(\d+)\/(\d+) :(pogchamp|kekw): "
            r"<https:\/\/www\.dotabuff\.com\/matches\/(\d+)"
            r"\|dotabuff\.com\/matches\/(\d+)>"
        ),
    )
