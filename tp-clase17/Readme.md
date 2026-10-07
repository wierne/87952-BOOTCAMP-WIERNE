# TP Clase 17 - CRUD de Persona (Flask)

## Estructura del proyecto

```
/
├── api.py
├── models/
│   └── persona.py
├── repositories/
│   └── persona_repository.py
└── services/
    └── persona_service.py
```

## Reglas de negocio

- **Modelo (`Persona`)**: el nombre comienza con mayúscula, sigue en minúscula y tiene como máximo 30 caracteres. El DNI es mayor a 0.
- **Servicio (`PersonaService`)**: el DNI no se puede repetir.

## Endpoints

| Método | URL | Descripción |
|---|---|---|
| GET | `/personas` | Lista todas las personas |
| GET | `/personas/<dni>` | Busca una persona por DNI (404 si no existe) |
| POST | `/personas` | Agrega una persona (400 si el nombre es inválido, 409 si el DNI ya existe) |

Body del POST:

```json
{
  "dni": 40123456,
  "nombre": "Lucia"
}
```

## Cómo correrlo

```
pip install flask
python api.py
```

Se prueba con Thunder Client en `http://127.0.0.1:5000`.
