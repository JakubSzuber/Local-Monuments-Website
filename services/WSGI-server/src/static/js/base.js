var element = document.getElementById("header-menu")
document.addEventListener('scroll', (e) => {
    if (document.documentElement.scrollTop > 50) {
        element.classList.add("transparent");
    } else {
        element.classList.remove("transparent");
    }
})

const body = document.querySelector('body');
const toggle = document.getElementById('toggle');
const footer = document.querySelector('footer');
const menu = document.getElementById('menu');

toggle.onclick=function(){
    toggle.classList.toggle('active');
    body.classList.toggle('active');
    footer.classList.toggle('active');
    menu.classList.toggle('active');
}
