import re

TIMESTAMP = re.compile(r"\[(\d{2}):(\d{2}):(\d{2})\]")

def load_lrc(path):
    lyrics = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
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
            lyrics.append({
                "time": timestamp,
                "text": text
            })
    return lyrics