from dataclasses import dataclass

@dataclass
class Note:
    time: float
    duration: float
    frequency: float
    midi: int
    pitch: str
    loudness: float

@dataclass
class Match:
    reference: Note
    singer: Note
    pitch_difference: int
    timing_difference: float
    loudness_difference: float
    picth_score: float = 0.0
    timing_score: float = 0.0
    loudness_score: float = 0.0
    note_score: float = 0.0