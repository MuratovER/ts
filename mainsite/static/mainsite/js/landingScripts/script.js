'use strict'

const   slides = document.querySelectorAll('.header--slider--item'),
        sliderBtns = document.querySelector('.header--slider--btns');

    let currentSlide = 0,
        interval;

    const prevSlide = (elem, index, strClass) => {
        elem[index].classList.remove(strClass);
    }
    const nextSlide = (elem, index, strClass) => {
        elem[index].classList.add(strClass);
    }

    const changeActive = () => {
        prevSlide(slides, currentSlide, 'header--slider--item-active'); 
        currentSlide++;
        if (currentSlide >= slides.length) currentSlide = 0;
        nextSlide(slides, currentSlide, 'header--slider--item-active');
    }

    const startSlide = (time = 3000) => {
        interval = setInterval(changeActive, time);
    }

    
    sliderBtns.addEventListener('click', (event) => {
        event.preventDefault();
        
        let target = event.target;

       
        if (target.matches('.header--slider--btn')) {
            parent = target;
        } else {
            parent = target.parentNode;
        }
        
        if (parent.matches(".header--slider--prev")) {
            prevSlide(slides, currentSlide, 'header--slider--item-active');
            currentSlide--;

            if (currentSlide < 0) currentSlide = slides.length - 1;

            nextSlide(slides, currentSlide, 'header--slider--item-active');
        } else if (parent.matches('.header--slider--next')) {
            
            prevSlide(slides, currentSlide, 'header--slider--item-active');
            currentSlide++;

            if (currentSlide >= slides.length) currentSlide = 0;

            nextSlide(slides, currentSlide, 'header--slider--item-active');
        } 
    })

    sliderBtns.addEventListener('mouseover', (event) => {
        let target = event.target;
        let parent = target.parentNode;

        if(parent.matches('.header--slider--btn')) {
            stopSlider();
        }
    });
    sliderBtns.addEventListener('mouseout', (event) => {
        let target = event.target;
        let parent = target.parentNode;

        if(parent.matches('.header--slider--btn')) {
            startSlide(3000);
        }
    });

    const stopSlider = () =>  {
        clearInterval(interval);
    };
    
    startSlide(3000);

    