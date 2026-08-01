import math
import librosa

import config
from models import Note

def detect_pitch(audio):
    frequencies, _, _ = librosa.pyin(
        audio,
        fmin=librosa.note_to_hz(config.MIN_NOTE),
        fmax=librosa.note_to_hz(config.MAX_NOTE),
        frame_length=config.FRAME_LENGTH,
        hop_length=config.HOP_LENGTH
    )
    return frequencies

def extract_notes(frequencies, sample_rate):
    notes = []
    for frame, frequency in enumerate(frequencies):
        if math.isnan(frequency):
            continue
        time = frame * config.HOP_LENGTH / sample_rate
        midi = round(librosa.hz_to_midi(frequency))
        name = librosa.midi_to_note(midi)
        notes.append(Note(time=time, frequency=frequency, midi=midi, name=name))
    return notes