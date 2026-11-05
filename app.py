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
    ordered = globals().get("MODULO_ORDER", list(MODULOS))
    ordered = [s for s in ordered if s in MODULOS]
    return {
        "static_build": STATIC_BUILD,
        "tool_info": TOOL_INFO,
        "learned_info": TOOL_LEARNED,
        "deep_info": TOOL_DEEP,
        "modulos": [{"slug": s, "titulo": MODULOS[s].get("titulo", s)} for s in ordered],
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
        "quiz": [
            {"q": "¿Qué busca ITIL v3 en la operación de TI?", "options": ["Automatizar hardware", "Gestionar servicios con buenas prácticas", "Eliminar todas las incidencias", "Vender software"], "answer": 1},
            {"q": "Un plan de contingencia se activa ante:", "options": ["Tareas rutinarias", "Interrupciones/crisis del servicio", "Compilación correcta", "Actualización de documentación"], "answer": 1},
            {"q": "La gestión de incidentes busca principalmente:", "options": ["Restaurar el servicio lo antes posible", "Cambiar la base de datos", "Reescribir el sistema", "Capacitar usuarios"], "answer": 0},
            {"q": "La disponibilidad se calcula como:", "options": ["tiempo operativo / tiempo total", "tiempo total / tiempo operativo", "incidentes / usuarios", "costos / beneficios"], "answer": 0},
            {"q": "Las caídas constantes generan:", "options": ["solo ahorro de costos", "atrasos, costos y mala imagen", "mayor seguridad", "mejor documentación"], "answer": 1},
        ],
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
        "quiz": [
            {"q": "En SQL, WHERE se usa para:", "options": ["Crear tablas", "Filtrar filas", "Eliminar base de datos", "Definir claves"], "answer": 1},
            {"q": "La propiedad 'Atomicidad' de ACID significa:", "options": ["La transacción se ejecuta completa o no se ejecuta", "Los datos se leen rápido", "La base se cifra", "Se crean índices"], "answer": 0},
            {"q": "Un backup diferencial contiene cambios desde:", "options": ["El primer backup", "El último backup completo", "El último backup incremental", "La última consulta"], "answer": 1},
            {"q": "En Power BI, DAX se usa para:", "options": ["Diseñar interfaces", "Crear medidas y cálculos", "Compilar código", "Ejecutar backups"], "answer": 1},
            {"q": "La normalización principalmente:", "options": ["Aumenta la redundancia", "Reduce la redundancia", "Elimina índices", "Cifra datos"], "answer": 1},
        ],
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
        "quiz": [
            {"q": "UML se utiliza para:", "options": ["Escribir código SQL", "Modelar el sistema", "Diseñar hardware", "Crear backups"], "answer": 1},
            {"q": "Un DFD representa:", "options": ["El flujo de datos y procesos", "La interfaz gráfica", "Los colores del sistema", "El presupuesto del proyecto"], "answer": 0},
            {"q": "El diccionario de datos sirve para:", "options": ["Ejecutar el sistema", "Definir estructura y significado de campos", "Probar el software", "Eliminar incidencias"], "answer": 1},
            {"q": "El manual de usuario apoya:", "options": ["La compilación", "La capacitación de nuevas contrataciones", "La creación de índices", "El backup"], "answer": 1},
            {"q": "POO ayuda a comprender:", "options": ["Solo el hardware", "La arquitectura y elementos del sistema", "El diseño gráfico", "La red"], "answer": 1},
        ],
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
        "quiz": [
            {"q": "Un sistema de información general produce:", "options": ["Solo juegos", "Información gerencial para decisiones", "Backups automáticos", "Código fuente"], "answer": 1},
            {"q": "Decisiones acertadas requieren:", "options": ["Información no confiable", "La carencia de sistemas", "Información confiable y actualizada", "Menos datos"], "answer": 2},
            {"q": "TypeScript aporta principalmente:", "options": ["Triplicar velocidad", "Tipado estático para detectar errores", "Eliminar pruebas", "Cifrar datos"], "answer": 1},
            {"q": "Vite se usa para:", "options": ["Gestionar bases de datos", "Desarrollo con HMR y bundling", "Diseñar hardware", "Crear manuales"], "answer": 1},
            {"q": "Git sirve para:", "options": ["Compilar .NET", "Control de versiones", "Crear dashboards", "Ejecutar pruebas unitarias"], "answer": 1},
        ],
    },
    "modulo31": {
        "titulo": "Módulo 3.1",
        "nombre": "Desarrollo web con ASP.NET y C#",
        "duracion": "8 semanas",
        "herramientas": [
            "Visual Studio",
            "C#",
            "ASP.NET Web Forms",
            ".NET Framework 4.8",
            "HTML / CSS",
            "IIS Express",
        ],
        "quiz": [
            {"q": "En ASP.NET Web Forms, el código del servidor se asocia mediante:", "options": ["Solo HTML", "Eventos y code-behind", "CSS", "SQL directo"], "answer": 1},
            {"q": "Las Cookies se usan para:", "options": ["Guardar datos en el servidor únicamente", "Persistir estado del cliente", "Compilar código", "Crear bases de datos"], "answer": 1},
            {"q": "Session permite:", "options": ["Estado por usuario en el servidor", "Diseño visual", "Respaldos", "Compilación"], "answer": 0},
            {"q": "Un postback envía:", "options": ["Solo imágenes", "Datos del formulario al servidor", "Consultas SQL", "Archivos .exe"], "answer": 1},
            {"q": "La validación del lado servidor:", "options": ["Es opcional siempre", "Aumenta seguridad y confiabilidad", "Elimina la base de datos", "Solo sirve para estilos"], "answer": 1},
        ],
    },
    "modulo35": {
        "titulo": "Módulo 3.5",
        "nombre": "Desarrollo en capas con ASP.NET Core",
        "duracion": "12 semanas",
        "herramientas": [
            "Visual Studio",
            "C#",
            ".NET 10 (ASP.NET Core)",
            "ASP.NET Core MVC / Razor Pages",
            ".NET Framework 4.8",
            "SQL (MySQL / SQL Server)",
            "HTML / CSS",
        ],
        "quiz": [
            {"q": "La arquitectura en capas separa principalmente:", "options": ["Colores de la interfaz", "Presentación, negocio y datos", "Solo backups", "Compilación"], "answer": 1},
            {"q": "Razor Pages facilita:", "options": ["Pruebas unitarias", "Páginas centradas en vistas y handlers", "Backup automático", "Diseño hardware"], "answer": 1},
            {"q": "Una DAL (capa de datos) se encarga de:", "options": ["El diseño visual", "Acceso y operaciones sobre la BD", "Autenticación visual", "Compilación"], "answer": 1},
            {"q": "El patrón CRUD incluye:", "options": ["Solo lectura", "Crear, leer, actualizar y eliminar", "Solo eliminación", "Estilos"], "answer": 1},
            {"q": "Middleware en ASP.NET Core permite:", "options": ["Dibujar ventanas", "Procesar la petición HTTP", "Crear bases Access", "Compilar C#"], "answer": 1},
        ],
    },
    "modulo36": {
        "titulo": "Módulo 3.6",
        "nombre": "Desarrollo multiplataforma con .NET MAUI",
        "duracion": "12 semanas",
        "herramientas": [
            "Visual Studio",
            "C#",
            ".NET 10 (.NET MAUI)",
            "XAML",
            "Android SDK",
            "iOS SDK",
            "Android Emulator",
            "iOS Simulator",
        ],
        "quiz": [
            {"q": "XAML se usa para:", "options": ["Consultas SQL", "Definir interfaces declarativas", "Backups", "Compilar .NET"], "answer": 1},
            {"q": "MAUI permite compartir:", "options": ["Solo código Android", "Código y UI entre plataformas", "Solo estilos web", "Bases de datos Access"], "answer": 1},
            {"q": "Un layout como Grid sirve para:", "options": ["Respaldo de datos", "Organizar controles en filas/columnas", "Compilar código", "Consultar SQL"], "answer": 1},
            {"q": "Para probar en Android normalmente usas:", "options": ["Access", "Emulador o dispositivo", "Excel", "Git"], "answer": 1},
            {"q": "Data binding conecta:", "options": ["Solo botones", "Propiedades de datos con la UI", "Hardware", "Backups"], "answer": 1},
        ],
    },
    "modulo37": {
        "titulo": "Módulo 3.7",
        "nombre": "Programación concurrente y móvil con .NET MAUI",
        "duracion": "12 semanas",
        "herramientas": [
            "Visual Studio",
            "C#",
            ".NET 10 (.NET MAUI)",
            "XAML",
            "async / await",
            "Task Parallel Library (TPL)",
            "Data Binding (MAUI)",
            "Android Emulator",
        ],
        "quiz": [
            {"q": "async/await sirve para:", "options": ["Bloquear la UI", "Ejecutar tareas sin bloquear", "Crear tablas", "Diseñar XAML"], "answer": 1},
            {"q": "Task representa:", "options": ["Un color", "Una operación asíncrona", "Una base de datos", "Un archivo"], "answer": 1},
            {"q": "Data binding en MAUI permite:", "options": ["Solo estilos", "Sincronizar datos y vistas", "Eliminar tareas", "Compilar"], "answer": 1},
            {"q": "Tras un await, la UI suele:", "options": ["Bloquearse siempre", "Continuar cuando la tarea termina", "Cerrar la app", "Perder estado"], "answer": 1},
            {"q": "La concurrencia ayuda a:", "options": ["Más bloqueos", "Mejorar responsividad", "Eliminar validaciones", "Reducir memoria"], "answer": 1},
        ],
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
    "Visual Studio": "Crear soluciones, diseñar formularios, compilar, depurar con breakpoints y administrar referencias.",
    "C#": "Sintaxis, clases, eventos, validaciones, manejo de excepciones y programación orientada a objetos.",
    ".NET Framework 4.8": "Trabajar con ensamblados, namespaces, configuración de proyecto y compilaciones Debug/Release.",
    "Windows Forms": "Usar controles, eventos, estados de interfaz y grillas/listas para capturar y mostrar datos.",
    "ADO.NET (System.Data)": "Conectar, consultar, insertar, actualizar y mostrar datos con DataSet/DataAdapter.",
    "MSBuild": "Compilar desde IDE/CLI, configurar targets y resolver dependencias del proyecto.",
    "Microsoft Access": "Diseñar tablas, relaciones, consultas, formularios e informes de base de datos.",
    "SQL (MySQL / SQL Server)": "Crear bases y tablas, CRUD, filtros, JOIN, funciones, procedimientos, triggers y transacciones.",
    "Power BI": "Limpiar y modelar datos, crear medidas DAX, relaciones y dashboards interactivos.",
    "Microsoft Excel": "Fórmulas, tablas dinámicas, gráficos, importación/exportación y análisis exploratorio.",
    "HTML / CSS": "Estructurar contenido semántico, estilos, layouts responsive y componentes visuales.",
    "Windows Batch (backups)": "Automatizar respaldos con comandos, copias, scripts y tareas programadas.",
    "WPF / XAML": "Diseñar interfaces declarativas, data binding, recursos y estilos.",
    "Microsoft Word / PDF": "Documentar sistemas, crear manuales técnicos y exportar documentación final a PDF.",
    "Node.js / npm": "Gestionar dependencias, scripts, entorno de desarrollo y build del proyecto frontend.",
    "TypeScript": "Tipar variables/funciones, interfaces, módulos y compilar a JavaScript.",
    "Vite": "Desarrollo con HMR, bundling y build optimizado para producción.",
    "Vitest": "Escribir y ejecutar pruebas unitarias, casos de borde y resultados esperados.",
    "ESLint": "Aplicar reglas de calidad, corregir estilo y detectar errores antes de ejecutar.",
    "Python": "Scripting, automatización, estructuras de datos y backend web.",
    "Flask": "Crear rutas, renderizar plantillas, exponer endpoints y servir una app web.",
    "Jinja2": "Herencia de plantillas, bloques, filtros, variables y generación dinámica de HTML.",
    "Git & GitHub Pages": "Control de versiones, commits, push, branches y despliegue estático.",
}

