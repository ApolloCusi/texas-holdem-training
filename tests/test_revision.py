from src.revision import evaluar_decision


def test_foldear_gratis_es_error():
    assert evaluar_decision("r", 80)[0] == "ERROR"


def test_pasar_con_mano_fuerte_es_mejorable():
    assert evaluar_decision("p", 80)[0] == "MEJORABLE"


def test_apostar_con_mano_debil_es_riesgo():
    assert evaluar_decision("a", 20)[0] == "RIESGO"


def test_decision_razonable():
    assert evaluar_decision("a", 70)[0] == "OK"
    assert evaluar_decision("p", 50)[0] == "OK"