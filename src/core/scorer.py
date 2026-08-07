from core.models import Match, Note
from core.fuzzy import fuzzy_good

import utils.config as config

def compare_notes(reference_notes: list[Note], singer_notes: list[Note]) -> list[Match]:
    matches = []
    reference_index = 0
    singer_index = 0
    while (reference_index < len(reference_notes) and singer_index < len(singer_notes)):
        reference = reference_notes[reference_index]
        singer = singer_notes[singer_index]
        time_difference = abs(reference.time - singer.time)
        if time_difference <= config.TIME_TOLERANCE:
            matches.append(
                Match(
                    reference=reference, singer=singer, pitch_difference=abs(reference.midi - singer.midi),
                    timing_difference=time_difference,
                    loudness_difference=abs(reference.loudness - singer.loudness)
                )
            )
            reference_index += 1
            singer_index += 1
        elif singer.time < reference.time:
            singer_index += 1
        else:
            reference_index += 1
    return matches

def calculate_pitch_score(match: Match) -> float:
    """
    Measures how close the singer's pitch is
    compared to the reference pitch.
    Every semitone difference reduces the score.
    """
    return max(0.0, 100.0 - (match.pitch_difference * 25.0))

def calculate_timing_score(match: Match) -> float:
    """
    Uses fuzzy membership.
    A smaller timing difference has a higher score.
    """
    quality = fuzzy_good(match.timing_difference, 0.02, 0.20)
    return quality * 100

def calculate_loudness_score(match: Match) -> float:
    """
    Uses fuzzy membership.
    Similar loudness to the reference receives a higher score.
    """
    quality = fuzzy_good(match.loudness_difference, 0.01, 0.10)
    return quality * 100

def calculate_note_score(match: Match) -> float:
    """
    Combines all scoring factors.
    Pitch:
    60% - Most important in karaoke
    Timing:
    25% - Singing at the correct moment
    Loudness:
    15% - Volume consistency
    """
    pitch_score = calculate_pitch_score(match)
    timing_score = calculate_timing_score(match)
    loudness_score = calculate_loudness_score(match)
    return (pitch_score * 0.60 + timing_score * 0.25 + loudness_score * 0.15)

def calculate_final_score(matches: list[Match]) -> float:
    """
    Calculates the average performance score.
    """
    if not matches:
        return 0.0
    total_score = 0.0
    for match in matches:
        total_score += calculate_note_score(match)
    return total_score / len(matches)