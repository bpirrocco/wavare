let nazare = document.querySelector('#Nazaré');
let nazButton = document.querySelector('#Nazarébutton');


nazButton.addEventListener("click", function() {
    nazare = nazare.value;
    window.location.href = `1/2023-02-10/${nazare}`
})
