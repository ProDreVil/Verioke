```
Verioke/
│
├── .venv/                          # Virtual environment
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
├── recordings/
│
├── src/
│   ├── main.py                     # Entry point
│   ├── recorder.py                 # Records microphone input
│   ├── audio.py                    # Loads audio files
│   ├── pitch.py                    # Detects notes
│   ├── scorer.py                   # Calculates score
│   ├── utils.py                    # Helper functions
│   ├── config.py                   # Constants/settings
│   ├── gui.py                      # Visual interpretation
│   ├── models.py                   # Dataclasses
│   └── README.md                   # Project Structure
│
├── tests/
│
├── plan.txt
├── requirements.txt
└── README.md
```