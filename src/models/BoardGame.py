from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BoardGame:
    id: int
    name: str
    type: str
    description: str
    minplayers: int
    maxplayers: int
    yearpublished: int
    thumbnail: Optional[str] = None
    image: Optional[str] = None

    def __post_init__(self):
        object.__setattr__(self, "id", int(self.id))
        object.__setattr__(self, "maxplayers", int(self.maxplayers))
        object.__setattr__(self, "minplayers", int(self.minplayers))
        object.__setattr__(self, "yearpublished", int(self.yearpublished))
        # This bypasses frozen=true by modifying the object class which all objects inherent from including dataclasses
