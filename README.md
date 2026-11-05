# Proyecto Final - Repaso

Aplicación web para repasar los módulos de **Desarrollo de Software** con una interfaz inspirada en el estilo cyberpunk (Cyberpunk: Edgerunners).

## Enlace publicado

https://suprasupremacy.github.io/Proyecto-Final---Repaso/

## Características

- Portada con diseño neon cyberpunk y glitcheos.
- Barra de navegación a todos los módulos (Módulo 1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7 y 3.8).
- Modo claro / oscuro con persistencia en `localStorage`.
- Barra de progreso de scroll de 0% a 100%.
- Buscador global con filtros por módulo y herramienta.
- Tarjeta de herramientas usadas en cada módulo.
- Definiciones, aprendizaje y explicación detallada por herramienta en acordeón.
- Quiz de repaso con puntaje y reinicio.
- Sitio estático desplegado con GitHub Pages.

## Estructura

- `app.py`: aplicación Flask, datos de módulos y generación de JSON para búsqueda.
- `templates/`: plantillas Jinja2 (`base.html`, `index.html`, `modulo.html`, `404.html`).
- `static/`: CSS, JavaScript y recursos.
- `build.py`: renderiza rutas a HTML estático dentro de `docs/`.
- `docs/`: sitio estático servido por GitHub Pages.
- `requirements.txt`: dependencias Python.

## Ejecución local

```bash
cd ProyectoFinal
pip install -r requirements.txt
python app.py
```

Abre `http://127.0.0.1:5000`.

## Build estático

```bash
cd ProyectoFinal
python build.py
```

Esto genera `docs/` (incluyendo `modules.json`, CSS, JS y páginas `modulo*.html`).

## Despliegue en GitHub Pages

En GitHub: Settings → Pages

- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/docs`

## Módulos

| Código | Nombre | Duración |
|---|---|---|
| Módulo 1 | Mantenimiento y aseguramiento de la operación del sistema informático | 8 semanas |
| Módulo 3.1 | Desarrollo web con ASP.NET y C# | 8 semanas |
| Módulo 3.3 | Administración de Bases de Datos | 12 semanas |
| Módulo 3.4 | Elaboración de Documentación de Sistemas Informáticos | 12 semanas |
| Módulo 3.5 | Desarrollo en capas con ASP.NET Core | 12 semanas |
| Módulo 3.6 | Desarrollo multiplataforma con .NET MAUI | 12 semanas |
| Módulo 3.7 | Programación concurrente y móvil con .NET MAUI | 12 semanas |
| Módulo 3.8 | Proyecto innovador de desarrollo de software | 3 semanas |
