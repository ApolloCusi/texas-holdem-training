from collections import Counter
from itertools import combinations

from src.cartas import VALORES

NOMBRES = {
    8: "Flor Corrida", 7: "Pókar", 6: "Full House",
    5: "Color", 4: "Corrida", 3: "Tercia",
    2: "Dos pares", 1: "Par", 0: "Carta alta",
}

def evaluar_cinco(cartas):
    """Evalúa exactamente 5 cartas. Devuelve una tupla comparable."""
    valores = sorted((VALORES[v] for v, _ in cartas), reverse=True)
    palos = [p for _, p in cartas]

    es_color = len(set(palos)) == 1

    unicos = sorted(set(valores), reverse=True)
    es_corrida = False
    alta = None
    if len(unicos) == 5:
        if unicos[0] - unicos[4] == 4:
            es_corrida, alta = True, unicos[0]
        elif unicos == [14, 5, 4, 3, 2]: # La corrida A-2-3-4-5
            es_corrida, alta = True, 5

    conteo = Counter(valores)
    grupos = sorted(conteo.items(), key=lambda x: (x[1], x[0]), reverse=True)
    orden = [valor for valor, _ in grupos]
    frecuencias = [veces for _, veces in grupos]

    if es_corrida and es_color:
        return(8, alta)
    if frecuencias == [4, 1]:
        return(7, *orden)
    if frecuencias == [3, 2]:
        return(6, *orden)
    if es_color:
        return(5, *valores)
    if es_corrida:
        return(4, alta)
    if frecuencias == [3, 1, 1]:
        return(3, *orden)
    if frecuencias == [2, 2, 1]:
        return(2, *orden)
    if frecuencias == [2, 1, 1, 1]:
        return (1, *orden)
    return (0, *valores)

def mejor_mano(cartas):
    """Con 5 a 7 cartas, pruebas todas las combinaciones de 5 y devuelve la mejor."""
    return max(evaluar_cinco(c) for c in combinations(cartas, 5))

def nombre_mano(puntaje):
    return NOMBRES[puntaje[0]]
