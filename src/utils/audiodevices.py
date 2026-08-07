import sounddevice as sd

def get_input_device_name():
    device = sd.query_devices(kind="input")
    return device["name"]