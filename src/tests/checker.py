from pathlib import Path

ROOT = Path("assets")
SIGNATURES = {
    b"RIFF": "WAV",
    b"ID3": "MP3",
    b"fLaC": "FLAC",
    b"OggS": "OGG",
}

def detect_format(file: Path) -> str:
    with open(file, "rb") as f:
        header = f.read(16)
    if header.startswith(b"RIFF") and header[8:12] == b"WAVE":
        return "WAV"
    if header.startswith(b"ID3"):
        return "MP3"
    if len(header) >= 2 and header[0] == 0xFF and (header[1] & 0xE0) == 0xE0:
        return "MP3"
    if header.startswith(b"fLaC"):
        return "FLAC"
    if header.startswith(b"OggS"):
        return "OGG"
    return "Unknown"

def check_audio_files(root: Path):
    print("Checking .wav files...\n")
    total = 0
    good = 0
    bad = 0
    for file in root.rglob("*.wav"):
        total += 1
        actual = detect_format(file)
        if actual == "WAV":
            good += 1
            print(f"✅ {file}")
        else:
            bad += 1
            print(f"❌ {file}")
            print(f"   Extension : .wav")
            print(f"   Actual    : {actual}")
            print()
    print("-" * 40)
    print(f"Checked : {total}")
    print(f"Valid   : {good}")
    print(f"Invalid : {bad}")

if __name__ == "__main__":
    check_audio_files(ROOT)