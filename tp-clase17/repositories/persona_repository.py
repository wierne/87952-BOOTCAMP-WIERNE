from models.persona import Persona


class PersonaRepository:
    def __init__(self):
        self.personas = []
        self.cargar_datos_prueba()

    def cargar_datos_prueba(self):
        self.personas.append(Persona(30111222, "Juan"))
        self.personas.append(Persona(28333444, "Maria"))
        self.personas.append(Persona(35555666, "Carlos"))

    def guardar(self, persona: Persona):
        self.personas.append(persona)

    def obtener_todas(self):
        return self.personas.copy()

    def obtener_por_dni(self, dni: int):
        for persona in self.personas:
            if persona.dni == dni:
                return persona
        return None
