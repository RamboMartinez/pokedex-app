import math

def calc_stat (base: int, iv: int, ev: int, level: int, nature: int) -> int:
    """Calculate a Pokemon's final stat (any stat except HP)."""
    return math.floor(((((2 * base + iv + (ev / 4)) * level) / 100) + 5) * nature)