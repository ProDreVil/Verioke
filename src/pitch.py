import math
import librosa

import config
from models import Note

def detect_pitch(audio) -> list:
    frequencies, _, _ = librosa.pyin(
        audio,
        fmin=librosa.note_to_hz(config.MIN_NOTE),
        fmax=librosa.note_to_hz(config.MAX_NOTE),
        frame_length=config.FRAME_LENGTH,
        hop_length=config.HOP_LENGTH
    )
    rms = librosa.feature.rms(
        y=audio,
        frame_length=config.FRAME_LENGTH,
        hop_length=config.HOP_LENGTH
    )[0]
    return frequencies, rms

def extract_notes(frequencies, rms, sample_rate) -> list[Note]:
    notes = []
    for frame_index, frequency in enumerate(frequencies):
        if math.isnan(frequency):
            continue
        time = frame_index * config.HOP_LENGTH / sample_rate
        midi = round(librosa.hz_to_midi(frequency))
        pitch = librosa.midi_to_note(midi)
        loudness = rms[frame_index]
        notes.append(Note(time=time, duration=0.0, frequency=frequency, midi=midi, pitch=pitch, loudness=loudness))
    return merge_notes(notes)

def merge_notes(notes: list[Note]) -> list[Note]:
    if not notes:
        return []
    merged_notes = [notes[0]]
    for note in notes[1:]:
        last_note = merged_notes[-1]
        if note.pitch == last_note.pitch:
            last_note.duration = (note.time + note.duration) - last_note.time
        else:
            merged_notes.append(note)
    return merged_notes