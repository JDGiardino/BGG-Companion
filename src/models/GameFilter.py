from dataclasses import dataclass


@dataclass
class GameFilter:
    minplayers: int = None
    maxplayers: int = None
    exactplayers: int = None
    gameType: str = "boardgame"