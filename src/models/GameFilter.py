from dataclasses import dataclass
from typing import Optional


@dataclass
class GameFilter:
    gameType: str = "boardgame"
    minplayers: Optional[int] = None
    maxplayers: Optional[int] = None
    exactplayers: Optional[int] = None
