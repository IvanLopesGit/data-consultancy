"use strict";
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const menu = document.querySelector('.menu');
    const body = document.querySelector('body');
    // Verifica se os elementos existem antes de adicionar eventos
    if (menuToggle && menu) {
        menuToggle.addEventListener('click', (event) => {
            event.stopPropagation(); // Previne que o clique no menuToggle feche o menu
            menu.classList.toggle('active');
            body.classList.toggle('menu-open');
        });
    }
    document.addEventListener('click', (event) => {
        // Verifica se o clique foi fora do menu e do menuToggle
        if (menu.classList.contains('active') && !menu.contains(event.target) && !menuToggle.contains(event.target)) {
            menu.classList.remove('active');
            body.classList.remove('menu-open');
        }
    });
});
