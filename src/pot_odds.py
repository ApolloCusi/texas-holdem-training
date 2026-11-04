import random

DRAWS = {
    "Proyecto de color": 9,
    "Escalera abierta": 8,
    "Gutshot (escalera por dentro)": 4,
    "Dos sobrecartas": 6,
    "Color + gutshot": 12,
    "Color + escalera abierta": 15,
}
BOTES = (60, 120, 180, 240)
FRACCIONES = ((1, 3), (1, 2), (2, 3), (1, 1))
TOLERANCIA = 3


def equity_necesaria(bote, apuesta):
    """Equity mínima (en %) para que pagar sea rentable. `bote` es el bote ANTES de la apuesta."""
    return apuesta / (bote + 2 * apuesta) * 100


def equity_por_outs(outs, cartas_por_venir):
    """Regla del 2 y 4."""
    multiplicador = 4 if cartas_por_venir == 2 else 2
    return outs * multiplicador


def generar_pregunta():
    nombre, outs = random.choice(list(DRAWS.items()))
    num, den = random.choice(FRACCIONES)
    bote = random.choice(BOTES)
    return {
        "proyecto": nombre,
        "outs": outs,
        "cartas_por_venir": random.choice((2, 1)),
        "bote": bote,
        "apuesta": bote * num // den,
    }


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Escribe un número entero.")


def pedir_decision():
    while True:
        opcion = input("¿Pagas o foldeas? [p/f]: ").strip().lower()
        if opcion in ("p", "f"):
            return opcion
        print("Opción no válida.")


def hacer_pregunta():
    """Hace una pregunta. Devuelve True si acertaste el estimado y la decisión."""
    p = generar_pregunta()
    calle = "flop (2 cartas por venir)" if p["cartas_por_venir"] == 2 else "turn (1 carta por venir)"
    print(f"\nTienes: {p['proyecto']} ({p['outs']} outs) en el {calle}.")
    print(f"Bote: {p['bote']} | Tu rival apuesta: {p['apuesta']}")

    estimado = pedir_entero("Tu equity aproximada (%): ")
    decision = pedir_decision()

    real = equity_por_outs(p["outs"], p["cartas_por_venir"])
    necesaria = equity_necesaria(p["bote"], p["apuesta"])
    correcta = "p" if real >= necesaria else "f"

    acierto_equity = abs(estimado - real) <= TOLERANCIA
    acierto_decision = decision == correcta

    print(f"Equity por outs: {real}% | Equity necesaria: {necesaria:.1f}%")
    print("✓ Estimado correcto" if acierto_equity else f"✗ Estimado: lo correcto era {real}% (±{TOLERANCIA})")
    print("✓ Decisión correcta" if acierto_decision else f"✗ Decisión: lo correcto era {'pagar' if correcta == 'p' else 'foldear'}")
    return acierto_equity and acierto_decision


def entrenar_pot_odds(rondas=5):
    aciertos = 0
    for numero in range(1, rondas + 1):
        print(f"\n--- Pregunta {numero}/{rondas} ---")
        if hacer_pregunta():
            aciertos += 1
    print(f"\nResultado: {aciertos}/{rondas}")
    return aciertos, rondas