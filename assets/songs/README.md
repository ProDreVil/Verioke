# Songs Directory

This directory is intentionally left empty.

Verioke does **not** include copyrighted songs, album covers, instrumentals, vocals, or lyrics in this repository.

To add your own songs, create a new folder inside `assets/songs/` using the following structure:

```text
Song Name/
├── cover.jpg
├── instrumental.wav
├── lyrics.lrc
├── vocals.wav
└── reference.json
```

## File Descriptions

| File               | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| `cover.jpg`        | Album cover or custom artwork displayed in the UI.         |
| `instrumental.wav` | Instrumental version used during karaoke playback.         |
| `lyrics.lrc`       | Time-synchronized lyrics.                                  |
| `vocals.wav`       | Original vocal track used to generate the reference notes. |
| `reference.json`   | Generated note reference used for scoring.                 |

## Importing Songs

Use Verioke's song `importer.py` to generate the required `reference.json` file from the provided vocals.

## Important

Only use songs and media that you have the legal right to use.

This repository does not distribute copyrighted music or artwork.
