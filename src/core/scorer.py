from core.models import Match, Note
from core.fuzzy import fuzzy_note_score

import utils.config as config

def compare_notes(reference_notes: list[Note], singer_notes: list[Note]) -> list[Match]:
    matches = []
    singer_index = 0
    for reference in reference_notes:
        while (singer_index < len(singer_notes) and singer_notes[singer_index].time < reference.time - config.TIME_TOLERANCE):
            singer_index += 1
        if (singer_index < len(singer_notes) and abs(reference.time - singer_notes[singer_index].time) <= config.TIME_TOLERANCE):
            singer = singer_notes[singer_index]
            matches.append(
                Match(
                    reference=reference,
                    singer=singer,
                    pitch_difference=abs(
                        reference.midi - singer.midi
                    ),
                    timing_difference=abs(
                        reference.time - singer.time
                    ),
                    loudness_difference=abs(
                        reference.loudness - singer.loudness
                    )
                )
            )
            singer_index += 1
        else:
            matches.append(Match(reference=reference, singer=None, pitch_difference=4.0, timing_difference=0.40, loudness_difference=0.60))
    return matches

def calculate_pitch_score(match: Match) -> float: # just for reference
    difference = match.pitch_difference
    return max(0.0, 100.0 - (difference * 25.0))

def calculate_timing_score(match: Match) -> float:
    difference = match.timing_difference
    if difference <= 0.02:
        return 100.0
    if difference >= 0.40:
        return 0.0
    return ((0.40 - difference) / (0.40 - 0.02)) * 100.0

def calculate_loudness_score(match: Match) -> float:
    difference = match.loudness_difference
    if difference <= 0.05:
        return 100.0
    if difference >= 0.60:
        return 0.0
    return ((0.60 - difference) / (0.60 - 0.05)) * 100.0

def calculate_note_score(match: Match) -> float:
    return fuzzy_note_score(
        pitch_difference=match.pitch_difference,
        timing_difference=match.timing_difference,
        loudness_difference=match.loudness_difference
    )

def calculate_final_score(matches: list[Match]) -> float:
    if not matches:
        return 0.0
    weighted_score = 0.0
    total_duration = 0.0
    for match in matches:
        score = calculate_note_score(match)
        duration = match.reference.duration
        weighted_score += score * duration
        total_duration += duration
    if total_duration == 0:
        return 0.0
    return round(weighted_score / total_duration, 2)