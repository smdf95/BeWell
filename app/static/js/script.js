window.addEventListener('scroll', reveal);

function reveal() {

    // Makes hidden elements on the page appear when scrolling towards them

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

    // Function for opening and closing the menu on tablets and phones

    const mainMenu = document.querySelector('.links');
    const openMenu = document.querySelector('.openMenu');
    const closeMenu = document.querySelector('.closeMenu');


    openMenu.addEventListener('click', show);
    closeMenu.addEventListener('click', close);


    function show() {
        mainMenu.style.left = "0";
        mainMenu.style.boxShadow = "0 0 200px 100px #000000";
    }

    function close() {
        mainMenu.style.left = "-70%";
        mainMenu.style.boxShadow = "none";

    }
});










