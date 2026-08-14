import sounddevice as sd
import soundfile as sf

import utils.config as config
from utils.audiodevices import get_input_device

def record_audio(output_path: str, duration: float):
    print("Recorder: start")
    recording = sd.rec(
        int(duration * config.SAMPLE_RATE),
        samplerate=config.SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=get_input_device()
    )
    print("Recorder: rec() returned")
    sd.wait()
    print("Recorder: wait finished")
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