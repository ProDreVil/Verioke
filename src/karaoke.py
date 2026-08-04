from pathlib import Path
from reference import load_reference
from recorder import record_audio
from utils import process_audio
from scorer import compare_notes, calculate_final_score
from report import print_report

def run_karaoke(song_folder: str | Path, duration: int) -> float:
    song_folder = Path(song_folder)
    reference_notes = load_reference(song_folder)
    recording_path = Path("recordings/take1.wav")
    record_audio(recording_path, duration)
    singer_notes = process_audio(recording_path)
    matches = compare_notes(reference_notes, singer_notes)
    print_report(reference_notes, singer_notes, matches)
    return calculate_final_score(matches)