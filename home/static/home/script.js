// let nazare = document.querySelector('#Nazaré');
// let nazButton = document.querySelector('#Nazarébutton');


// nazButton.addEventListener("click", function() {
//     nazare = nazare.value;
//     window.location.href = `1/2023-02-10/${nazare}`
// })

let location, interval;

function getInfo(e) {
    let button, selector;
    button = e.target;
    selector = button.previousSibling;
    location = selector.id;
    interval = selector.value;
}

let buttons = document.querySelector('button');

buttons.addEventListener("click", function(e) {
    getInfo(e);
    window.location.href - `${location}/2023-02-10/${interval}`
})