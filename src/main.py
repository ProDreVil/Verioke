from reference import load_reference

reference_notes = load_reference("assets/songs/beer")

for note in reference_notes[:20]:
    print(note)