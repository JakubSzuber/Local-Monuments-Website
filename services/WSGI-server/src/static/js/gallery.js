// This file is responsible for handling the image expand functionality on the website.
// When the user clicks on an image, the full-size version of the image will be displayed in an expanded view
// Also when the window loads it will select an image element with an alt attribute of "The shaft gate" and sets its width to 101%


// Function responsible for expanding the image after clicking on it
function myFunction(imgs) {

    var expandImg = document.getElementById("expandedImg");
    var imgText = document.getElementById("imgtext");

    expandImg.src = imgs.src;
    imgText.innerHTML = imgs.alt;
    expandImg.parentElement.parentElement.style.display = "flex";
}

// Function that after loading the page set the width of the one image element to 101% in order to enforce images to the right position
window.onload= function(){
    var imgElement = document.querySelector('img[alt="The shaft gate"]')
    imgElement.style.width = "101%";
}
