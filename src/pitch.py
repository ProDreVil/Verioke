import librosa
import config

def detect_pitch(audio):
    frequencies, voiced_flag, voiced_probability = librosa.pyin(
        audio,
        fmin=librosa.note_to_hz(config.MIN_NOTE),
        fmax=librosa.note_to_hz(config.MAX_NOTE),
        frame_length=config.FRAME_LENGTH,
        hop_length=config.HOP_LENGTH
    )

    return frequencies