from dataclasses import dataclass


@dataclass(frozen=True)
class BoardGame:
    id: int
    name: str
    type: str
    description: str
    minplayers: int
    maxplayers: int
    thumbnail: str
    image: str
