from songs.reference import load_reference
# from recorder import record_audio, list_input_devices
from core.scorer import *
from utils.helpers import process_audio

# notes = process_audio("recordings/take1.wav")
# for note in notes[:10]:
#     print(note)
# print(f"Total merged notes: {len(notes)}")

reference_notes = load_reference("assets/songs/beer")
# record_audio("recordings/take1.wav", 5)
singer_notes = process_audio("recordings/take1.wav")

matches = compare_notes(reference_notes, singer_notes)
# score = calculate_pitch_accuracy(matches)

for match in matches:
    pitch_score = calculate_pitch_score(match)
    timing_score = calculate_timing_score(match)
    loudness_score = calculate_loudness_score(match)
    overall_score = calculate_note_score(match)
    print(f"Reference : {match.reference.pitch}")
    print(f"Singer    : {match.singer.pitch}")
    print(f"Pitch Δ   : {match.pitch_difference}")
    print(f"Timing Δ  : {match.timing_difference:.3f}s")
    print(f"Loudness Δ: {match.loudness_difference:.6f}")
    print(f"Pitch Score   : {pitch_score:.2f}")
    print(f"Timing Score  : {timing_score:.2f}")
    print(f"Loudness Score: {loudness_score:.2f}")
    print(f"Overall Score: {overall_score:.2f}")
    print("-" * 40)

print(f"Reference Notes: {len(reference_notes)}")
print(f"Singer Notes: {len(singer_notes)}")
print(f"Matched Notes: {len(matches)}")
print(f"Final Score: {calculate_final_score(matches):.2f}")

# for reference, singer in matches[:10]:
#     print(f"{reference.pitch:>3} ({reference.time:.2f}s)" f" -> "f"{singer.pitch:>3} ({singer.time:.2f}s)")

# for reference, singer in matches:
#     print(f"Ref: {reference.pitch:>3} ({reference.midi}) -> Singer: {singer.pitch:>3} ({singer.midi})")

# list_input_devices()

# for note in reference_notes[:20]:
#     print(note)