import json
from datetime import datetime
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent.parent / "progreso.json"


def cargar_progreso():
    if not ARCHIVO.exists():
        return {}
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def guardar_sesion(modulo, aciertos, total):
    progreso = cargar_progreso()
    sesiones = progreso.setdefault(modulo, [])
    sesiones.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "aciertos": aciertos,
        "total": total,
    })
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(progreso, f, ensure_ascii=False, indent=2)


def resumen_modulo(sesiones):
    aciertos = sum(s["aciertos"] for s in sesiones)
    total = sum(s["total"] for s in sesiones)
    porcentaje = aciertos * 100 / total if total else 0
    return aciertos, total, porcentaje


def mostrar_progreso():
    progreso = cargar_progreso()
    if not progreso:
        print("Aún no tienes sesiones guardadas. ¡Entrena primero!")
        return
    print("\n=== TU PROGRESO ===")
    for modulo, sesiones in progreso.items():
        aciertos, total, porcentaje = resumen_modulo(sesiones)
        print(f"\n{modulo}: {aciertos}/{total} ({porcentaje:.0f}%) en {len(sesiones)} sesiones")
        for s in sesiones[-3:]:
            print(f"  {s['fecha']}  {s['aciertos']}/{s['total']}")