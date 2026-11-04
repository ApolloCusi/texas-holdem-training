import random

from src.cartas import crear_baraja, barajar, repartir, mostrar_cartas

ORDEN = "23456789TJQKA"

# Referencia APROXIMADA (6-max, 100bb, todos foldean hasta ti).
# Reemplázalas por los rangos que tú estudias: solo editas este diccionario.
RANGOS_TEXTO = {
    "UTG": "55+, A9s+, A5s-A3s, KTs+, QTs+, JTs, T9s, 98s, AJo+, KQo",
    "HJ": "33+, A8s+, A5s-A2s, K9s+, Q9s+, J9s+, T9s, 98s, 87s, 76s, ATo+, KJo+, QJo",
    "CO": "22+, A2s+, K7s+, Q9s+, J9s+, T8s+, 97s+, 86s+, 76s, 65s, A9o+, KTo+, QTo+, JTo",
    "BTN": "22+, A2s+, K2s+, Q4s+, J6s+, T6s+, 96s+, 85s+, 75s+, 64s+, 54s, A2o+, K8o+, Q9o+, J9o+, T9o",
}


def _expandir_mas(base):
    """'77+' -> pares desde 77 hasta AA. 'ATs+' -> ATs, AJs, AQs, AKs."""
    c1, c2 = base[0], base[1]
    if c1 == c2:
        return {ORDEN[i] * 2 for i in range(ORDEN.index(c1), len(ORDEN))}
    tipo = base[2]
    return {c1 + ORDEN[i] + tipo for i in range(ORDEN.index(c2), ORDEN.index(c1))}


def _expandir_entre(inicio, fin):
    """'A5s-A2s' -> A5s, A4s, A3s, A2s. '77-55' -> 77, 66, 55."""
    if inicio[0] == inicio[1]:
        a, b = sorted((ORDEN.index(inicio[0]), ORDEN.index(fin[0])))
        return {ORDEN[i] * 2 for i in range(a, b + 1)}
    c1, tipo = inicio[0], inicio[2]
    a, b = sorted((ORDEN.index(inicio[1]), ORDEN.index(fin[1])))
    return {c1 + ORDEN[i] + tipo for i in range(a, b + 1)}


def expandir_rango(texto):
    manos = set()
    for token in (t.strip() for t in texto.split(",")):
        if "-" in token:
            inicio, fin = token.split("-")
            manos |= _expandir_entre(inicio, fin)
        elif token.endswith("+"):
            manos |= _expandir_mas(token[:-1])
        else:
            manos.add(token)
    return manos


RANGOS = {posicion: expandir_rango(texto) for posicion, texto in RANGOS_TEXTO.items()}


def clase_de_mano(carta1, carta2):
    """(('A','♠'), ('K','♠')) -> 'AKs'. Las cartas usan '10', los rangos usan 'T'."""
    v1 = "T" if carta1[0] == "10" else carta1[0]
    v2 = "T" if carta2[0] == "10" else carta2[0]
    if ORDEN.index(v1) < ORDEN.index(v2):
        v1, v2 = v2, v1
    if v1 == v2:
        return v1 + v2
    return v1 + v2 + ("s" if carta1[1] == carta2[1] else "o")


def pedir_accion_preflop():
    while True:
        opcion = input("¿Abres con raise (r) o foldeas (f)? ").strip().lower()
        if opcion in ("r", "f"):
            return opcion
        print("Opción no válida.")


def hacer_pregunta_rango():
    posicion = random.choice(list(RANGOS))
    rango = RANGOS[posicion]
    querer_en_rango = random.random() < 0.5  # mitad de las manos están en el rango

    while True:
        mano = repartir(barajar(crear_baraja()), 2)
        clase = clase_de_mano(*mano)
        if (clase in rango) == querer_en_rango:
            break

    print(f"\nPosición: {posicion} | Todos foldean hasta ti")
    print(f"Tu mano: {mostrar_cartas(mano)} ({clase})")

    respuesta = pedir_accion_preflop()
    correcta = "r" if clase in rango else "f"

    if respuesta == correcta:
        print("✓ Correcto")
        return True
    print(f"✗ Lo correcto era {'abrir con raise' if correcta == 'r' else 'foldear'} en {posicion}")
    return False


def entrenar_rangos(rondas=10):
    aciertos = 0
    for numero in range(1, rondas + 1):
        print(f"\n--- Pregunta {numero}/{rondas} ---")
        if hacer_pregunta_rango():
            aciertos += 1
    print(f"\nResultado: {aciertos}/{rondas}")
    return aciertos, rondas