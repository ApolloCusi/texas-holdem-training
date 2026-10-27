from src.cartas import crear_baraja, barajar, repartir, mostrar_cartas
from src.evaluador import mejor_mano, nombre_mano

ANTE = 10
APUESTA = 20
FICHAS_INICIALES = 500

def crear_jugador(nombre):
    return {"nombre": nombre, "fichas": FICHAS_INICIALES, "mano": [], "activo": True}

def cobrar(jugador, cantidad):
    """Quita fichas al jugador (sin pararse de las que tiene) y devuelve lo cobrado."""
    cantidad = min(cantidad, jugador["fichas"])
    jugador["fichas"] -= cantidad
    return cantidad

def activos(jugadores):
    return [j for j in jugadores if j["activo"]]

def pedir_accion():
    while True:
        opcion = input("Tú hablas. [p]asar / [a]postar / [r]etirarte: ").strip().lower()
        if opcion in ("p", "a", "r"):
            return opcion
        print("Opción no válida.")

def bot_iguala(bot, comunitarias):
    """El bot iguala si tiene al menos un par con las cartas que ve."""
    categoria = mejor_mano(bot["mano"] + comunitarias)[0]
    return categoria >= 1

def ronda_apuestas(jugadores, comunitarias):
    """Jugadores [0] es siempre el humano. Devuelve las fichas que se suman al bote."""
    humano = jugadores[0]
    bote_extra = 0
    accion = pedir_accion()

    if accion == "r":
        humano["activo"] = False
        return 0

    if accion == "a":
        bote_extra += cobrar(humano, APUESTA)
        for bot in jugadores[1:]:
            if not bot["activo"]:
                continue
            if bot_iguala(bot, comunitarias):
                bote_extra += cobrar(bot, APUESTA)
            else:
                bot["activo"] = False
                print(f"{bot['nombre']} se retira.")
    return bote_extra

def resolver(jugadores, comunitarias, bote):
    en_juego = activos(jugadores)

    if len(en_juego) == 1:
        ganador = en_juego[0]
        ganador["fichas"] += bote
        print(f"\n{ganador['nombre']} gana {bote} fichas (los demás se retiraron).")
        return

    puntajes = {}
    print("\n--- Showdown ---")
    print(f"Mesa: {mostrar_cartas(comunitarias)}")
    for j in en_juego:
        puntajes[j["nombre"]] = mejor_mano(j["mano"] + comunitarias)
        print(f"{j['nombre']}: {mostrar_cartas(j['mano'])} --> {nombre_mano(puntajes[j['nombre']])}")

    mejor = max(puntajes.values())
    ganadores = [j for j in en_juego if puntajes[j["nombre"]] == mejor]
    premio = bote // len(ganadores)
    for g in ganadores:
        g["fichas"] += premio
    nombres = " y ".join(g["nombre"] for g in ganadores)
    print(f"\n{nombres} gana(n) {premio} fichas.")

def contar_manos(func):
    """Decorador: imprime el número de mano cada vez que se juega una."""
    def wrapper(*args, **kwargs):
        wrapper.total += 1
        print(f"\n===== Mano #{wrapper.total} =====")
        return func(*args, **kwargs)
    wrapper.total = 0
    return wrapper

@contar_manos
def jugar_mano(jugadores):
    baraja = barajar(crear_baraja())
    comunitarias = []
    bote = 0

    for j in jugadores:
        j["activo"] = True
        j["mano"] = repartir(baraja, 2)
        bote += cobrar(j, ANTE)

    humano = jugadores[0]
    print(f"Tu mano: {mostrar_cartas(humano['mano'])}")

    for etapa, cantidad in (("Flop", 3), ("Turn", 1), ("River", 1)):
        comunitarias += repartir(baraja, cantidad)
        print(f"\n{etapa}: {mostrar_cartas(comunitarias)} | Bote: {bote}")
        if humano["activo"]:
            bote += ronda_apuestas(jugadores, comunitarias)
        if len(activos(jugadores)) == 1:
            break

    resolver(jugadores, comunitarias, bote)
