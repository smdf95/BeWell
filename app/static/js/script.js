window.addEventListener('scroll', reveal);

function reveal() {
    var reveals = document.querySelectorAll('.reveal');
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var revealTop = reveals[i].getBoundingClientRect().top;
        var revealPoint = 100;
        if (revealTop < windowHeight - revealPoint) {
            reveals[i].classList.add('active');
        } else {
            reveals[i].classList.remove('active');
        }
    }
}


document.addEventListener('DOMContentLoaded', () => {
    const mainMenu = document.querySelector('.links');
    const openMenu = document.querySelector('.openMenu');
    const closeMenu = document.querySelector('.closeMenu');


    openMenu.addEventListener('click', show);
    closeMenu.addEventListener('click', close);


    function show() {
        mainMenu.style.left = "0";
    }

    function close() {
        mainMenu.style.left = "-80%";
    }
});










