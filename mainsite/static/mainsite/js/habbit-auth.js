'use strict'
let showPasswordBtn = document.querySelectorAll('.show--password');

//show disable password
showPasswordBtn.forEach((item) => {
    console.log(item);
    item.addEventListener('click', (event) => {
        event.preventDefault();
        let passwordInput =  event.target.parentElement.previousElementSibling;
       if(passwordInput.getAttribute('type') == 'password') {
        event.target.setAttribute('src', '../../../static/mainsite/images/dist/habbit/icecream.png');
        passwordInput.setAttribute('type', 'text');
       } else {
        passwordInput.setAttribute('type', 'password');
        event.target.setAttribute('src', '../../../static/mainsite/images/dist/habbit/ghost-character.png');
       }
    })
})