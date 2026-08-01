import numpy as np

from audio import load_audio
from pitch import detect_pitch

audio, sample_rate = load_audio("assets/sample/sample.wav")

frequencies = detect_pitch(audio)

# for i, freq in enumerate(frequencies):
#     if not np.isnan(freq):
#         time = i * 1024 / sample_rate
#         print(f"{time:.2f}s - {freq:.2f} Hz - {i}")

for i, freq in enumerate(frequencies[:30]):
    print(i, freq)