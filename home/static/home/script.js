let nazare = document.querySelector('#nazare');
let nazButton = document.querySelector('#nazbutton');


nazButton.addEventListener("click", function() {
    nazare = nazare.value;
    window.location.href = `1/2023-02-10/${nazare}`
})
