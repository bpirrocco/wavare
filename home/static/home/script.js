// let nazare = document.querySelector('#Nazaré');
// let nazButton = document.querySelector('#Nazarébutton');


// nazButton.addEventListener("click", function() {
//     nazare = nazare.value;
//     window.location.href = `1/2023-02-10/${nazare}`
// })

// let location, interval;

function getInfo(e, location, interval) {
    let button, selector;
    button = e.target;
    selector = button.previousSibling;
    location = selector.parentNode.id;
    interval = selector.value;
    return location, interval;
}

let buttons = document.getElementsByTagName('button');
let buttonCount = buttons.length;
// buttons.addEventListener("onclick", function(e) {
//     getInfo(e, location, interval);
//     window.location.href - `${location}/2023-02-10/${interval}`
// })
for ( )
buttons.addEventListener("click", function() {
    let selector, location, interval;
    selector = buttons.
})

// TODO:
// For each button in buttons, add an eventlistener that
// gets the selector next to that button, gets the location id 
//  from its parent div, and gets the interval from the selector 
// value. Also maybe make a date variable that holds 2/10/23
// for now. Will eventually make it the current date