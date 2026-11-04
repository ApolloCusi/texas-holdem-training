from src.juego import jugar_partida


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
        "2": proximamente,
        "3": proximamente,
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