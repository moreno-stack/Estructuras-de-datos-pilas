from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from lista_doble import DoublyLinkedList

bp = Blueprint("turnos", __name__)
turnos = DoublyLinkedList()
salidas = []

TURNOS_INICIALES = [
    ("Urgencias", 1),
    ("Consulta general", 3),
    ("Pruebas de laboratorio", 4),
    ("Entrega de recetas", 5),
]

for nombre, prioridad in TURNOS_INICIALES:
    turnos.add_priority(nombre, prioridad)


def build_summary():
    lista = turnos.to_list()
    ultima_salida = salidas[-1] if salidas else None
    return {
        "total_pendientes": len(lista),
        "total_atendidos": len(salidas),
        "turno_proximo": lista[0]["nombre"] if lista else "No hay turnos",
        "ultima_salida": ultima_salida,
        "turno_mayor_prioridad": lista[0]["prioridad"] if lista else "N/A",
    }


@bp.route("/")
def index():
    return render_template("index.html", turnos=turnos.to_list(), summary=build_summary(), salidas=salidas)


@bp.route("/add", methods=["POST"])
def add_turno():
    nombre = request.form.get("nombre", "").strip()
    prioridad = request.form.get("prioridad", "0").strip()
    if nombre and prioridad.isdigit():
        turnos.add_priority(nombre, int(prioridad))
    return redirect(url_for("turnos.index"))


@bp.route("/remove/<nombre>")
def remove_turno(nombre):
    turnos.remove(nombre)
    return redirect(url_for("turnos.index"))


@bp.route("/move/<nombre>/<direction>")
def move_turno(nombre, direction):
    if direction in ("up", "down"):
        turnos.move(nombre, direction)
    return redirect(url_for("turnos.index"))


@bp.route("/update", methods=["POST"])
def update_turno():
    nombre = request.form.get("nombre", "").strip()
    prioridad = request.form.get("prioridad", "0").strip()
    if nombre and prioridad.isdigit():
        turnos.update_prio(nombre, int(prioridad))
    return redirect(url_for("turnos.index"))


@bp.route("/checkout", methods=["POST"])
def checkout_turno():
    nombre = request.form.get("salida_nombre", "").strip()
    motivo = request.form.get("motivo", "").strip()
    if nombre:
        node = turnos.find(nombre)
        if node and turnos.remove(nombre):
            salidas.append({
                "nombre": node.nombre,
                "prioridad": node.prioridad,
                "hora": datetime.now().strftime("%H:%M:%S"),
                "motivo": motivo if motivo else "No especificado",
            })
    return redirect(url_for("turnos.index"))
