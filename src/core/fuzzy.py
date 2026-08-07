def fuzzy_good(value, start, end):
    if value <= start:
        return 1.0
    if value >= end:
        return 0.0
    return (end - value) / (end - start)


def fuzzy_bad(value, start, end):
    if value <= start:
        return 0.0
    if value >= end:
        return 1.0
    return (value - start) / (end - start)