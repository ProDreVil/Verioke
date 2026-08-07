from core.models import Match, Note
from core.fuzzy import fuzzy_note_score

import utils.config as config


def compare_notes(reference_notes: list[Note], singer_notes: list[Note]) -> list[Match]:
    matches = []
    reference_index = 0
    singer_index = 0
    while (
        reference_index < len(reference_notes)
        and singer_index < len(singer_notes)
    ):
        reference = reference_notes[reference_index]
        singer = singer_notes[singer_index]

        time_difference = abs(
            reference.time - singer.time
        )

        if time_difference <= config.TIME_TOLERANCE:
            matches.append(
                Match(
                    reference=reference,
                    singer=singer,
                    pitch_difference=abs(
                        reference.midi - singer.midi
                    ),
                    timing_difference=time_difference,
                    loudness_difference=abs(
                        reference.loudness - singer.loudness
                    )
                )
            )

            reference_index += 1
            singer_index += 1

        elif singer.time < reference.time:
            singer_index += 1

        else:
            reference_index += 1

    return matches


def calculate_pitch_score(match: Match) -> float: # just for reference
    difference = match.pitch_difference
    return max(
        0.0,
        100.0 - (difference * 25.0)
    )

def calculate_timing_score(match: Match) -> float:
    difference = match.timing_difference

    if difference <= 0.02:
        return 100.0

    if difference >= 0.40:
        return 0.0

    return (
        (0.40 - difference)
        / (0.40 - 0.02)
    ) * 100.0


def calculate_loudness_score(match: Match) -> float:

    difference = match.loudness_difference

    if difference <= 0.05:
        return 100.0

    if difference >= 0.60:
        return 0.0

    return (
        (0.60 - difference)
        / (0.60 - 0.05)
    ) * 100.0

def calculate_note_score(match: Match) -> float:
    return fuzzy_note_score(
        pitch_difference=match.pitch_difference,
        timing_difference=match.timing_difference,
        loudness_difference=match.loudness_difference
    )

def calculate_final_score(matches: list[Match]) -> float:
    if not matches:
        return 0.0

    total_score = sum(
        calculate_note_score(match)
        for match in matches
    )

    return round(
        total_score / len(matches),
        2
    )