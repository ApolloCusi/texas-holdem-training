from src.juego import jugar_partida
from src.pot_odds import entrenar_pot_odds
from src.rangos import entrenar_rangos
from src.equity import entrenar_equity, calculadora_equity
from src.progreso import guardar_sesion, mostrar_progreso


def sesion_pot_odds():
    aciertos, total = entrenar_pot_odds()
    guardar_sesion("pot_odds", aciertos, total)


def sesion_rangos():
    aciertos, total = entrenar_rangos()
    guardar_sesion("rangos_preflop", aciertos, total)


def sesion_equity():
    aciertos, total = entrenar_equity()
    guardar_sesion("equity", aciertos, total)

from src.bankroll import simulador_bankroll

# Para agregar un módulo nuevo: una línea aquí, antes de "Ver mi progreso".
OPCIONES = [
    ("Jugar partida contra bots", jugar_partida),
    ("Entrenar pot odds", sesion_pot_odds),
    ("Entrenar rangos preflop", sesion_rangos),
    ("Entrenar equity (mano vs mano)", sesion_equity),
    ("Calculadora de equity", calculadora_equity),
    ("Simulador de bankroll", simulador_bankroll),
    ("Ver mi progreso", mostrar_progreso),
]


def mostrar_menu():
    print("\n=== TEXAS HOLD'EM TRAINING ===")
    for numero, (texto, _) in enumerate(OPCIONES, start=1):
        print(f"{numero}. {texto}")
    print("0. Salir")


def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "0":
            print("¡Hasta la próxima!")
            break
        if opcion.isdigit() and 1 <= int(opcion) <= len(OPCIONES):
            _, accion = OPCIONES[int(opcion) - 1]
            accion()
        else:
            print("Opción no válida.")