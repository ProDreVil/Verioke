import re

TIMESTAMP = re.compile(r"\[(\d{2}):(\d{2}):(\d{2})\]")

TITLE = re.compile(r"\[ti:(.*)\]")
ARTIST = re.compile(r"\[ar:(.*)\]")


def load_lrc(path):
    data = {
        "title": "",
        "artist": "",
        "lyrics": []
    }
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
            title = TITLE.match(line)
            if title:
                data["title"] = title.group(1)
                continue
            artist = ARTIST.match(line)
            if artist:
                data["artist"] = artist.group(1)
                continue
            match = TIMESTAMP.match(line)
            if not match:
                continue
            minute = int(match.group(1))
            second = int(match.group(2))
            hundredth = int(match.group(3))
            timestamp = (
                minute * 60
                + second
                + hundredth / 100
            )
            text = line[match.end():]
            data["lyrics"].append({
                "time": timestamp,
                "text": text
            })
    return data