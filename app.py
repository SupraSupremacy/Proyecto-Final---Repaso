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
    return {
        "static_build": STATIC_BUILD,
        "tool_info": TOOL_INFO,
        "learned_info": TOOL_LEARNED,
        "deep_info": TOOL_DEEP,
    }


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
            "aprendizajes": [TOOL_LEARNED.get(h, "") for h in m.get("herramientas", [])],
            "profundidades": [TOOL_DEEP.get(h, "") for h in m.get("herramientas", [])],
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
TOOL_LEARNED = {
    "Visual Studio": "Crear soluciones, dise�ar formularios, compilar, depurar con breakpoints y administrar referencias.",
    "C#": "Sintaxis, clases, eventos, validaciones, manejo de excepciones y programaci�n orientada a objetos.",
    ".NET Framework 4.8": "Trabajar con ensamblados, namespaces, configuraci�n de proyecto y compilaciones Debug/Release.",
    "Windows Forms": "Usar controles, eventos, estados de interfaz y grillas/listas para capturar y mostrar datos.",
    "ADO.NET (System.Data)": "Conectar, consultar, insertar, actualizar y mostrar datos con DataSet/DataAdapter.",
    "MSBuild": "Compilar desde IDE/CLI, configurar targets y resolver dependencias del proyecto.",
    "Microsoft Access": "Dise�ar tablas, relaciones, consultas, formularios e informes de base de datos.",
    "SQL (MySQL / SQL Server)": "Crear bases y tablas, CRUD, filtros, JOIN, funciones, procedimientos, triggers y transacciones.",
    "Power BI": "Limpiar y modelar datos, crear medidas DAX, relaciones y dashboards interactivos.",
    "Microsoft Excel": "F�rmulas, tablas din�micas, gr�ficos, importaci�n/exportaci�n y an�lisis exploratorio.",
    "HTML / CSS": "Estructurar contenido sem�ntico, estilos, layouts responsive y componentes visuales.",
    "Windows Batch (backups)": "Automatizar respaldos con comandos, copias, scripts y tareas programadas.",
    "WPF / XAML": "Dise�ar interfaces declarativas, data binding, recursos y estilos.",
    "Microsoft Word / PDF": "Documentar sistemas, crear manuales t�cnicos y exportar documentaci�n final a PDF.",
    "Node.js / npm": "Gestionar dependencias, scripts, entorno de desarrollo y build del proyecto frontend.",
    "TypeScript": "Tipar variables/funciones, interfaces, m�dulos y compilar a JavaScript.",
    "Vite": "Desarrollo con HMR, bundling y build optimizado para producci�n.",
    "Vitest": "Escribir y ejecutar pruebas unitarias, casos de borde y resultados esperados.",
    "ESLint": "Aplicar reglas de calidad, corregir estilo y detectar errores antes de ejecutar.",
    "Python": "Scripting, automatizaci�n, estructuras de datos y backend web.",
    "Flask": "Crear rutas, renderizar plantillas, exponer endpoints y servir una app web.",
    "Jinja2": "Herencia de plantillas, bloques, filtros, variables y generaci�n din�mica de HTML.",
    "Git & GitHub Pages": "Control de versiones, commits, push, branches y despliegue est�tico.",
}

