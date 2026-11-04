from src.juego import jugar_partida
from src.pot_odds import entrenar_pot_odds
from src.rangos import entrenar_rangos

def proximamente():
    print("Próximamente...")


def mostrar_menu():
    print("\n=== TEXAS HOLD'EM TRAINING ===")
    print("1. Jugar partida contra bots")
    print("2. Entrenar pot odds")
    print("3. Entrenar rangos preflop")
    print("4. Ver mi progreso")
    print("0. Salir")


def menu_principal():
    acciones = {
        "1": jugar_partida,
        "2": entrenar_pot_odds,
        "3": entrenar_rangos,
        "4": proximamente,
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