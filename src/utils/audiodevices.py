import sounddevice as sd
import utils.config as config

def get_input_device_name():
    device = sd.query_devices(config.INPUT_DEVICE, "input")
    print(f"Input device: {device['name']}")
    print(f"Device ID: {config.INPUT_DEVICE}")
    print(f"Sample rate: {config.SAMPLE_RATE}")
    return device["name"]

if __name__ == "__main__":
    get_input_device_name()