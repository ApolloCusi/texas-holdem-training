import random

from src.cartas import crear_baraja, barajar, repartir, mostrar_cartas, parsear_cartas
from src.evaluador import mejor_mano
from src.pot_odds import pedir_entero

TOLERANCIA_EQUITY = 7


def calcular_equity(mano, comunitarias=(), oponentes=1, simulaciones=2000, mano_rival=None):
    """Equity (en %) de `mano` contra `oponentes`.

    - Los oponentes desconocidos reciben cartas al azar.
    - Si das `mano_rival`, ese es uno de los oponentes y su mano es conocida.
    """
    comunitarias = list(comunitarias)
    rival_conocido = list(mano_rival) if mano_rival else []
    conocidas = list(mano) + comunitarias + rival_conocido

    if len(mano) != 2:
        raise ValueError("Tu mano debe tener exactamente 2 cartas.")
    if len(comunitarias) not in (0, 3, 4, 5):
        raise ValueError("La mesa debe tener 0, 3, 4 o 5 cartas.")
    if oponentes < 1:
        raise ValueError("Debe haber al menos 1 oponente.")
    if len(set(conocidas)) != len(conocidas):
        raise ValueError("Hay cartas repetidas.")

    baraja = [c for c in crear_baraja() if c not in conocidas]
    faltan_mesa = 5 - len(comunitarias)
    desconocidos = oponentes - (1 if rival_conocido else 0)
    por_sacar = faltan_mesa + 2 * desconocidos

    puntos = 0.0
    for _ in range(simulaciones):
        cartas = random.sample(baraja, por_sacar)
        mesa = comunitarias + cartas[:faltan_mesa]
        resto = cartas[faltan_mesa:]

        rivales = [rival_conocido] if rival_conocido else []
        rivales += [resto[i:i + 2] for i in range(0, len(resto), 2)]

        mia = mejor_mano(list(mano) + mesa)
        puntajes = [mejor_mano(r + mesa) for r in rivales]
        mejor_rival = max(puntajes)

        if mia > mejor_rival:
            puntos += 1
        elif mia == mejor_rival:
            puntos += 1 / (puntajes.count(mia) + 1)

    return puntos * 100 / simulaciones


def calculadora_equity():
    print("\n=== CALCULADORA DE EQUITY ===")
    print("Cartas: valor + palo (s=♠ h=♥ d=♦ c=♣). Ejemplo: As Kh   |   10d 9d   |   Td 9d")
    try:
        mano = parsear_cartas(input("Tu mano (2 cartas): "))
        mesa = parsear_cartas(input("Mesa (0, 3, 4 o 5 cartas; Enter si no hay): "))
        oponentes = pedir_entero("Número de oponentes (1 a 5): ")
        if not 1 <= oponentes <= 5:
            raise ValueError("Los oponentes deben ser entre 1 y 5.")
        print("Calculando...")
        equity = calcular_equity(mano, mesa, oponentes, simulaciones=3000)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"\nTu equity contra {oponentes} oponente(s) al azar: {equity:.1f}%")


def generar_situacion():
    baraja = barajar(crear_baraja())
    mano = repartir(baraja, 2)
    rival = repartir(baraja, 2)
    mesa = repartir(baraja, random.choice((0, 3, 4)))
    return mano, rival, mesa


def hacer_pregunta_equity():
    mano, rival, mesa = generar_situacion()
    print(f"\nTu mano: {mostrar_cartas(mano)}")
    print(f"Mano del rival: {mostrar_cartas(rival)}")
    print(f"Mesa: {mostrar_cartas(mesa) if mesa else '(preflop, sin cartas en la mesa)'}")

    estimado = pedir_entero("¿Cuál crees que es tu equity (%)? ")
    print("Calculando...")
    real = calcular_equity(mano, mesa, 1, 1500, mano_rival=rival)
    error = abs(estimado - real)

    print(f"Equity real: {real:.1f}% | Tu estimado: {estimado}% | Error: {error:.1f} puntos")
    if error <= TOLERANCIA_EQUITY:
        print("✓ Dentro de tolerancia")
        return True
    print(f"✗ Fuera de tolerancia (±{TOLERANCIA_EQUITY})")
    return False


def entrenar_equity(rondas=5):
    aciertos = 0
    for numero in range(1, rondas + 1):
        print(f"\n--- Pregunta {numero}/{rondas} ---")
        if hacer_pregunta_equity():
            aciertos += 1
    print(f"\nResultado: {aciertos}/{rondas}")
    return aciertos, rondas