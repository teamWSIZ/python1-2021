def time_to_seconds(time: str) -> int:
    h, m, s = time.split(':')
    res = int(h) * 3600 + int(m) * 60 + int(s)
    return res
