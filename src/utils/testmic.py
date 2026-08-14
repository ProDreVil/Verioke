import sounddevice as sd

from utils.audiodevices import get_input_device

def callback(indata, frames, time, status):
    if status:
        print(status)

    volume = abs(indata).max()
    print("Volume:", volume)

with sd.InputStream(device=get_input_device, channels=1, samplerate=44100, callback=callback):
    print("Listening... Speak into the microphone.")
    input("Press Enter to stop...\n")