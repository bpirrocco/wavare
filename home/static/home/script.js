// let nazare = document.querySelector('#Nazaré');
// let nazButton = document.querySelector('#Nazarébutton');


// nazButton.addEventListener("click", function() {
//     nazare = nazare.value;
//     window.location.href = `1/2023-02-10/${nazare}`
// })

// let locationId, interval;

// locationId = nazButton.parentNode.id;
if (window.location.pathname == '/forecast/') {

    let card = document.getElementById("Nazarécard");
    card.addEventListener("mouseover", function(e) {
        addClass(e, card);
    })
    card.addEventListener("mouseleave", function(e) {
        removeClass(e, card);
    })
    function addClass(e, card) {
        card.classList.add("locationimg");
    }
    function removeClass(e, card) {
        card.classList.remove("locationimg")
        // card.classList.replace("locationimg", "locationoff");
    }


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

    for (var i = 0; i <= buttonCount; i += 1) {
        buttons[i].onclick = function(e) {
            let locationId, interval;
            locationId = this.parentNode.id;
            interval = this.previousElementSibling.value;
            window.location.href = `${locationId}/2023-02-10/${interval}`;
        }
    }

   

    
    

    // function addBackgroundImage() {
    //     let i;
    //     let card = document.querySelectorAll("locationcard");
    //     for (i = 0; i <= card.length; i++) {
    //         card[i].addEventListener("onmouseover", function() {
    //             this.classList.add("locationimg");
    //         })
    //     }
    // }
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
if (window.location.pathname == '/about/') {
    let slideIndex1 = 0;
    let slideIndex2 = 0;
    let slides2 = document.getElementsByClassName("myslide2");
    let j;
    for (j = 1; j <slides2.length; j++) {
        slides2[j].style.display = "none";
    }
    showSlides();
    window.onload = function() {
        setTimeout(showSlides2, 4000);
    }

    function showSlides() {
    let i;
    let slides = document.getElementsByClassName("myslide");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex1++;
    if (slideIndex1 > slides.length) {slideIndex1 = 1} 
    slides[slideIndex1-1].style.display = "block";  
    setTimeout(showSlides, 8000); // Change image every 2 seconds
    }

    function showSlides2() {
        let i;
        let slides = document.getElementsByClassName("myslide2");
        slides[0].classList.replace("invisible", "fade3");
        // slides[0].classList.add("fade3");
        for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
        }
        slideIndex2++;
        if (slideIndex2 > slides.length) {slideIndex2 = 1} 
        slides[slideIndex2-1].style.display = "block";  
        setTimeout(showSlides2, 8000); // Change image every 2 seconds
    }
}



// TODO:

// Once you've completed that. Attempt to use JavaScript to
// create the originally intended effect on the location cards