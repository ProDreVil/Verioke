from models import Note
import config

def compare_notes(reference_notes: list[Note], singer_notes: list[Note]) -> list[tuple[Note, Note]]:
    matches = []
    for reference_note in reference_notes:
        closest_note = None
        closest_difference = float("inf")
        for singer_note in singer_notes:
            difference = abs(reference_note.time - singer_note.time)
            if (difference < closest_difference and difference <= config.TIME_TOLERANCE):
                closest_difference = difference
                closest_note = singer_note
        if closest_note is not None:
            matches.append((reference_note, closest_note))
    return matches