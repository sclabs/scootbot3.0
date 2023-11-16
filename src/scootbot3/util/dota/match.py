from dataclasses import dataclass
from functools import cached_property

import requests
from typing_extensions import Self

from scootbot3.constants.steam import USER_TO_STEAM_ID
from scootbot3.util.dota.heroes import hero_name_from_id

DOTABUFF_BASE_URL = "https://www.dotabuff.com/matches/"
OPENDOTA_BASE_URL = "https://www.opendota.com/matches/"


@dataclass
class Match:
    match_id: int
    player_slot: int
    radiant_win: bool
    hero_id: int
    kills: int
    deaths: int
    assists: int

    @cached_property
    def radiant(self) -> bool:
        return self.player_slot < 128

    @cached_property
    def won(self) -> bool:
        return self.radiant == self.radiant_win

    @cached_property
    def hero_name(self) -> str:
        return hero_name_from_id(self.hero_id)

    def message(self, user: str, base_url: str = OPENDOTA_BASE_URL) -> str:
        return (
            f"{user} {'won' if self.won else 'lost'} as {self.hero_name} "
            f"going {self.kills}/{self.deaths}/{self.assists} "
            f"{':pogchamp:' if self.won else ':kekw:'} "
            f"<{base_url}{self.match_id}|{base_url[12:]}{self.match_id}>"
        )

    @classmethod
    def most_recent_for_user(cls, user: str) -> Self:
        url = (
            "https://api.opendota.com/"
            f"api/players/{USER_TO_STEAM_ID[user]}/matches?limit=1"
        )
        match = requests.get(url).json()[0]
        return cls(
            match_id=match["match_id"],
            player_slot=match["player_slot"],
            radiant_win=match["radiant_win"],
            hero_id=match["hero_id"],
            kills=match["kills"],
            deaths=match["deaths"],
            assists=match["assists"],
        )
