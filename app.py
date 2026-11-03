from flask import Flask, render_template

app = Flask(__name__)

MODULOS = {
    "modulo1": {
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
    "modulo3": {"nombre": "Módulo 3", "duracion": "—", "objetivos": "Contenido pendiente.", "situacion": "Contenido pendiente."},
    "modulo4": {"nombre": "Módulo 4", "duracion": "—", "objetivos": "Contenido pendiente.", "situacion": "Contenido pendiente."},
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
    return render_template("modulo.html", title="Módulo " + num, data=m, n=num)


if __name__ == "__main__":
    app.run(debug=True)
