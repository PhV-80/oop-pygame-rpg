"""Tests für Stats System."""

from core.stats import Stats


def test_default_stats():
    """Test: Standard-Stats (Allrounder)."""
    stats = Stats(level=1)

    assert stats.get_level() == 1
    assert stats.get_max_hp() == 50
    assert stats.get_intelligence() == 50
    # INT Bonus: 50 // 5 = 10 MP
    assert stats.get_max_mp() == 30 + 10  # 40
    # INT Bonus: 50 // 10 = 5 Magic Attack
    assert stats.get_magic_attack() == 50 + 5  # 55


def test_warrior_archetype():
    """Test: Krieger (niedrige INT, kein MP)."""
    warrior_stats = {
        'hp': 60, 'mp': 0,
        'attack': 80, 'defense': 120,
        'magic_attack': 20, 'magic_defense': 80,
        'intelligence': 30,  # Niedrig
        'speed': 8, 'luck': 5
    }
    stats = Stats(level=1, base_stats=warrior_stats)

    assert stats.get_max_hp() == 60
    assert stats.get_intelligence() == 30
    # INT Bonus: 30 // 5 = 6 MP (aber Base = 0)
    assert stats.get_max_mp() == 0 + 6  # 6 MP
    assert stats.is_magic_user() == True  # Hat MP durch INT!
    assert stats.get_attack() == 80


def test_mage_archetype():
    """Test: Magier (hohe INT → Bonus MP + Magic Attack)."""
    mage_stats = {
        'hp': 40, 'mp': 70,
        'attack': 20, 'defense': 80,
        'magic_attack': 80, 'magic_defense': 120,
        'intelligence': 100,
        'speed': 12, 'luck': 8
    }
    stats = Stats(level=1, base_stats=mage_stats)

    assert stats.get_max_hp() == 40
    assert stats.get_intelligence() == 100
    # INT Bonus: 100 // 5 = 20 MP
    assert stats.get_max_mp() == 70 + 20  # 90
    # INT Bonus: 100 // 10 = 10 Magic Attack
    assert stats.get_magic_attack() == 80 + 10  # 90


def test_level_scaling_with_int():
    """Test: INT steigt mit Level, beeinflusst MP + Magic Attack."""
    mage_stats = {
        'hp': 40, 'mp': 70,
        'attack': 20, 'defense': 80,
        'magic_attack': 80, 'magic_defense': 120,
        'intelligence': 100,
        'speed': 12, 'luck': 8
    }
    stats = Stats(level=5, base_stats=mage_stats)

    # INT: 100 + (5-1)*2 = 108
    assert stats.get_intelligence() == 108
    # MP: 70 + 4*5 + (108//5) = 70 + 20 + 21 = 111
    assert stats.get_max_mp() == 111
    # Magic Attack: 80 + 4*3 + (108//10) = 80 + 12 + 10 = 102
    assert stats.get_magic_attack() == 102


def test_take_damage():
    """Test: HP-Schaden funktioniert."""
    stats = Stats(level=1)

    stats.take_damage(20)
    assert stats.get_hp() == 30

    stats.take_damage(100)
    assert stats.get_hp() == 0
    assert not stats.is_alive()


def test_heal():
    """Test: Heilung funktioniert."""
    stats = Stats(level=1)

    stats.take_damage(30)
    stats.heal(10)
    assert stats.get_hp() == 30

    stats.heal(100)
    assert stats.get_hp() == 50  # Clamped


def test_mp_usage():
    """Test: MP-Verbrauch funktioniert."""
    mage_stats = {
        'hp': 40, 'mp': 70,
        'attack': 20, 'defense': 80,
        'magic_attack': 80, 'magic_defense': 120,
        'intelligence': 100,
        'speed': 12, 'luck': 8
    }
    stats = Stats(level=1, base_stats=mage_stats)

    assert stats.use_mp(20) == True
    assert stats.get_mp() == 70  # 90 - 20 = 70

    assert stats.use_mp(100) == False  # Nicht genug


def test_mp_restore():
    """Test: MP-Regeneration funktioniert."""
    mage_stats = {
        'hp': 40, 'mp': 70,
        'attack': 20, 'defense': 80,
        'magic_attack': 80, 'magic_defense': 120,
        'intelligence': 100,
        'speed': 12, 'luck': 8
    }
    stats = Stats(level=1, base_stats=mage_stats)

    stats.use_mp(30)
    stats.restore_mp(20)
    assert stats.get_mp() == 80  # 90 - 30 + 20

    stats.restore_mp(100)
    assert stats.get_mp() == 90  # Clamped zu max


if __name__ == "__main__":
    print("Running Stats tests...")
    test_default_stats()
    test_warrior_archetype()
    test_mage_archetype()
    test_level_scaling_with_int()
    test_take_damage()
    test_heal()
    test_mp_usage()
    test_mp_restore()
    print("✅ All tests passed!")
