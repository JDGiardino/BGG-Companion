from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GameFilter:
    gametype: Optional[str] = None
    minplayers: Optional[int] = None
    maxplayers: Optional[int] = None
    playerrangetype: Optional[str] = None
    playstyle: Optional[str] = None
    mincomplexity: Optional[float] = None
    maxcomplexity: Optional[float] = None

    def __post_init__(self):
        if self.minplayers is not None:
            object.__setattr__(self, "minplayers", int(self.minplayers))
        if self.maxplayers is not None:
            object.__setattr__(self, "maxplayers", int(self.maxplayers))
        if self.playerrangetype is not None:
            object.__setattr__(self, "playerrangetype", str(self.playerrangetype))
        if self.playstyle is not None:
            object.__setattr__(self, "playerstyle", str(self.playstyle))
        if self.mincomplexity is not None:
            object.__setattr__(self, "mincomplexity", float(self.mincomplexity))
        if self.maxcomplexity is not None:
            object.__setattr__(self, "maxcomplexity", float(self.maxcomplexity))

    # This bypasses frozen=true by modifying the object class which all objects inherent from including dataclasses
