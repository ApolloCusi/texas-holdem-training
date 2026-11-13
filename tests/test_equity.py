import pytest
from src.cartas import parsear_carta, parsear_cartas
from src.equity import calcular_equity


def test_parsear_carta():
    assert parsear_carta("As") == ("A", "♠")
    assert parsear_carta("10h") == ("10", "♥")
    assert parsear_carta("Td") == ("10", "♦")


def test_parsear_carta_invalida():
    with pytest.raises(ValueError):
        parsear_carta("Zx")


def test_escalera_real_gana_siempre():
    mano = parsear_cartas("As Ks")
    mesa = parsear_cartas("Qs Js 10s 2d 3c")
    assert calcular_equity(mano, mesa, oponentes=2, simulaciones=200) == 100.0


def test_cartas_repetidas():
    with pytest.raises(ValueError):
        calcular_equity(parsear_cartas("As Ks"), parsear_cartas("As 2d 3c"))


def test_ases_contra_reyes():
    equity = calcular_equity(
        parsear_cartas("As Ah"),
        mano_rival=parsear_cartas("Ks Kh"),
        simulaciones=2000,
    )
    assert 77 <= equity <= 87