TOOL_DEEP = {
    "Visual Studio": "Visual Studio organiza el proyecto en solución, proyecto, formularios y código. Se aprende a validar entradas, separar lógica por eventos y depurar paso a paso para encontrar estados incorrectos. En la práctica, esto ayudó a construir interfaces WinForms con DataGridView y botones, evitando duplicar lógica y detectando valores nulos antes de guardar. También se usó para configurar compilación en Debug/Release y revisar referencias externas.",
    "C#": "C# permitió modelar clases y métodos para el aplicativo, encapsular datos y responder a eventos de la interfaz. Se practicó validación, conversión de tipos, recorridos de colecciones y manejo de excepciones. La curva incluyó pasar de scripts simples a un proyecto con múltiples archivos, manteniendo responsabilidades separadas y usando métodos reutilizables para cálculos.",
    ".NET Framework 4.8": "Se comprendió el rol del CLR, los ensamblados y la configuración App.config al compilar un proyecto WinForms. El trabajo con assemblies y referencias ayudó a resolver errores de compilación y a entender dependencias. También se vio cómo el mismo código puede ejecutarse en modo Debug para inspección y Release para entrega final.",
    "Windows Forms": "WinForms se usó para diseñar formularios con botones, ComboBox, ListView y DataGridView. Se aprendió a actualizar la interfaz desde eventos, mantener sincronizados datos de memoria y controles visuales, y a calcular totales en tiempo real. La práctica incluyó validar campos obligatorios y limpiar controles después de cada operación.",
    "ADO.NET (System.Data)": "Se usaron conexiones, comandos y DataAdapter para mover datos entre SQL/Access y la interfaz. La curva pasó de consultar tablas a mostrar resultados en DataGridView/ComboBox y de insertar o actualizar registros con validación. También se entendió la importancia de cerrar conexiones y manejar errores de proveedor de datos.",
    "MSBuild": "MSBuild se usó indirectamente desde el IDE para compilar el .csproj. Se aprendió que un proyecto define propiedades, referencias e inclusiones de archivos, y que los cambios de estructura afectan la compilación. La práctica incluyó verificar errores en Console/output y entender salidas bin/Debug.",
    "Microsoft Access": "Access se usó para crear tablas, relaciones y consultas en bases desktop. Se aprendió a modelar entidades, definir claves y relaciones, y a construir formularios e informes para usuarios finales. La curva incluyó migrar o comparar base antes/después del diseño.",
    "SQL (MySQL / SQL Server)": "Los scripts cubrieron DDL, DML, filtros, joins, funciones, procedimientos, triggers y transacciones. Se aprendió a crear base desde cero, cargar datos, consultar con operadores requeridos y mantener integridad con ALTER/UPDATE/DELETE. La práctica también incluyó backups, restores y consultas orientadas a dashboard.",
    "Power BI": "Power BI se usó para importar datos, transformar columnas, crear relaciones y medidas DAX, y visualizar KPIs en dashboards. Se aprendió a distinguir modelo de informe, usar slicers/filtros y validar cifras contra las consultas SQL. La curva incluyó comparar datos limpios con datos crudos.",
    "Microsoft Excel": "Excel se usó para exportar/importar tablas, preparar CSV, fórmulas y tablas dinámicas. Se aprendió a limpiar datos antes de análisis y a documentar resultados en hojas por caso de negocio. La práctica incluyó cruces y resúmenes rápidos.",
    "HTML / CSS": "Se usaron HTML semántico y CSS para estructurar páginas, estilos, navegación, cards y layouts responsive. En la práctica se aplicaron grids, sticky header, animaciones CSS y componentes reutilizables para páginas de trabajo e informes.",
    "Windows Batch (backups)": "Se crearon scripts .bat para automatizar copias/backups y ejecutar comandos SQL. Se aprendió a registrar pasos, validar rutas y probar restauración. La práctica incluyó backups full/diff/log y comparación de resultados.",
    "WPF / XAML": "WPF se usó con XAML para definir UI declarativa y eventos con code-behind. Se practicó layout, recursos, estilos y enlace de datos. La curva incluyó pasar de WinForms a XAML y sincronizar estado visual con variables.",
    "Microsoft Word / PDF": "Se usó para documentar sistemas, crear manuales de usuario y generar PDFs para entrega. Se aprendió a estructurar secciones, capturas, glosarios y versiones finales. La práctica reforzó claridad y formato consistente.",
    "Node.js / npm": "Se instaló dependencias, ejecutó scripts dev/build/test y entendió package.json. Se aprendió a diferenciar dependencias de desarrollo, versiones y lock. La práctica incluyó ejecutar Vite y Vitest desde terminal.",
    "TypeScript": "Se practicó tipado de funciones, interfaces, módulos y DOM. Se aprendió a detectar errores en compile-time y a estructurar código en archivos separados. La práctica incluyó estado de juego tipado y funciones puras.",
    "Vite": "Vite se usó como servidor de desarrollo con HMR y empaquetador final. Se aprendió a configurar scripts, entry points y assets, y a optimizar build para publicación. La práctica incluyó debugging de rutas y carga de módulos.",
    "Vitest": "Se escribieron pruebas unitarias para lógica de juego y se interpretaron resultados. Se aprendió a definir casos mínimos, verificar cálculos y reproducir errores antes de corregir. La práctica ayudó a mejorar robustez.",
    "ESLint": "Se configuraron reglas y se corrigieron advertencias/errores de estilo. Se aprendió a mantener código consistente y detectar patrones problemáticos temprano. La práctica incluyó ajustar reglas TypeScript.",
    "Python": "Se usó Python para backend, scripts y automatización de generación estática. Se aprendió a manejar estructuras de datos, rutas, rendering y construcción reproducible. La práctica incluyó generación de docs y JSON.",
    "Flask": "Se crearon rutas dinámicas, renderizado de plantillas y endpoints JSON. Se aprendió a separar datos, vistas y archivos estáticos. La práctica incluyó despliegue estático a GitHub Pages.",
    "Jinja2": "Se extendieron templates con herencia, bloques, loops, condicionales y filtros. Se aprendió a compartir componentes como navbar y a generar rutas relativas/absolutas según entorno.",
    "Git & GitHub Pages": "Se inicializó repositorio, se hicieron commits y push, se gestionó visibilidad y se publicó sitio estático. Se aprendió flujo básico y troubleshooting de builds de Pages.",
}

