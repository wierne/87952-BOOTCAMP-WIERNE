from flask import Flask, jsonify, request

from models.persona import Persona
from services.persona_service import PersonaService


app = Flask(__name__)

# Un solo servicio para toda la app, asi las personas que agregas
# con el POST siguen estando cuando haces el GET
servicio = PersonaService()


def persona_a_dict(persona):
    return {"dni": persona.dni, "nombre": persona.nombre}


@app.get("/personas")
def obtener_personas():
    personas = servicio.obtener_personas()
    return jsonify([persona_a_dict(p) for p in personas])


@app.get("/personas/<int:dni>")
def obtener_persona(dni):
    persona = servicio.obtener_persona_por_dni(dni)

    if persona is None:
        return jsonify({"error": "Persona no encontrada"}), 404

    return jsonify(persona_a_dict(persona))


@app.post("/personas")
def agregar_persona():
    datos = request.get_json()

    # Si el nombre o el DNI no cumplen las reglas -> 400
    try:
        persona = Persona(datos["dni"], datos["nombre"])
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    # Si el DNI ya existe -> 409
    try:
        servicio.agregar_persona(persona)
    except ValueError as error:
        return jsonify({"error": str(error)}), 409

    return jsonify(persona_a_dict(persona)), 201


if __name__ == "__main__":
    app.run(debug=True)
