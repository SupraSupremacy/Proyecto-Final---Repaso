import os
from flask import Flask, render_template

app = Flask(__name__)

STATIC_BUILD = os.environ.get("STATIC_BUILD") == "1"


@app.template_filter("slugify")
def slugify(value):
    import unicodedata, re
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "tool"


TOOL_INFO = {
    "Visual Studio": "IDE para desarrollar, depurar, compilar y desplegar aplicaciones; incluye diseñador visual, IntelliSense y gestión de proyectos.",
    ".NET Framework 4.8": "Runtime y librerías base de Microsoft para ejecutar aplicaciones Windows y servicios sobre CLR.",
    "Windows Forms": "Framework de interfaz gráfica para aplicaciones de escritorio Windows, basado en controles y eventos.",
    "ADO.NET (System.Data)": "Conjunto de clases para acceder a datos: conexiones, comandos, adaptadores y conjuntos de datos.",
    "MSBuild": "Motor de compilación que procesa archivos de proyecto para compilar, empaquetar y publicar soluciones.",
    "Microsoft Access": "Sistema gestor de bases de datos de escritorio para crear tablas, consultas, formularios e informes.",
    "SQL (MySQL / SQL Server)": "Lenguaje para definir, consultar y administrar bases de datos relacionales (DDL/DML).",
    "Power BI": "Herramienta de inteligencia de negocios para modelar datos y crear dashboards e informes interactivos.",
    "Microsoft Excel": "Hoja de cálculo para análisis, fórmulas, tablas dinámicas, gráficos e intercambio de datos.",
    "HTML / CSS": "Lenguajes de marcado y estilo para estructurar y presentar contenido en páginas web.",
    "Windows Batch (backups)": "Script de comandos para automatizar tareas del sistema operativo, como respaldos y copias.",
    "WPF (XAML)": "Framework de UI para apps de escritorio Windows con diseño declarativo XAML y enlace de datos.",
    "Microsoft Word / PDF": "Herramientas para redactar documentación y exportar a PDF con formato fijo.",
    "Node.js / npm": "Entorno de ejecución de JavaScript y gestor de paquetes para dependencias y scripts de build.",
    "TypeScript": "Superset tipado de JavaScript que se compila a JavaScript para mejorar mantenibilidad y detección de errores.",
    "Vite": "Servidor de desarrollo rápido y empaquetador moderno para aplicaciones web frontend.",
    "Vitest": "Corredor de pruebas unitarias integrado con Vite para validar componentes y lógica.",
    "ESLint": "Analizador estático de código para detectar errores y aplicar reglas de calidad/estilo.",
    "Python": "Lenguaje de propósito general usado para scripting, backends, automatización y procesamiento de datos.",
    "Flask": "Microframework web para Python para crear aplicaciones y APIs HTTP.",
    "Jinja2": "Motor de plantillas para generar HTML dinámico usando variables, filtros y estructuras de control.",
    "Git & GitHub Pages": "Control de versiones y plataforma para publicar sitios estáticos desde un repositorio.",
    "C#": "Lenguaje de programación orientado a objetos del ecosistema .NET.",
}


@app.context_processor
def inject_build_flags():
    return {"static_build": STATIC_BUILD, "tool_info": TOOL_INFO}


MODULOS = {
    "modulo1": {
        "titulo": "Módulo 1",
        "nombre": "Mantenimiento y aseguramiento de la operación del sistema informático",
        "duracion": "8 semanas",
        "herramientas": [
            "Visual Studio",
            "C#",
            ".NET Framework 4.8",
            "Windows Forms",
            "ADO.NET (System.Data)",
            "MSBuild",
        ],
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
        "herramientas": [
            "Microsoft Access",
            "SQL (MySQL / SQL Server)",
            "Power BI",
            "Microsoft Excel",
            "HTML / CSS",
            "Windows Batch (backups)",
        ],
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
        "herramientas": [
            "Visual Studio",
            "C#",
            ".NET Framework 4.8",
            "Windows Forms",
            "WPF (XAML)",
            "HTML / CSS",
            "Microsoft Word / PDF",
        ],
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
    "modulo4": {
        "titulo": "Módulo 3.8",
        "nombre": "Proyecto innovador de desarrollo de software",
        "duracion": "3 Semanas",
        "herramientas": [
            "Node.js / npm",
            "TypeScript",
            "Vite",
            "Vitest",
            "ESLint",
            "Python",
            "Flask",
            "Jinja2",
            "Git & GitHub Pages",
            "HTML / CSS",
        ],
        "objetivos": (
            "Desarrollar las competencias que permitan la creación de aplicaciones de "
            "software orientadas a la producción de información gerencial para la toma de "
            "decisiones acertadas y confiables dentro de una empresa o entidad."
        ),
        "competencia": (
            "Desarrollar aplicaciones de software orientadas a la información general para "
            "la toma de decisiones acertadas y confiables en una empresa o entidad."
        ),
        "situacion": (
            "Ciertas empresas toman decisiones erróneas basadas en información no "
            "confiable debido a la carencia de sistemas de información general, lo cual "
            "provoca altas pérdidas financieras y disminución en oportunidades de negocio "
            "tanto a nivel nacional como internacional."
        ),
    },
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


def module_records():
    out = []
    for slug, m in MODULOS.items():
        out.append({
            "slug": slug,
            "title": m.get("titulo", slug),
            "nombre": m.get("nombre", ""),
            "duracion": m.get("duracion", ""),
            "competencia": m.get("competencia", ""),
            "objetivos": m.get("objetivos", ""),
            "situacion": m.get("situacion", ""),
            "herramientas": m.get("herramientas", []),
            "definiciones": [TOOL_INFO.get(h, "") for h in m.get("herramientas", [])],
            "url": (slug + ".html") if STATIC_BUILD else ("/" + slug),
        })
    return out


@app.route("/modules.json")
def modules_json():
    import json
    return app.response_class(
        json.dumps(module_records(), ensure_ascii=False),
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(debug=True)
