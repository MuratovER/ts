'use strict'
const grid = document.querySelector('.profile-grid'),
      gridCol = document.querySelectorAll('.grid-col');
let width = document.documentElement.clientWidth;
if (width <= 1800) {
    grid.insertAdjacentHTML('afterend', 
    `<style>
    .profile-grid {
        width: ${width}px
        position: relative
        margin: 0 auto
        display: -ms-grid
        display: grid
        -ms-grid-columns:  1018px
        grid-template-columns: 1018px
    }
    </style>
    `);
}