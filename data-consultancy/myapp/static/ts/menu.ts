document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle') as HTMLElement;
    const menu = document.querySelector('.menu') as HTMLElement;
    const body = document.querySelector('body') as HTMLElement;

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
        if (menu.classList.contains('active') && !menu.contains(event.target as Node) && !menuToggle.contains(event.target as Node)) {
            menu.classList.remove('active');
            body.classList.remove('menu-open');
        }
    });
});