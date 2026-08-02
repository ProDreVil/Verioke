from dataclasses import dataclass

@dataclass
class Note:
    time: float
    # duration: float
    frequency: float
    midi: int
    pitch: str