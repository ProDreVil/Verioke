from models import Note
import config

def compare_notes(reference_notes: list[Note], singer_notes: list[Note]) -> list[tuple[Note, Note]]:
    matches = []
    reference_index = 0
    singer_index = 0
    while (reference_index < len(reference_notes) and singer_index < len(singer_notes)):
        reference = reference_notes[reference_index]
        singer = singer_notes[singer_index]
        difference = abs(reference.time - singer.time)
        if difference <= config.TIME_TOLERANCE:
            matches.append((reference, singer))
            reference_index += 1
            singer_index += 1
        elif singer.time < reference.time:
            singer_index += 1
        else:
            reference_index += 1
    return matches

def calculate_pitch_accuracy(matches: list[tuple[Note, Note]]) -> float:
    if not matches:
        return 0.0
    correct = 0
    for reference, singer in matches:
        if reference.midi == singer.midi:
            correct += 1
    print(f"Correct Notes: {correct}")
    return (correct/len(matches)) * 100