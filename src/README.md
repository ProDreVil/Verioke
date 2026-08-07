```
Verioke/
│
├── .venv/                          # Virtual environment
│
│
├── assets/
│   ├── grade/
│   │   └── grade.jpg               # Rating
│   │
│   ├── songs/
│   │   ├── Song Name/
│   │   │   ├── cover.jpg           # Cover photo
│   │   │   ├── instrumental.wav    # Background music
│   │   │   ├── lyrics.lrc          # Lyrics duh
│   │   │   ├── reference.json      # Stores necessary values for computation
│   │   │   └── vocals.wav          # Is compared to the user's performance
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
│       └── video.mp4               # Background videos playing
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
│   │   ├── screens/
│   │   │   ├── home.py             # Shows available songs
│   │   │   ├── performance.py      # Actual singing
│   │   │   └── results.py          # Results display
│   │   │
│   │   ├── widgets/
│   │   │   ├── background.py       # Background video playing
│   │   │   ├── progress.py         # Progress bar
│   │   │   ├── songcard.py         # Song card
│   │   │   ├── videoplayer.py      # Video player
│   │   │   └── visualizer.py       # visualizer
│   │   │
│   │   ├── gui.py                  # Controls the screen switching
│   │   ├── report.py               # Console reports
│   │   ├── sfx.py                  # Sound effects
│   │   └── theme.py                # Global themes
│   │
│   ├── songs/
│   │   ├── importer.py             # Adds songs
│   │   └── reference.py            # Generates/loads reference notes
│   │
│   ├── sound/
│   │   ├── audio.py                # Loads audio files
│   │   ├── inputmeter.py           # Shows waveform meter
│   │   ├── pitch.py                # Detects notes/pitch
│   │   ├── player.py               # Plays the instrumental
│   │   └── recorder.py             # Records microphone input
│   │
│   ├── test/
│   │   ├── checker.py              # Checks whether wavs files are valid
│   │   ├── sync.py                 # Checks if the song, instrumental, recoder syncs
│   │   └── test.py                 # Code stash
│   │
│   ├── utils/
│   │   ├── audiodevices.py         # Shows the current input device
│   │   ├── config.py               # Constants/settings
│   │   ├── helpers.py              # Helper functions
│   │   └── lrc.py                  # Lyric utils
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