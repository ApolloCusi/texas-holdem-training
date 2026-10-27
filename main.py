from src.juego import crear_jugador, jugar_mano, ANTE

def main():
    jugadores = [crear_jugador("Tú"), crear_jugador("Daniel Negreanu"), crear_jugador("Phil Ivey")]

    while True:
        jugar_mano(jugadores)

        print("\nFichas:", ", ".join(f"{j['nombre']}: {j['fichas']}" for j in jugadores))

        if jugadores[0]["fichas"] < ANTE:
            print("Te quedaste sin stack. PLAYER OUT")
            break

        jugadores = [jugadores[0]] + [b for b in jugadores[1:] if b["fichas"] >= ANTE]
        if len(jugadores) == 1:
            print("¡Eliminaste a todos los bots! Ganaste.")
            break

        if input("\n¿Otra mano? [S/N]: ").strip().lower() != "s":
            break


if __name__ == "__main__":
    main()