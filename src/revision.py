from src.cartas import mostrar_cartas
from src.equity import calcular_equity

UMBRAL_APOSTAR = 65
UMBRAL_BLUFF = 35
NOMBRES_ACCION = {"p": "Pasar", "a": "Apostar", "r": "Retirarte"}


def evaluar_decision(accion, equity):
    """Devuelve (veredicto, comentario). Aquí siempre actúas primero, así que pasar es gratis."""
    if accion == "r":
        return "ERROR", "Te retiraste cuando pasar era gratis. Nunca foldees si no enfrentas una apuesta."
    if accion == "p" and equity >= UMBRAL_APOSTAR:
        return "MEJORABLE", f"Con {equity:.0f}% de equity conviene apostar por valor."
    if accion == "a" and equity < UMBRAL_BLUFF:
        return "RIESGO", f"Apostaste con solo {equity:.0f}% de equity: es un bluff. Solo funciona si tus rivales pueden foldear manos mejores."
    return "OK", "Decisión razonable."


def revisar_mano(registro, simulaciones=1000):
    print("\n=== REVISIÓN DE TU MANO ===")
    print("(Equity calculada contra manos al azar. Analizando...)")
    veredictos = []
    for d in registro:
        equity = calcular_equity(d["mano"], d["mesa"], d["rivales"], simulaciones)
        veredicto, comentario = evaluar_decision(d["accion"], equity)
        veredictos.append(veredicto)
        print(f"\n{d['calle']}: {mostrar_cartas(d['mano'])} | Mesa: {mostrar_cartas(d['mesa'])}")
        print(f"  Rivales: {d['rivales']} | Tu equity: {equity:.0f}%")
        print(f"  {NOMBRES_ACCION[d['accion']]} -> {veredicto}: {comentario}")

    buenas = sum(1 for v in veredictos if v == "OK")
    print(f"\nDecisiones sin observaciones: {buenas}/{len(registro)}")