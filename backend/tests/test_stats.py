from app.stats import calc_stat

# Test the attack stat calculations for a level 50 Garchomp with different IVs and EVs and Natures

def test_garchomp_attack_stat_level50_noIvs_noEvs_hardyNature():
    assert calc_stat(130, 0, 0, 50, 1.0) == 135

def test_garchomp_attack_stat_level50_31Ivs_noEvs_hardyNature():
    assert calc_stat(130, 31, 0, 50, 1.0) == 150

def test_garchomp_attack_stat_level50_31Ivs_252Evs_hardyNature():
    assert calc_stat(130, 31, 252, 50, 1.0) == 182

def test_garchomp_attack_stat_level50_31Ivs_252Evs_adamantNature():
    assert calc_stat(130, 31, 252, 50, 1.1) == 200