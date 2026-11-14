import math
import random


def riesgo_ruina_teorico(winrate, desviacion, bankroll_bb):
    """Riesgo de ruina (en %). winrate y desviacion en bb/100; bankroll en bb."""
    if winrate <= 0:
        return 100.0
    return math.exp(-2 * winrate * bankroll_bb / desviacion ** 2) * 100


def simular_bankroll(winrate, desviacion, buyins, manos=100000, simulaciones=1000, bb_por_buyin=100):
    bloques = manos // 100
    arruinados = 0
    finales = []

    for _ in range(simulaciones):
        bankroll = buyins * bb_por_buyin
        for _ in range(bloques):
            bankroll += random.gauss(winrate, desviacion)
            if bankroll <= 0:
                bankroll = 0
                arruinados += 1
                break
        finales.append(bankroll)

    finales.sort()
    return {
        "riesgo_ruina": arruinados * 100 / simulaciones,
        "peor_5": finales[int(len(finales) * 0.05)],
        "mediana": finales[len(finales) // 2],
        "mejor_5": finales[int(len(finales) * 0.95)],
    }


def pedir_numero(mensaje, defecto=None):
    while True:
        texto = input(mensaje).strip()
        if texto == "" and defecto is not None:
            return defecto
        try:
            return float(texto)
        except ValueError:
            print("Escribe un número (puedes usar decimales).")


def simulador_bankroll():
    print("\n=== SIMULADOR DE BANKROLL ===")
    print("Todo en bb/100 manos. Orientativo en 6-max: desviación entre 80 y 100.")
    winrate = pedir_numero("Tu winrate (bb/100): ")
    desviacion = pedir_numero("Desviación estándar (Enter = 90): ", 90)
    buyins = pedir_numero("Bankroll en buy-ins de 100bb: ")
    manos = int(pedir_numero("Manos a simular (Enter = 100000): ", 100000))

    if desviacion <= 0 or buyins <= 0 or manos < 100:
        print("Datos no válidos: desviación y buy-ins deben ser positivos y manos al menos 100.")
        return

    print("\nRiesgo de ruina teórico según tu bankroll:")
    for b in (10, 20, 30, 50, 100):
        print(f"  {b:>3} buy-ins: {riesgo_ruina_teorico(winrate, desviacion, b * 100):.1f}%")

    print("\nSimulando...")
    r = simular_bankroll(winrate, desviacion, buyins, manos)
    print(f"\nCon {buyins:.0f} buy-ins y {manos} manos:")
    print(f"  Riesgo de ruina simulado: {r['riesgo_ruina']:.1f}%")
    print(f"  Bankroll final (bb): peor 5% = {r['peor_5']:.0f} | mediana = {r['mediana']:.0f} | mejor 5% = {r['mejor_5']:.0f}")
    print("\nModelo simplificado: winrate constante, resultados normales. No contempla subir o bajar de límite.")