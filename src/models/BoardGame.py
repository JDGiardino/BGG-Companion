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

    def __post_init__(self):
        object.__setattr__(self, "id", int(self.id))
        object.__setattr__(self, "maxplayers", int(self.maxplayers))
        object.__setattr__(self, "minplayers", int(self.minplayers))
        # This bypasses frozen=true by modifying the object class which all objects inherent from including dataclasses
