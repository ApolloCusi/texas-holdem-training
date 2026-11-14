from src.cartas import parsear_cartas
from src.juego import bot_iguala


def test_bot_con_escalera_real_siempre_iguala():
    bot = {"mano": parsear_cartas("As Ks")}
    mesa = parsear_cartas("Qs Js 10s 2d 3c")
    assert bot_iguala(bot, mesa, bote_actual=80) is True