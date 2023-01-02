function myFunction(imgs) {
    var expandImg = document.getElementById("expandedImg");
    var imgText = document.getElementById("imgtext");
    expandImg.src = imgs.src;
    imgText.innerHTML = imgs.alt;
    expandImg.parentElement.parentElement.style.display = "flex";
}

window.onload= function(){
    var imgElement = document.querySelector('img[alt="The shaft gate"]')
    imgElement.style.width = "101%";
}
