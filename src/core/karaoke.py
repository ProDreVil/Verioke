from pathlib import Path
from songs.reference import load_reference
from sound.recorder import record_audio
from sound.audio import get_audio_duration
from utils.helpers import process_audio, get_recording_path
from core.scorer import compare_notes, calculate_final_score
from interface.report import print_report

def run_karaoke(song_folder: str | Path) -> float:
    song_folder = Path(song_folder)
    song_name = song_folder.name
    instrumental_path = song_folder / "instrumental.wav"
    duration = get_audio_duration(instrumental_path)
    reference_notes = load_reference(song_folder)
    recording_path = get_recording_path(song_name)
    record_audio(recording_path, duration)
    singer_notes = process_audio(recording_path)
    matches = compare_notes(reference_notes, singer_notes)
    print_report(reference_notes, singer_notes, matches)
    final_score = calculate_final_score(matches)
    return {"score": final_score, "matches": matches, "reference_notes": reference_notes, "singer_notes": singer_notes}