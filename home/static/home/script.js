// let nazare = document.querySelector('#Nazaré');
// let nazButton = document.querySelector('#Nazarébutton');


// nazButton.addEventListener("click", function() {
//     nazare = nazare.value;
//     window.location.href = `1/2023-02-10/${nazare}`
// })

// let locationId, interval;

// locationId = nazButton.parentNode.id;

function getInfo(e) {
    let button, selector, locationId, interval;
    button = e.target;
    selector = button.previousSibling;
    locationId = button.parentNode.id;
    interval = selector.value;
    return locationId, interval;
}

let buttons = document.getElementsByTagName('button');
let buttonCount = buttons.length;
// let data;
// nazButton.addEventListener("click", function(e) {
//     data = getInfo(e);
//     alert(data);
// })
// buttons.addEventListener("onclick", function(e) {
//     getInfo(e, location, interval);
//     window.location.href - `${location}/2023-02-10/${interval}`
// })
if (!buttons) {
    for (var i = 0; i <= buttonCount; i += 1) {
        buttons[i].onclick = function(e) {
            let locationId, interval;
            locationId = this.parentNode.id;
            interval = this.previousElementSibling.value;
            window.location.href = `${locationId}/2023-02-10/${interval}`;
        }
    }
}

// function addListener(button) {
//     button.addEventListener("click", function() {
//         let selector, locationId, interval;
//         selector = button.previousSibling;
//         locationId = selector.parentNode.id;
//         interval = selector.value;
//         window.location.href = `${locationId}/2023-02-10/${interval}`;
//     })
// }

// buttons.forEach(addListener)

// let slide = document.getElementById('slide1');
// changeSrc(slide);
// function changeSrc(slide) {
//     alert('Hello')
//     slide.src = "{% static 'home/nazare_lighthouse.jpg' %}";
//     setTimeout(changeSrc, 2000);
// }
// window.onload = function() {
//     alert("hello")
// }

let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("myslide");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1} 
  slides[slideIndex-1].style.display = "block";  
  setTimeout(showSlides, 3000); // Change image every 2 seconds
}


// TODO:
// Create two slideshows on the about.html page
// These slideshows should have some kind of smooth transition
// between images.

// Once you've completed that. Attempt to use JavaScript to
// create the originally intended effect on the location cards