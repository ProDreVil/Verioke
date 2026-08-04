```
Verioke/
│
├── .venv/                          # Virtual environment
│
│
├── assets/
│   ├── grade/
│   │   └── 1~10.jpg                # Score
│   │
│   ├── songs/
│   │   ├── Song Name/
│   │   │   ├── cover.jpg
│   │   │   ├── instrumental.wav
│   │   │   ├── lyrics.lrc
│   │   │   ├── reference.json
│   │   │   └── vocals.wav
│   │   │
│   │   └── Another Song/
│   │       ├── cover.jpg
│   │       ├── instrumental.wav
│   │       ├── lyrics.lrc
│   │       ├── reference.json
│   │       └── vocals.wav
│   │
│   ├── tests/
│   │
│   └── videos/
│       └── video.mp3               # Background videos playing
│
│
├── recordings/
│
│
├── src/
│   ├── main.py                     # Entry point
│   │
│   ├── core/
│   │   ├── fuzzy.py                # Fuzzy scoring logic
│   │   ├── karaoke.py              # Main karaoke workflow
│   │   ├── models.py               # Dataclasses
│   │   └── scorer.py               # Calculates score
│   │
│   ├── interface/
│   │   ├── gui.py                  # Visual interpretation
│   │   └── report.py               # Console reports
│   │
│   ├── songs/
│   │   ├── importer.py             # Adds songs
│   │   └── reference.py            # Generate/load reference notes
│   │
│   ├── sound/
│   │   ├── audio.py                # Loads audio files
│   │   ├── pitch.py                # Detects notes/pitch
│   │   └── recorder.py             # Records microphone input
│   │
│   ├── test/
│   │   └── test.py                 # Code stash
│   │
│   ├── utils/
│   │   ├── config.py               # Constants/settings
│   │   └── helpers.py              # Helper functions
│   │
│   └── README.md                   # You are here
│
│
├── plan.txt
│
├── requirements.txt
│
└── README.md
```