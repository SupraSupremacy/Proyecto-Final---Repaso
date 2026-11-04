const dataUrl = window.location.pathname.endsWith('.html') ? 'modules.json' : '/modules.json';

const input = document.getElementById('searchInput');
const results = document.getElementById('searchResults');
const filterModule = document.getElementById('filterModule');
const filterTool = document.getElementById('filterTool');

let modules = [];

function norm(value) {
    return (value || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function escapeHtml(value) {
    return String(value || '')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

function textOf(value) {
    return Array.isArray(value) ? value.join(', ') : (value || '');
}

function snippet(module, query) {
    const q = norm(query);
    if (!q) {
        return module.duracion ? 'Duración: ' + module.duracion : (module.nombre || '');
    }
    const fields = [
        ['Competencia', module.competencia],
        ['Objetivos', module.objetivos],
        ['Situación', module.situacion],
        ['Herramientas', textOf(module.herramientas)],
        ['Definiciones', textOf(module.definiciones)],
        ['Aprendimos', textOf(module.aprendizajes)],
        ['Profundidad', textOf(module.profundidades)],
        ['Módulo', module.nombre]
    ];
    for (const [label, value] of fields) {
        const text = textOf(value);
        if (norm(text).includes(q)) {
            return label + ': ' + text.slice(0, 140);
        }
    }
    return module.nombre || '';
}

function filteredModules() {
    const query = norm(input.value.trim());
    const selectedModule = filterModule.value;
    const selectedTool = filterTool.value;

    return modules.filter((module) => {
        if (selectedModule && module.slug !== selectedModule) {
            return false;
        }
        if (selectedTool && !(module.herramientas || []).includes(selectedTool)) {
            return false;
        }
        if (!query) {
            return true;
        }
        const haystack = norm([
            module.title,
            module.nombre,
            module.competencia,
            module.objetivos,
            module.situacion,
            textOf(module.herramientas),
            textOf(module.definiciones),
            textOf(module.aprendizajes),
            textOf(module.profundidades)
        ].join(' '));
        return haystack.includes(query);
    });
}

function renderResults() {
    const list = filteredModules();
    if (!list.length) {
        results.innerHTML = '<div class="sr-empty">Sin resultados</div>';
        results.hidden = false;
        return;
    }
    results.innerHTML = list.map((module) => {
        return '<a class="sr-item" href="' + module.url + '">' +
            '<span class="sr-title">' + escapeHtml(module.title) + '</span>' +
            '<span class="sr-name">' + escapeHtml(module.nombre) + '</span>' +
            '<span class="sr-snippet">' + escapeHtml(snippet(module, input.value)) + '</span>' +
            '</a>';
    }).join('');
    results.hidden = false;
}

function populateFilters() {
    modules.forEach((module) => {
        const option = document.createElement('option');
        option.value = module.slug;
        option.textContent = module.title + ' - ' + module.nombre;
        filterModule.appendChild(option);
    });

    const tools = [...new Set(modules.flatMap((module) => module.herramientas || []))].sort();
    tools.forEach((tool) => {
        const option = document.createElement('option');
        option.value = tool;
        option.textContent = tool;
        filterTool.appendChild(option);
    });
}

if (input && results && filterModule && filterTool) {
    input.addEventListener('input', renderResults);
    filterModule.addEventListener('change', renderResults);
    filterTool.addEventListener('change', renderResults);
    input.addEventListener('focus', renderResults);
    document.addEventListener('click', (event) => {
        if (!event.target.closest('.search-wrap')) {
            results.hidden = true;
        }
    });

    fetch(dataUrl)
        .then((response) => response.json())
        .then((data) => {
            modules = data;
            populateFilters();
            results.hidden = true;
        })
        .catch(() => {
            results.innerHTML = '<div class="sr-empty">No se pudieron cargar los datos</div>';
            results.hidden = false;
        });
}
