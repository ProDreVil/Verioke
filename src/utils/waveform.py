def level_to_bar(level):
    if level < 0.01:
        return "▁"
    elif level < 0.02:
        return "▂"
    elif level < 0.03:
        return "▃"
    elif level < 0.05:
        return "▄"
    elif level < 0.07:
        return "▅"
    elif level < 0.10:
        return "▆"
    elif level < 0.15:
        return "▇"
    return "█"