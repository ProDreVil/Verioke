from dataclasses import dataclass

@dataclass
class Note:
    time: float
    frequency: float
    midi: int
    name: str