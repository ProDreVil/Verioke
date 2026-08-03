import json

from pathlib import Path
from dataclasses import asdict
from audio import load_audio
from pitch import detect_pitch, extract_notes
from models import Note

def get_reference_path(song_folder):
    song_folder = Path(song_folder)
    reference_path = song_folder / "reference.json"
    if not reference_path.exists():
        generate_reference(song_folder)
    return reference_path

def generate_reference(song_folder: str | Path) -> None:
    song_folder = Path(song_folder)
    vocals_path = song_folder / "vocals.wav"
    reference_path = song_folder / "reference.json"
    audio, sample_rate = load_audio(vocals_path)
    frequencies = detect_pitch(audio)
    notes = extract_notes(frequencies, sample_rate)
    json_notes = [asdict(note) for note in notes]
    with reference_path.open("w", encoding="utf-8") as file:
        json.dump(json_notes, file, indent=4)
    print(f"Reference saved to: {reference_path}")

def load_reference(song_folder: str | Path) -> list[Note]:
    reference_path = get_reference_path(song_folder)
    try:
        with reference_path.open("r", encoding="utf-8") as file:
            json_notes = json.load(file)
            notes = [Note(**note_dict) for note_dict in json_notes]
            return notes
    except (json.JSONDecodeError, FileNotFoundError, TypeError):
        print("Reference is outdated or invalid. Regenerating...")
        generate_reference(song_folder)
        with reference_path.open("r", encoding="utf-8") as file:
            json_notes = json.load(file)
        return [Note(**note_dict) for note_dict in json_notes]