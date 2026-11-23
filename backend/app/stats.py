import math

def calc_stat (base: int, iv: int, ev: int, level: int, nature: int) -> int:
    """Calculate a Pokemon's final stat (any stat except HP)."""

    if (iv < 0):
        print("input for IVs was below minimum. IVs set to 0")
        iv = 0
    elif (iv > 31):
        print("input for IVs was higher than maximum. IVs set to 31")
        iv = 31

    if (ev < 0):
        print("input for EVs was below minimum. EVs set to 0")
        ev = 0
    elif (ev > 252):
        print("input for EVs was higher than maximum. EVs set to 252")
        ev = 252

    if (level < 1):
        print("input for Level was below minimum. Level set to 1")
        level = 1
    elif (level > 100):
        print("input for Level was higher than maximum. Level set to 100")
        level = 100

    return math.floor(((((2 * base + iv + (ev / 4)) * level) / 100) + 5) * nature)

def calc_health (base: int, iv: int, ev: int, level: int) -> int:
    """Calculate a Pokemon's final stat (any stat except HP)."""

    if (iv < 0):
        print("input for IVs was below minimum. IVs set to 0")
        iv = 0
    elif (iv > 31):
        print("input for IVs was higher than maximum. IVs set to 31")
        iv = 31

    if (ev < 0):
        print("input for EVs was below minimum. EVs set to 0")
        ev = 0
    elif (ev > 252):
        print("input for EVs was higher than maximum. EVs set to 252")
        ev = 252

    if (level < 1):
        print("input for Level was below minimum. Level set to 1")
        level = 1
    elif (level > 100):
        print("input for Level was higher than maximum. Level set to 100")
        level = 100

        
    return math.floor(((((2 * base + iv + (ev / 4)) * level) / 100) + level + 10))