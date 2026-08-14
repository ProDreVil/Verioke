import sounddevice as sd

for i, device in enumerate(sd.query_devices()):
    print(i, device["name"], "input: ", device["max_input_channels"], " - output: ", device["max_output_channels"])