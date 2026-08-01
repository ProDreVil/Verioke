import numpy as np
import config

from audio import load_audio
from pitch import detect_pitch, extract_notes

audio, sample_rate = load_audio("assets/sample/sample.wav")
frequencies = detect_pitch(audio)
notes = extract_notes(frequencies, sample_rate)

# for i, freq in enumerate(frequencies[:20]):
#     if not np.isnan(freq):
#         time = i * config.HOP_LENGTH / sample_rate
#         print(f"{time:.2f}s - {freq:.2f} Hz - {i} - {notes[i].name}")

for note in notes[:20]:
    print(note)