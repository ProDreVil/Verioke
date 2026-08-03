from reference import load_reference
from recorder import record_audio, list_input_devices
from scorer import compare_notes
from utils import process_audio

reference_notes = load_reference("assets/songs/beer")
# record_audio("recordings/take1.wav", 5)
singer_notes = process_audio("recordings/take1.wav")

matches = compare_notes(reference_notes, singer_notes)

for reference, singer in matches[:10]:
    print(f"{reference.pitch:>3} ({reference.time:.2f}s)" f" -> "f"{singer.pitch:>3} ({singer.time:.2f}s)")


# list_input_devices()

# for note in reference_notes[:20]:
#     print(note)