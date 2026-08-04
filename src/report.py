from scorer import *
from models import Match, Note

def print_report(reference_notes: list[Note], singer_notes: list[Note], matches: list[Match]) -> None:
    for match in matches:
        pitch_score = calculate_pitch_score(match)
        timing_score = calculate_timing_score(match)
        loudness_score = calculate_loudness_score(match)
        note_score = calculate_note_score(match)
        print(f"Reference : {match.reference.pitch}")
        print(f"Singer    : {match.singer.pitch}")
        print(f"Pitch Δ   : {match.pitch_difference}")
        print(f"Timing Δ  : {match.timing_difference:.3f}s")
        print(f"Loudness Δ: {match.loudness_difference:.6f}")
        print(f"Pitch Score   : {pitch_score:.2f}")
        print(f"Timing Score  : {timing_score:.2f}")
        print(f"Loudness Score: {loudness_score:.2f}")
        print(f"Note Score    : {note_score:.2f}")
        print("-" * 40)
    print(f"Reference Notes: {len(reference_notes)}")
    print(f"Singer Notes: {len(singer_notes)}")
    print(f"Matched Notes: {len(matches)}")
    print(f"Final Score: {calculate_final_score(matches):.2f}")
    print(f"\nDetected {len(singer_notes)} notes.")

# If it detected 0 notes, check which microphone your device is using.
# Might as well check config.py and set the INPUT_DEVICE to 0 (default device mic)