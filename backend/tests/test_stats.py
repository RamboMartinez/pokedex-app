from app.stats import calc_stat, calc_health

# Test the attack stat calculations for a level 50 Garchomp with different IVs and EVs and Natures

# def test_garchomp_attack_stat_level50_noIvs_noEvs_hardyNature():
#     assert calc_stat(130, 0, 0, 50, 1.0) == 135

# def test_garchomp_attack_stat_level50_31Ivs_noEvs_hardyNature():
#     assert calc_stat(130, 31, 0, 50, 1.0) == 150

# def test_garchomp_attack_stat_level50_31Ivs_252Evs_hardyNature():
#     assert calc_stat(130, 31, 252, 50, 1.0) == 182

# def test_garchomp_attack_stat_level50_31Ivs_252Evs_adamantNature():
#     assert calc_stat(130, 31, 252, 50, 1.1) == 200

def test_garchomp_health_stat_level50_0Ivs_0Evs():
    assert calc_health(108, 0, 0, 50) == 168

def test_garchomp_health_stat_level50_31Ivs_0Evs():
    assert calc_health(108, 31, 0, 50) == 183

def test_garchomp_health_stat_level50_31Ivs_252Evs():
    assert calc_health(108, 31, 252, 50) == 215

def test_garchomp_health_stat_level50_31Ivs_250Evs():
    assert calc_health(108, 31, 250, 50) == 214

def test_garchomp_health_stat_level100_0Ivs_0Evs():
    assert calc_health(108, 0, 0, 100) == 326

def test_garchomp_health_stat_level100_31Ivs_252Evs():
    assert calc_health(108, 31, 252, 100) == 420