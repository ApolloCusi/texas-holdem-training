import pytest
from src.bankroll import riesgo_ruina_teorico, simular_bankroll


def test_riesgo_teorico_ejemplo():
    assert riesgo_ruina_teorico(5, 90, 3000) == pytest.approx(2.46, abs=0.05)


def test_riesgo_teorico_winrate_negativo():
    assert riesgo_ruina_teorico(-2, 90, 3000) == 100.0


def test_simulacion_sin_ruina():
    r = simular_bankroll(10, 50, 100, manos=10000, simulaciones=200)
    assert r["riesgo_ruina"] == 0


def test_simulacion_ruina_segura():
    r = simular_bankroll(-20, 10, 1, manos=10000, simulaciones=100)
    assert r["riesgo_ruina"] == 100