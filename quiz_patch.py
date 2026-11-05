from pathlib import Path

path = Path(r"C:\Users\VirusZ\Desktop\3er Año\Tecno J\Modulo3.8\Final\ProyectoFinal\app.py")
text = path.read_text(encoding="utf-8")

# Helper: insert quiz list before a module's closing brace.
mod1 = [
    {"q": "¿Qué busca ITIL v3 en la operación de TI?", "options": ["Automatizar hardware", "Gestionar servicios con buenas prácticas", "Eliminar todas las incidencias", "Vender software"], "answer": 1},
    {"q": "Un plan de contingencia se activa ante:", "options": ["Tareas rutinarias", "Interrupciones/crisis del servicio", "Compilación correcta", "Actualización de documentación"], "answer": 1},
    {"q": "La gestión de incidentes busca principalmente:", "options": ["Restaurar el servicio lo antes posible", "Cambiar la base de datos", "Reescribir el sistema", "Capacitar usuarios"], "answer": 0},
    {"q": "La disponibilidad se calcula como:", "options": ["tiempo operativo / tiempo total", "tiempo total / tiempo operativo", "incidentes / usuarios", "costos / beneficios"], "answer": 0},
    {"q": "Las caídas constantes generan:", "options": ["solo ahorro de costos", "atrasos, costos y mala imagen", "mayor seguridad", "mejor documentación"], "answer": 1},
]

mod2 = [
    {"q": "En SQL, WHERE se usa para:", "options": ["Crear tablas", "Filtrar filas", "Eliminar base de datos", "Definir claves"], "answer": 1},
    {"q": "La propiedad 'Atomicidad' de ACID significa:", "options": ["La transacción se ejecuta completa o no se ejecuta", "Los datos se leen rápido", "La base se cifra", "Se crean índices"], "answer": 0},
    {"q": "Un backup diferencial contiene cambios desde:", "options": ["El primer backup", "El último backup completo", "El último backup incremental", "La última consulta"], "answer": 1},
    {"q": "En Power BI, DAX se usa para:", "options": ["Diseñar interfaces", "Crear medidas y cálculos", "Compilar código", "Ejecutar backups"], "answer": 1},
    {"q": "La normalización principalmente:", "options": ["Aumenta la redundancia", "Reduce la redundancia", "Elimina índices", "Cifra datos"], "answer": 1},
]

mod3 = [
    {"q": "UML se utiliza para:", "options": ["Escribir código SQL", "Modelar el sistema", "Diseñar hardware", "Crear backups"], "answer": 1},
    {"q": "Un DFD representa:", "options": ["El flujo de datos y procesos", "La interfaz gráfica", "Los colores del sistema", "El presupuesto del proyecto"], "answer": 0},
    {"q": "El diccionario de datos sirve para:", "options": ["Ejecutar el sistema", "Definir estructura y significado de campos", "Probar el software", "Eliminar incidencias"], "answer": 1},
    {"q": "El manual de usuario apoya:", "options": ["La compilación", "La capacitación de nuevas contrataciones", "La creación de índices", "El backup"], "answer": 1},
    {"q": "POO ayuda a comprender:", "options": ["Solo el hardware", "La arquitectura y elementos del sistema", "El diseño gráfico", "La red"], "answer": 1},
]

mod4 = [
    {"q": "Un sistema de información general produce:", "options": ["Solo juegos", "Información gerencial para decisiones", "Backups automáticos", "Código fuente"], "answer": 1},
    {"q": "Decisiones acertadas requieren:", "options": ["Información no confiable", "La carencia de sistemas", "Información confiable y actualizada", "Menos datos"], "answer": 2},
    {"q": "TypeScript aporta principalmente:", "options": ["Triplicar velocidad", "Tipado estático para detectar errores", "Eliminar pruebas", "Cifrar datos"], "answer": 1},
    {"q": "Vite se usa para:", "options": ["Gestionar bases de datos", "Desarrollo con HMR y bundling", "Diseñar hardware", "Crear manuales"], "answer": 1},
    {"q": "Git sirve para:", "options": ["Compilar .NET", "Control de versiones", "Crear dashboards", "Ejecutar pruebas unitarias"], "answer": 1},
]

def quiz_block(items):
    lines = ['        "quiz": [\n']
    for item in items:
        opts = ", ".join('"' + o.replace('"', '\\"') + '"' for o in item["options"])
        lines.append(f'            {{"q": "{item["q"].replace(chr(34), chr(92)+chr(34))}", "options": [{opts}], "answer": {item["answer"]}}},\n')
    lines.append("        ],\n")
    return "".join(lines)

replacements = [
    (
        '        ),\n    },\n    "modulo2": {',
        '        ),\n' + quiz_block(mod1) + '    },\n    "modulo2": {',
    ),
    (
        '        ),\n    },\n    "modulo3": {',
        '        ),\n' + quiz_block(mod2) + '    },\n    "modulo3": {',
    ),
    (
        '        ),\n    },\n    "modulo4": {',
        '        ),\n' + quiz_block(mod3) + '    },\n    "modulo4": {',
    ),
    (
        '        ),\n    },\n}\n\n\n@app.route("/")',
        '        ),\n' + quiz_block(mod4) + '    },\n}\n\n\n@app.route("/")',
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit("marker not found:\n" + old[:120])
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("done")