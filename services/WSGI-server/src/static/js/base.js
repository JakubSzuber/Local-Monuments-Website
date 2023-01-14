// This file is responsible for handling the transparent header effect and toggle menu functionality on the website.
// When the user scrolls more than 50px on the website, the header gets a transparent effect.
// Also when the user clicks on the toggle button the menu appears and the body, footer and toggle button get the active class.


var element = document.getElementById("header-menu")

// Add an event listener to the document that listens for a scroll event (so the navigation bar will be on the same place)
document.addEventListener('scroll', (e) => {
    if (document.documentElement.scrollTop > 50) {
        element.classList.add("transparent");
    } else {
        element.classList.remove("transparent");
    }
})

// Get the body, toggle, footer and menu element
const body = document.querySelector('body');
const toggle = document.getElementById('toggle');
const footer = document.querySelector('footer');
const menu = document.getElementById('menu');

// Add a click event listener to the toggle button (turn website into light mode)
toggle.onclick=function(){
    toggle.classList.toggle('active');
    body.classList.toggle('active');
    footer.classList.toggle('active');
    menu.classList.toggle('active');
}
