from reference import load_reference
from recorder import record_audio

reference_notes = load_reference("assets/songs/beer")

record_audio(output_path="recordings/take1.wav", duration=5)

# for note in reference_notes[:20]:
#     print(note)