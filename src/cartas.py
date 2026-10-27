import random

PALOS = ("♠", "♥", "♦", "♣")
VALORES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
}

def crear_baraja():
    """Devuelve una lista de 52 cartas. Cada carta es una tupla (valor, palo)."""
    return[(valor, palo) for palo in PALOS for valor in VALORES]

def barajar(baraja):
    random.shuffle(baraja)
    return baraja

def repartir(baraja, cantidad):
    """Saca `cantidad` cartas del final de la baraja."""
    return [baraja.pop() for _ in range(cantidad)]

def mostrar_carta(carta):
    valor, palo = carta
    return f"{valor}{palo}"

def mostrar_cartas(cartas):
    return " ".join(mostrar_carta(c) for c in cartas)