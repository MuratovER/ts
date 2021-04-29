'use strict'
const habbitsListBtn = document.querySelectorAll('.habbits--list-title'),
      allHabbitsBtn = document.querySelector('.allHabbitsBtn'),  
      allHabbitsList = document.querySelector('.allHabbitsList'),
      checkHabbitBtn = document.querySelectorAll('.check--habbit'),
      showPasswordBtn = document.querySelectorAll('.show--password');
   
//show habbits group lists
habbitsListBtn.forEach((item) => {
    item.addEventListener('click', () => {
        item.nextElementSibling.classList.toggle('displayNone');
    });
})

//change checked habbit style
checkHabbitBtn.forEach((item) => {
    item.addEventListener('click', () => {
        item.nextElementSibling.classList.toggle('checkedHabbit');
    })
})

//show all habbits
allHabbitsBtn.addEventListener(('click'), () => {
    allHabbitsList.classList.toggle('displayNone');
})

