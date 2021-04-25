'use strict'

const helpBtn = document.querySelectorAll('.profile--help-btn');

    helpBtn.forEach(btn => {
        btn.addEventListener('click', (event) => {

            event.currentTarget.nextElementSibling.classList.toggle('active--help-block');
        })
    })