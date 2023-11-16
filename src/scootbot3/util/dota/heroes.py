from __future__ import annotations

from functools import lru_cache
from typing import Any, cast

import requests

HEROES_JSON_URL = (
    "https://raw.githubusercontent.com/odota/dotaconstants/master/build/heroes.json"
)


@lru_cache
def _heroes_dict() -> dict[str, Any]:
    return cast("dict[str, Any]", requests.get(HEROES_JSON_URL).json())


def hero_name_from_id(hero_id: int) -> str:
    return cast(str, _heroes_dict()[str(hero_id)]["localized_name"])
