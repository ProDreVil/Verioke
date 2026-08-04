import math
import librosa

import utils.config as config
from core.models import Note

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
        frequency = float(frequency)
        time = frame_index * config.HOP_LENGTH / sample_rate
        midi = round(librosa.hz_to_midi(frequency))
        pitch = librosa.midi_to_note(midi)
        loudness = float(rms[frame_index])
        notes.append(Note(time=time, duration=0.0, frequency=frequency, midi=midi, pitch=pitch, loudness=loudness))
    return merge_notes(notes)

def merge_notes(notes: list[Note]) -> list[Note]:
    if not notes:
        return []
    merged_notes = []
    current_note = notes[0]
    loudness_sum = current_note.loudness
    frame_count = 1
    for note in notes[1:]:
        gap = note.time - (current_note.time + current_note.duration)
        if (note.pitch == current_note.pitch and gap <= config.MERGE_TIME_THRESHOLD):
            current_note.duration = (note.time + note.duration) - current_note.time
            loudness_sum += note.loudness
            frame_count += 1
        else:
            current_note.loudness = loudness_sum / frame_count
            merged_notes.append(current_note)
            current_note = note
            loudness_sum = current_note.loudness
            frame_count = 1
    current_note.loudness = loudness_sum / frame_count
    merged_notes.append(current_note)
    return merged_notes