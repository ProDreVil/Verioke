from reference import load_reference
from recorder import record_audio, list_input_devices
from scorer import compare_notes, calculate_pitch_accuracy
from utils import process_audio

reference_notes = load_reference("assets/songs/beer")
# record_audio("recordings/take1.wav", 5)
singer_notes = process_audio("recordings/take1.wav")

matches = compare_notes(reference_notes, singer_notes)
score = calculate_pitch_accuracy(matches)

print(f"Reference Notes: {len(reference_notes)}")
print(f"Singer Notes: {len(singer_notes)}")
print(f"Matched Notes: {len(matches)}")

# for reference, singer in matches[:10]:
#     print(f"{reference.pitch:>3} ({reference.time:.2f}s)" f" -> "f"{singer.pitch:>3} ({singer.time:.2f}s)")

for reference, singer in matches:
    print(f"Ref: {reference.pitch:>3} ({reference.midi}) -> Singer: {singer.pitch:>3} ({singer.midi})")

# list_input_devices()

# for note in reference_notes[:20]:
#     print(note)