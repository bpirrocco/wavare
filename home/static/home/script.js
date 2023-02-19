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
for (var i = 0; i <= buttonCount; i += 1) {
    buttons[i].onclick = function(e) {
        let locationId, interval;
        locationId = this.parentNode.id;
        interval = this.previousElementSibling.value;
        window.location.href = `${locationId}/2023-02-10/${interval}`;
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


// TODO:
// For each button in buttons, add an eventlistener that
// gets the selector next to that button, gets the location id 
//  from its parent div, and gets the interval from the selector 
// value. Also maybe make a date variable that holds 2/10/23
// for now. Will eventually make it the current date