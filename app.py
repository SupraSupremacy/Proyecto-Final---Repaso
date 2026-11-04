import os
from flask import Flask, render_template

app = Flask(__name__)

STATIC_BUILD = os.environ.get("STATIC_BUILD") == "1"


@app.context_processor
def inject_build_flags():
    return {"static_build": STATIC_BUILD}


MODULOS = {
    "modulo1": {
        "titulo": "Módulo 1",
        "nombre": "Mantenimiento y aseguramiento de la operación del sistema informático",
        "duracion": "8 semanas",
        "objetivos": (
            "Desarrollar las competencias que permitan definir planes operativos y "
            "contingenciales, utilizando normas ISO, estándares internacionales y buenas "
            "prácticas como las que implementa ITIL v3 y normas ISO, para mantener la "
            "operación y la sostenibilidad de un sistema computacional."
        ),
        "situacion": (
            "Las caídas constantes en los sistemas informáticos no se tienen mitigadas "
            "debido a que no se cuenta con un área que se encargue del mantenimiento y "
            "aseguramiento de la operación. Esto genera atrasos en la cadena productiva, "
            "erogación de recursos de manera innecesaria y una mala imagen de la entidad."
        ),
    },
    "modulo2": {
        "titulo": "Módulo 3.3",
        "nombre": "Administración de Bases de Datos",
        "duracion": "12 semanas",
        "competencia": (
            "Definir procedimientos, esquemas y políticas de seguridad de una base de "
            "datos, supervisando además el desempeño de las aplicaciones que obtienen "
            "recursos de estas."
        ),
        "objetivos": (
            "Desarrollar las competencias que permiten realizar una adecuada gestión de "
            "una base de datos, asegurando la integridad de la información almacenada en ella."
        ),
        "situacion": (
            "Las caídas constantes de la base de datos de un sistema informático se deben a "
            "que no se administra, gestiona y planifica adecuadamente, generando atrasos en "
            "la cadena productiva, malestar en los usuarios internos y externos, erogación de "
            "recursos de manera innecesaria y una mala imagen de la entidad."
        ),
    },
    "modulo3": {
        "titulo": "Módulo 3.4",
        "nombre": "Elaboración de Documentación de Sistemas Informáticos",
        "duracion": "12 semanas",
        "competencia": [
            "Elabora manuales técnicos del sistema, contribuye diccionario de datos, crea manual de usuario, documenta procesos con DFD, usa UML para modelación.",
            "Propone ideas de proyectos software, visualiza oportunidades de negocio, desarrolla habilidades de venta, busca recursos tecnológicos.",
            "Proactivo con el cliente, actúa con ética profesional, es autodidacta y curioso, comunica ideas con claridad, trabaja en equipo eficientemente.",
            "Emplea estándares de documentación, usa POO para comprender arquitectura, aplica fundamentos DB, interpreta documentos de diseño, usa símbolos para diagramas de flujo.",
        ],
        "objetivos": (
            "Elaborar documentación de sistemas informáticos, como medio para lograr la "
            "fácil comprensión de sus estructuras, elementos y funcionalidad: y como apoyo "
            "en la capacitación de nuevas contrataciones sobre las herramientas con que la "
            "empresa cuenta."
        ),
        "situacion": (
            "El Mantenimiento de sistemas en muchas empresas demora más de lo esperado "
            "porque no existe la documentación necesaria."
        ),
    },
    "modulo4": {"titulo": "Módulo 3.8", "nombre": "Módulo 4", "duracion": "—", "objetivos": "Contenido pendiente.", "situacion": "Contenido pendiente."},
}


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/<slug>")
def modulo(slug):
    m = MODULOS.get(slug)
    if m is None:
        return render_template("404.html", title="404"), 404
    num = slug.replace("modulo", "")
    titulo = m.get("titulo", "Módulo " + num)
    return render_template("modulo.html", title=titulo, data=m, n=num)


if __name__ == "__main__":
    app.run(debug=True)
