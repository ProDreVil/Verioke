import sounddevice as sd
import soundfile as sf
import numpy as np

import utils.config as config

def record_audio(output_path: str, duration: float):
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

def list_input_devices():
    devices = sd.query_devices()
    for index, device in enumerate(devices):
        if device["max_input_channels"] > 0:
            print(f"{index}:")
            print(f"  Name: {device['name']}")
            print(f"  Host API: {sd.query_hostapis(device['hostapi'])['name']}")
            print(f"  Sample Rate: {device['default_samplerate']}")
            print()