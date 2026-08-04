```
Verioke/
│
├── .venv/                          # Virtual environment
│
│
├── assets/
│   ├── sample/
│   │   └── sample.wav/
│   │
│   └── songs/
│       ├── Song Name/
│       │   ├── cover.jpg
│       │   ├── instrumental.wav
│       │   ├── lyrics.lrc
│       │   ├── reference.json
│       │   └── vocals.wav
│       │
│       └── Another Song/
│           ├── cover.jpg
│           ├── instrumental.wav
│           ├── lyrics.lrc
│           ├── reference.json
│           └── vocals.wav
│
│
├── recordings/
│
│
├── src/
│   ├── main.py                     # Entry point
│   │
│   ├── core/
│   │   ├── fuzzy.py                # Handles the fuzzy logic
│   │   ├── karaoke.py              # Processes the karaoke
│   │   ├── models.py               # Dataclasses
│   │   └── scorer.py               # Calculates score
│   │
│   ├── interface/
│   │   ├── gui.py                  # Visual interpretation
│   │   └── report.py               # Printing and basic TUI
│   │
│   ├── songs/
│   │   ├── importer.py             # Adds songs
│   │   └── reference.py            # Generate/load reference notes
│   │
│   ├── sound/
│   │   ├── audio.py                # Loads audio files
│   │   ├── pitch.py                # Detects notes
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