import sounddevice as sd
import soundfile as sf
import numpy as np

import config

def record_audio(output_path: str, duration: float):
    """Records audio from the selected microphone and saves it as a WAV file."""
    print("Recording...")
    recording = sd.rec(
        int(duration * config.SAMPLE_RATE),
        samplerate=config.SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=config.INPUT_DEVICE
    )
    sd.wait()
    sf.write(output_path, recording, config.SAMPLE_RATE)
    print(f"Recording saved to: {output_path}")

