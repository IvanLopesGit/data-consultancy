function toggleMenu(): void {
    const menu = document.querySelector('.menu') as HTMLElement;
    if (menu) {
        menu.classList.toggle('active');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle') as HTMLElement;
    if (menuToggle) {
        menuToggle.addEventListener('click', toggleMenu);
    }
});