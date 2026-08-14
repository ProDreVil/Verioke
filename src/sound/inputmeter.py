import sounddevice as sd
import numpy as np
import utils.config as config

from collections import deque
from utils.waveform import level_to_bar
from utils.audiodevices import get_input_device

class InputMeter:
    def __init__(self):
        self.level = 0
        self.stream = None
        self.smoothed_level = 0
        self.history = deque(["▁"] * 18, maxlen=18)

    def callback(self, indata, frames, time, status):
        if status:
            return
        self.level = float(np.sqrt(np.mean(indata ** 2)))
        rms = float(np.sqrt(np.mean(indata ** 2)))
        alpha = 0.2
        self.smoothed_level = (alpha * rms + (1 - alpha) * self.smoothed_level)
        self.history.append(level_to_bar(self.smoothed_level))

    def start(self):
        self.stream = sd.InputStream(
            samplerate=config.SAMPLE_RATE,
            channels=1,
            dtype="float32",
            device=get_input_device(),
            callback=self.callback
        )
        self.stream.start()

    def stop(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()

    def get_wave(self):
        return "".join(self.history)

    def get_level(self):
        return self.smoothed_level