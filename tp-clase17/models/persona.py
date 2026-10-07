class Persona:
    def __init__(self, dni: int, nombre: str):
        # Regla: el DNI tiene que ser un numero mayor a 0
        if dni <= 0:
            raise ValueError("El DNI debe ser mayor que 0.")

        # Regla: el nombre no puede estar vacio ni tener mas de 30 caracteres
        if len(nombre) == 0 or len(nombre) > 30:
            raise ValueError("El nombre debe tener entre 1 y 30 caracteres.")

        # Regla: solo letras (sin numeros ni espacios)
        if not nombre.isalpha():
            raise ValueError("El nombre solo puede tener letras.")

        # Regla: primera letra mayuscula
        if not nombre[0].isupper():
            raise ValueError("El nombre debe comenzar con mayúscula.")

        # Regla: el resto en minuscula
        if nombre[1:] != nombre[1:].lower():
            raise ValueError("Después de la primera letra, el nombre va en minúscula.")

        self.dni = dni
        self.nombre = nombre