TOOL_DEEP = {
    "Visual Studio": "Visual Studio organiza el proyecto en soluci�n, proyecto, formularios y c�digo. Se aprende a validar entradas, separar l�gica por eventos y depurar paso a paso para encontrar estados incorrectos. En la pr�ctica, esto ayud� a construir interfaces WinForms con DataGridView y botones, evitando duplicar l�gica y detectando valores nulos antes de guardar. Tambi�n se us� para configurar compilaci�n en Debug/Release y revisar referencias externas.",
    "C#": "C# permiti� modelar clases y m�todos para el aplicativo, encapsular datos y responder a eventos de la interfaz. Se practic� validaci�n, conversi�n de tipos, recorridos de colecciones y manejo de excepciones. La curva incluy� pasar de scripts simples a un proyecto con m�ltiples archivos, manteniendo responsabilidades separadas y usando m�todos reutilizables para c�lculos.",
    ".NET Framework 4.8": "Se comprendi� el rol del CLR, los ensamblados y la configuraci�n App.config al compilar un proyecto WinForms. El trabajo con assemblies y referencias ayud� a resolver errores de compilaci�n y a entender dependencias. Tambi�n se vio c�mo el mismo c�digo puede ejecutarse en modo Debug para inspecci�n y Release para entrega final.",
    "Windows Forms": "WinForms se us� para dise�ar formularios con botones, ComboBox, ListView y DataGridView. Se aprendi� a actualizar la interfaz desde eventos, mantener sincronizados datos de memoria y controles visuales, y a calcular totales en tiempo real. La pr�ctica incluy� validar Campos obligatorios y limpiar controles despu�s de cada operaci�n.",
    "ADO.NET (System.Data)": "Se usaron conexiones, comandos y DataAdapter para mover datos entre SQL/Access y la interfaz. La curva pas� de consultar tablas a mostrar resultados en DataGridView/ComboBox y de insertar o actualizar registros con validaci�n. Tambi�n se entendi� la importancia de cerrar conexiones y manejar errores de proveedor de datos.",
    "MSBuild": "MSBuild se us� indirectamente desde el IDE para compilar el .csproj. Se aprendi� que un proyecto define propiedades, referencias e inclusiones de archivos, y que los cambios de estructura afectan la compilaci�n. La pr�ctica incluy� verificar errores en Console/output y entender salidas bin/Debug.",
    "Microsoft Access": "Access se us� para crear tablas, relaciones y consultas en bases desktop. Se aprendi� a modelar entidades, definir claves y relaciones, y a construir formularios e informes para usuarios finales. La curva incluy� migrar o comparar base antes/despu�s del dise�o.",
    "SQL (MySQL / SQL Server)": "Los scripts cubrieron DDL, DML, filtros, joins, funciones, procedimientos, triggers y transacciones. Se aprendi� a crear base desde cero, cargar datos, consultar con operadores requeridos y mantener integridad con ALTER/UPDATE/DELETE. La pr�ctica tambi�n incluy� backups, restores y consultas orientadas a dashboard.",
    "Power BI": "Power BI se us� para importar datos, transformar columnas, crear relaciones y medidas DAX, y visualizar KPIs en dashboards. Se aprendi� a distinguir modelo de informe, usar slicers/filtros y validar cifras contra las consultas SQL. La curva incluy� comparar datos limpios con datos crudos.",
    "Microsoft Excel": "Excel se us� para exportar/importar tablas, preparar CSV, f�rmulas y tablas din�micas. Se aprendi� a limpiar datos antes de an�lisis y a documentar resultados en hojas por caso de negocio. La pr�ctica incluy� cruces y res�menes r�pidos.",
    "HTML / CSS": "Se usaron HTML sem�ntico y CSS para estructurar p�ginas, estilos, navegaci�n, cards y layouts responsive. En la pr�ctica se aplicaron grids, sticky header, animaciones CSS y componentes reutilizables para p�ginas de trabajo e informes.",
    "Windows Batch (backups)": "Se crearon scripts .bat para automatizar copias/backups y ejecutar comandos SQL. Se aprendi� a registrar pasos, validar rutas y probar restauraci�n. La pr�ctica incluy� backups full/diff/log y comparaci�n de resultados.",
    "WPF / XAML": "WPF se us� con XAML para definir UI declarativa y eventos con code-behind. Se practic� layout, recursos, estilos y enlace de datos. La curva incluy� pasar de WinForms a XAML y sincronizar estado visual con variables.",
    "Microsoft Word / PDF": "Se us� para documentar sistemas, crear manuales de usuario y generar PDFs para entrega. Se aprendi� a estructurar secciones, capturas, glosarios y versiones finales. La pr�ctica reforz� claridad y formato consistente.",
    "Node.js / npm": "Se instal� dependencias, ejecut� scripts dev/build/test y entendi� package.json. Se aprendi� a diferenciar dependencias de desarrollo, versiones y.lock. La pr�ctica incluy� ejecutar Vite y Vitest desde terminal.",
    "TypeScript": "Se practic� tipado de funciones, interfaces, m�dulos y DOM. Se aprendi� a detectar errores en compile-time y a estructurar c�digo en archivos separados. La pr�ctica incluy� estado de juego tipado y funciones puras.",
    "Vite": "Vite se us� como servidor de desarrollo con HMR y empaquetador final. Se aprendi� a configurar scripts, entry points y assets, y a optimizar build para publicaci�n. La pr�ctica incluy� debugging de rutas y carga de m�dulos.",
    "Vitest": "Se escribieron pruebas unitarias para l�gica de juego y se interpretaron resultados. Se aprendi� a definir casos m�nimos, verificar c�lculos y reproducir errores antes de corregir. La pr�ctica ayud� a mejorar robustez.",
    "ESLint": "Se configuraron reglas y se corrigieron advertencias/errores de estilo. Se aprendi� a mantener c�digo consistente y detectar patrones problem�ticos temprano. La pr�ctica incluy� ajustar reglas TypeScript.",
    "Python": "Se us� Python para backend, scripts y automatizaci�n de generaci�n est�tica. Se aprendi� a manejar estructuras de datos, rutas, rendering y construcci�n reproducible. La pr�ctica incluy� generaci�n de docs y JSON.",
    "Flask": "Se crearon rutas din�micas, renderizado de plantillas y endpoints JSON. Se aprendi� a separar datos, vistas y archivos est�ticos. La pr�ctica incluy� despliegue est�tico a GitHub Pages.",
    "Jinja2": "Se extendieron templates con herencia, bloques, loops, condicionales y filtros. Se aprendi� a compartir componentes como navbar y a generar rutas relativas/absolutas seg�n entorno.",
    "Git & GitHub Pages": "Se inicializ� repositorio, se hicieron commits y push, se gestion� visibilidad y se public� sitio est�tico. Se aprendi� flujo b�sico y troubleshooting de builds de Pages.",
}

# Insertion marker
TOOL_DEEP_MARKER = True
