let nazare = document.querySelector('.nazare')
let nazButton = document.querySelector('.nazbutton')


nazButton.addEventListener("click", function() {
    location.replace(`127.0.0.1:8000/forecast/1/2023-02-10/hourly`)
})
