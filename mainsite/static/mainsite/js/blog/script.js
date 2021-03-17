console.log('Hello1')

Array.from(document.querySelectorAll('.card')).forEach(function (item) {
    item.addEventListener('click', function (event) {
        event.classList.toggle('flip')
    })
})