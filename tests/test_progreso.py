import pytest
from src import progreso


def test_guardar_y_cargar(tmp_path, monkeypatch):
    monkeypatch.setattr(progreso, "ARCHIVO", tmp_path / "p.json")
    progreso.guardar_sesion("pot_odds", 4, 5)
    progreso.guardar_sesion("pot_odds", 3, 5)
    datos = progreso.cargar_progreso()
    assert len(datos["pot_odds"]) == 2
    aciertos, total, porcentaje = progreso.resumen_modulo(datos["pot_odds"])
    assert (aciertos, total) == (7, 10)
    assert porcentaje == pytest.approx(70.0)