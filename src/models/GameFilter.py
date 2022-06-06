from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GameFilter:
    gameType: str = "boardgame"
    minplayers: Optional[int] = None
    maxplayers: Optional[int] = None
    exactplayers: Optional[int] = None

    def __post_init__(self):
        if self.minplayers is not None:
            object.__setattr__(self, "minplayers", int(self.minplayers))
        if self.maxplayers is not None:
            object.__setattr__(self, "maxplayers", int(self.maxplayers))
        if self.exactplayers is not None:
            object.__setattr__(self, "exactplayers", int(self.exactplayers))

    # This bypasses frozen=true by modifying the object class which all objects inherent from including dataclasses
