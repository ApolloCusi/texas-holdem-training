from src.juego import jugar_partida
from src.pot_odds import entrenar_pot_odds
from src.rangos import entrenar_rangos
from src.progreso import guardar_sesion, mostrar_progreso


def mostrar_menu():
    print("\n=== TEXAS HOLD'EM TRAINING ===")
    print("1. Jugar partida contra bots")
    print("2. Entrenar pot odds")
    print("3. Entrenar rangos preflop")
    print("4. Ver mi progreso")
    print("0. Salir")

def sesion_pot_odds():
    aciertos, total = entrenar_pot_odds()
    guardar_sesion("pot_odds", aciertos, total)


def sesion_rangos():
    aciertos, total = entrenar_rangos()
    guardar_sesion("rangos_preflop", aciertos, total)


def menu_principal():
    acciones = {
        "1": jugar_partida,
        "2": sesion_pot_odds,
        "3": sesion_rangos,
        "4": mostrar_progreso,
    }
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "0":
            print("¡Hasta la próxima!")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida.")
        else:
            accion()
