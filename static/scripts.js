// Script para cambiar el tema entre oscuro y claro
document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;

    // Guardar el tema seleccionado en localStorage
    if (localStorage.getItem('theme') === 'light') {
        body.classList.add('theme-light');
    } else {
        body.classList.remove('theme-light');
    }

    // Cambiar tema al hacer clic en un botón (no incluido en base.html)
    const themeToggleButton = document.getElementById('theme-toggle');
    if (themeToggleButton) {
        themeToggleButton.addEventListener('click', () => {
            body.classList.toggle('theme-light');
            localStorage.setItem('theme', body.classList.contains('theme-light') ? 'light' : 'dark');
        });
    }
});