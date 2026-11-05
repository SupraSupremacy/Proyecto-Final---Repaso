(function () {
    var button = document.getElementById('themeToggle');

    function currentTheme() {
        return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
    }

    function applyTheme(theme) {
        if (theme !== 'light' && theme !== 'dark') {
            theme = 'dark';
        }
        document.documentElement.setAttribute('data-theme', theme);
        try {
            localStorage.setItem('theme', theme);
        } catch (e) {}
        updateButton();
    }

    function updateButton() {
        if (!button) {
            return;
        }
        if (currentTheme() === 'light') {
            button.textContent = '🌙';
            button.setAttribute('aria-label', 'Cambiar a modo oscuro');
        } else {
            button.textContent = '☀';
            button.setAttribute('aria-label', 'Cambiar a modo claro');
        }
    }

    if (button) {
        button.addEventListener('click', function () {
            applyTheme(currentTheme() === 'light' ? 'dark' : 'light');
        });
    }

    try {
        var media = window.matchMedia('(prefers-color-scheme: light)');
        media.addEventListener('change', function (event) {
            if (!localStorage.getItem('theme')) {
                applyTheme(event.matches ? 'light' : 'dark');
            }
        });
    } catch (e) {}

    updateButton();
})();
