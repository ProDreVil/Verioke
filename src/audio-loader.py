import librosa
import librosa.display
import matplotlib.pyplot as plt


def load_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)

    print("===== Audio Information =====")
    print(f"File: {file_path}")
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Duration: {librosa.get_duration(y=audio, sr=sample_rate):.2f} seconds")
    print(f"Total Samples: {len(audio)}")

    return audio, sample_rate


def plot_waveform(audio, sample_rate):
    plt.figure(figsize=(12, 4))

    librosa.display.waveshow(
        audio,
        sr=sample_rate
    )

    plt.title("Audio Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    audio, sample_rate = load_audio("assets/sample/sample.wav")
    plot_waveform(audio, sample_rate)