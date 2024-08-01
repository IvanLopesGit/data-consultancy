"use strict";
function toggleMenu() {
    const menu = document.querySelector('.menu');
    if (menu) {
        menu.classList.toggle('active');
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', toggleMenu);
    }
});
