# Texas Hold'em Training

Entrena Texas Hold'em en la terminal. Juegas contra bots, y el proyecto está creciendo hacia un entrenador completo de póker (pot odds, rangos preflop, equity y progreso).

## Requisitos

- Python 3.8 o superior
- pytest (solo para correr los tests)

## Instalación

```bash
git clone https://github.com/ApolloCusi/texas-holdem-training.git
cd texas-holdem-training
pip install pytest
```

## Cómo jugar

```bash
python main.py
```

Juegas contra 2 bots. En cada mano:

1. Todos ponen un ante fijo de 10 fichas.
2. Se reparten 2 cartas a cada jugador.
3. Se juegan el Flop, el Turn y el River. En cada calle eliges:
   - `p`: pasar
   - `a`: apostar 20 fichas (los bots igualan o se retiran)
   - `r`: retirarte
4. En el showdown gana la mejor mano de 5 cartas entre tus 2 cartas y las 5 de la mesa.

### Reglas simplificadas

Esta versión usa reglas simplificadas a propósito: apuesta fija, sin ciegas y sin rondas de subidas. Los bots igualan si tienen al menos un par con las cartas que ven.

## Cómo funciona por dentro

- La baraja son tuplas `(valor, palo)`.
- El evaluador convierte cada mano de 5 cartas en una tupla comparable, `(categoría, desempates...)`, y con 7 cartas prueba las 21 combinaciones y se queda con la mejor.
- Reconoce la escalera con As bajo (A-2-3-4-5).

## Tests

```bash
python -m pytest -v
```

## Estructura del proyecto

```
texas-holdem-training/
├── main.py              # punto de entrada
├── src/
│   ├── cartas.py        # baraja, repartir, mostrar cartas
│   ├── evaluador.py     # evaluación de manos
│   └── juego.py         # lógica de la partida y los bots
└── tests/
    └── test_evaluador.py
```

## Hoja de ruta

- [x] Juego jugable contra bots
- [x] Evaluador de manos con tests
- [ ] Menú principal
- [ ] Entrenador de pot odds y outs
- [ ] Entrenador de rangos preflop
- [ ] Progreso guardado
- [ ] Calculadora de equity (Monte Carlo)
- [ ] Revisión de manos
- [ ] Simulador de bankroll

## Autor

Apollo ([@ApolloCusi](https://github.com/ApolloCusi))