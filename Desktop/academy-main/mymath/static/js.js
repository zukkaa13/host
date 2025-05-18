const images = [
    "{% static 'images/Screenshot_20250505_225714.png' %}",
    "{% static 'images/Screenshot_20250505_225955.png' %}",
];

let currentIndex = 0;
const imageElement = document.getElementById("dynamic-image");

function changeImage() {
    currentIndex = (currentIndex + 1) % images.length;
    imageElement.src = images[currentIndex];
}

setInterval(changeImage, 3000); 


document.addEventListener('DOMContentLoaded', function () {
    const burgerMenu = document.querySelector('.burger-menu');
    const menuContainer = document.querySelector('.menu-container');

    if (burgerMenu && menuContainer) {
        burgerMenu.addEventListener('click', function () {
            menuContainer.classList.toggle('open');
        });
    }
}); 