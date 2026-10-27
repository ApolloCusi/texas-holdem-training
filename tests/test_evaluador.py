from src.evaluador import evaluar_cinco, mejor_mano

def c(texto):
    """Convierte '10♠' en ('10', '♠')."""
    return (texto[:-1], texto[-1])

def mano(*textos):
    return[c(t) for t in textos]

def test_corrida_con_as_bajo():
    assert evaluar_cinco(mano("A♠", "2♥", "3♦", "4♣", "5♠")) == (4, 5)

def test_no_hay_escalera_que_da_la_vuelta():
    assert evaluar_cinco(mano("Q♠", "K♥", "A♦", "2♣", "3♠"))[0] == 0

def test_full_house_vence_a_color():
    full = evaluar_cinco(mano("K♠", "K♥", "K♦", "9♣", "9♠"))
    color = evaluar_cinco(mano("A♥", "J♥", "8♥", "5♥", "2♥"))
    assert full > color


def test_par_se_decide_por_la_carta_de_desempate():
    mejor = evaluar_cinco(mano("A♠", "A♥", "K♦", "7♣", "3♠"))
    peor = evaluar_cinco(mano("A♦", "A♣", "Q♦", "7♣", "3♠"))
    assert mejor > peor


def test_mejor_mano_de_siete_cartas():
    siete = mano("A♠", "K♠", "Q♠", "J♠", "10♠", "2♦", "3♣")
    assert mejor_mano(siete) == (8, 14)