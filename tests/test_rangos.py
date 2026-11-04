from src.rangos import expandir_rango, clase_de_mano


def test_pares_con_mas():
    assert len(expandir_rango("77+")) == 8
    assert len(expandir_rango("22+")) == 13


def test_suited_con_mas():
    assert expandir_rango("ATs+") == {"ATs", "AJs", "AQs", "AKs"}


def test_rango_con_guion():
    assert expandir_rango("A5s-A2s") == {"A5s", "A4s", "A3s", "A2s"}


def test_mano_suelta_y_varios_tokens():
    assert expandir_rango("KQo, JTs") == {"KQo", "JTs"}


def test_clase_de_mano():
    assert clase_de_mano(("A", "♠"), ("K", "♠")) == "AKs"
    assert clase_de_mano(("10", "♥"), ("A", "♦")) == "ATo"
    assert clase_de_mano(("7", "♣"), ("7", "♦")) == "77"