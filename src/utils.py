from pathlib import Path
from audio import load_audio
from pitch import detect_pitch, extract_notes, merge_notes
from models import Note

def process_audio(audio_path: str | Path) -> list[Note]:
    audio, sample_rate = load_audio(audio_path)
    frequencies, rms = detect_pitch(audio)
    notes = extract_notes(frequencies, rms, sample_rate)
    return merge_notes(notes)