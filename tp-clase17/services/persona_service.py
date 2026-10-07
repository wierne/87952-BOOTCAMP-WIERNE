from models.persona import Persona
from repositories.persona_repository import PersonaRepository


class PersonaService:
    def __init__(self):
        self.repo = PersonaRepository()

    def agregar_persona(self, persona: Persona):
        # Regla de negocio: el DNI no se puede repetir
        if self.repo.obtener_por_dni(persona.dni) is not None:
            raise ValueError("Ya existe una persona con ese DNI.")
        self.repo.guardar(persona)

    def obtener_personas(self):
        return self.repo.obtener_todas()

    def obtener_persona_por_dni(self, dni: int):
        return self.repo.obtener_por_dni(dni)
