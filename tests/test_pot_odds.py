import pytest
from src.pot_odds import equity_necesaria, equity_por_outs

def test_equity_necesaria_media_apuesta():
    assert equity_necesaria(100, 50) == pytest.approx(25.0)

def test_equity_necesaria_apuesta_del_bote():
    assert equity_necesaria(100, 100) == pytest.approx(33.33, abs=0.01)

def test_regla_del_2_y_4():
    assert equity_por_outs(9, 2) == 36
    assert equity_por_outs(9, 1) == 18