MODULO_ORDER = ["modulo31", "modulo1", "modulo2", "modulo3", "modulo35", "modulo36", "modulo37", "modulo4"]

TOOL_INFO.update({
    "ASP.NET Web Forms": "Framework web clásico de .NET basado en controles de servidor, postback y páginas .aspx para construir aplicaciones web.",
    "IIS Express": "Servidor web local para desarrollo y prueba de aplicaciones ASP.NET durante la depuración.",
    ".NET 10 (ASP.NET Core)": "Runtime y framework web moderno para crear APIs, MVC y Razor Pages multiplataforma.",
    "ASP.NET Core MVC / Razor Pages": "Patrones de desarrollo web para estructurar controllers/views o páginas centradas en handlers y UI.",
    ".NET 10 (.NET MAUI)": "Framework multiplataforma para crear apps nativas de Android, iOS, macOS y Windows compartiendo código.",
    "XAML": "Lenguaje de marcado declarativo para definir interfaces, recursos, estilos y data binding.",
    "Android SDK": "Conjunto de herramientas/APIs para compilar y ejecutar aplicaciones Android.",
    "iOS SDK": "Conjunto de herramientas/APIs para compilar y ejecutar aplicaciones iOS.",
    "Android Emulator": "Emulador Android para probar la app sin dispositivo físico durante el desarrollo.",
    "iOS Simulator": "Simulador iOS para probar la app sin dispositivo físico durante el desarrollo.",
    "async / await": "Construcciones de C# para ejecutar tareas asíncronas sin bloquear el hilo de la interfaz.",
    "Task Parallel Library (TPL)": "API de tareas y concurrencia para paralelismo, asincronía y continuaciones en .NET.",
    "Data Binding (MAUI)": "Enlace entre propiedades de datos y la UI para actualizar la vista automáticamente.",
})
TOOL_LEARNED.update({
    "ASP.NET Web Forms": "Trabajar con páginas .aspx, controles de servidor, postback, cookies y sesiones para estado web.",
    "IIS Express": "Levantar y depurar aplicaciones web ASP.NET localmente desde Visual Studio.",
    ".NET 10 (ASP.NET Core)": "Configurar apps modernas, middleware, routing y ejecución en diferentes entornos.",
    "ASP.NET Core MVC / Razor Pages": "Estructurar vistas, controladores/handlers, modelos y flujo de peticiones HTTP.",
    ".NET 10 (.NET MAUI)": "Compartir código y XAML entre plataformas y generar builds Android/iOS/Windows.",
    "XAML": "Diseñar interfaces, layouts, recursos, estilos y enlaces de datos.",
    "Android SDK": "Configurar compilación Android y usar APIs del sistema móvil.",
    "iOS SDK": "Configurar compilación iOS y usar APIs del sistema móvil.",
    "Android Emulator": "Probar comportamiento, layouts y eventos en Android sin dispositivo físico.",
    "iOS Simulator": "Probar comportamiento, layouts y eventos en iOS sin dispositivo físico.",
    "async / await": "Programar operaciones sin bloquear la interfaz y mantener datos de estado seguros.",
    "Task Parallel Library (TPL)": "Crear, encadenar y esperar tareas concurrentes controlando errores.",
    "Data Binding (MAUI)": "Conectar modelos de datos con controles XAML para actualización automática.",
})
TOOL_DEEP.update({
    "ASP.NET Web Forms": "Se practicó la construcción de aplicaciones web con controles de servidor y eventos de postback. Se trabajó con cookies, sesión, arrays y URLs para mantener estado del usuario. La curva incluyó comprender el ciclo de vida de la página y evitar dependencias sólo del lado cliente. También se validó entradas antes de procesarlas.",
    "IIS Express": "IIS Express permitió ejecutar y depurar localmente las páginas .aspx desde Visual Studio. Se aprendió a configurar el sitio, launch profiles y puertos. La práctica incluyó probar requests, postbacks y persistencia de sesión. Sirvió para validar el comportamiento antes de publicar.",
    ".NET 10 (ASP.NET Core)": "Se configuraron proyectos web modernos, middleware, routing y entornos de desarrollo/producción. Se aprendió a separar modelos, vistas y lógica de negocio. La práctica incluyó compilar y ejecutar APIs/controladores. También se validó la configuración por entorno.",
    "ASP.NET Core MVC / Razor Pages": "Se estructuraron vistas, controladores o handlers con modelos y validaciones. Se practicó el flujo petición/respuesta, bindings a formularios y redirecciones. La curva incluyó manejar errores y estados de modelo. También se separó la presentación de la lógica de negocio.",
    ".NET 10 (.NET MAUI)": "Se desarrollaron apps multiplataforma compartiendo XAML y C#. Se aprendió a configurar targets Android/iOS/Windows y resolver diferencias de plataforma. La práctica incluyó layouts, controles, navegación y pruebas en emuladores. También se gestionaron recursos y assets.",
    "XAML": "Se definió la UI de forma declarativa con layouts, recursos, estilos y enlace de datos. Se aprendió la jerarquía de controles y el ciclo de renderizado. La práctica incluyó layouts Grid/Stack/Flex/Absolute y páginas navegables. También se corrigieron problemas de espacio y alineación.",
    "Android SDK": "Se usaron las APIs y herramientas de Android para compilar y ejecutar la app en emulador o dispositivo. Se comprendió configuración de targets, permisos y recursos Android. La práctica incluyó resolver diferencias de plataforma y depurar en Android.",
    "iOS SDK": "Se usaron herramientas y APIs de Apple para compilar y probar en simulador o dispositivo. Se comprendió la configuración de targets iOS y recursos. La práctica incluyó validar comportamiento y layouts en iOS.",
    "Android Emulator": "Se probó la app en un dispositivo virtual Android para validar flujo, layouts y eventos. Se aprendió a lanzar emulador, desplegar y leer logs. La práctica incluyó detectar fallos de UI y ciclo de vida.",
    "iOS Simulator": "Se probó la app en un simulador iOS para validar flujo, layouts y eventos. Se aprendió a lanzar simulador, desplegar y depurar. La práctica incluyó verificar compatibilidad visual.",
    "async / await": "Se implementaron operaciones sin bloquear la interfaz. Se aprendió a propagar await, manejar tareas y mantener estado consistente. La práctica incluyó medir tiempos y mostrar resultados en pantalla.",
    "Task Parallel Library (TPL)": "Se crearon tareas y se coordinó su ejecución con Task.Run, Task.WhenAll y continuaciones. Se aprendió a capturar y mostrar errores. La práctica incluyó sincronizar datos y evitar bloqueos.",
    "Data Binding (MAUI)": "Se enlazaron propiedades de modelos con controles XAML. Se aprendió a usar INotifyPropertyChanged y actualización automática. La práctica incluyó formularios, listas y resultados en tiempo real.",
})
