from models import Match, Note
import config

def compare_notes(reference_notes: list[Note], singer_notes: list[Note]) -> list[Match]:
    matches = []
    reference_index = 0
    singer_index = 0
    while (reference_index < len(reference_notes) and singer_index < len(singer_notes)):
        reference = reference_notes[reference_index]
        singer = singer_notes[singer_index]
        difference = abs(reference.time - singer.time)
        if difference <= config.TIME_TOLERANCE:
            matches.append(Match(
                reference=reference,
                singer=singer,
                pitch_difference=abs(reference.midi - singer.midi),
                timing_difference=abs(reference.time - singer.time),
                loudness_difference=abs(reference.loudness - singer.loudness)
            ))
            reference_index += 1
            singer_index += 1
        elif singer.time < reference.time:
            singer_index += 1
        else:
            reference_index += 1
    return matches

# def calculate_pitch_accuracy(matches: list[Match]) -> float:
#     if not matches:
#         return 0.0
#     correct = 0
#     for match in matches:
#         if match.pitch_difference == 0:
#             correct += 1
#     return (correct / len(matches)) * 100

def calculate_pitch_score(match: Match) -> float:
    return max(0.0, 100.0 - (match.pitch_difference * 25.0))

def calculate_timing_score(match: Match) -> float:
    difference = match.timing_difference
    if difference <= 0.02:
        return 100.0
    elif difference <= 0.05:
        return 90.0
    elif difference <= 0.10:
        return 75.0
    elif difference <= 0.20:
        return 50.0
    return 0.0

def calculate_loudness_score(match: Match) -> float:
    difference = match.loudness_difference
    if difference <= 0.01:
        return 100.0
    elif difference <= 0.03:
        return 90.0
    elif difference <= 0.05:
        return 75.0
    elif difference <= 0.10:
        return 50.0
    return 0.0

def calculate_note_score(match: Match) -> float:
    pitch = calculate_pitch_score(match)
    timing = calculate_timing_score(match)
    loudness = calculate_loudness_score(match)
    return (pitch * 0.60 + timing * 0.25 + loudness * 0.15)

def calculate_final_score(matches: list[Match]) -> float:
    if not matches:
        return 0.0
    total_score = 0.0
    for match in matches:
        total_score += calculate_note_score(match)
    return total_score / len(matches)