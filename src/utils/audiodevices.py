import sounddevice as sd

def get_input_device():
    input_device, _ = sd.default.device
    return input_device

def get_output_device():
    _, output_device = sd.default.device
    return output_device

def get_input_device_name():
    device_id = get_input_device()
    device = sd.query_devices(device_id, "input")
    print(f"Input device: {device['name']}")
    print(f"Device ID: {device_id}")
    return device["name"]

def get_output_device_name():
    device_id = get_output_device()
    device = sd.query_devices(device_id, "output")
    print(f"Output device: {device['name']}")
    print(f"Device ID: {device_id}")
    return device["name"]

if __name__ == "__main__":
    get_input_device_name()
    get_output_device_name()