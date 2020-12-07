$(document).ready(function(){
    let CountUpFlag = 0;
    //let $width = $(window).width();
    $('.menu-button').on('click', function(){
       
       $('.menu-button').toggleClass('menu-button-close');
        $('.header-menu').toggleClass('header-menu-show');
        $("html,body").toggleClass("scrollNone");
    });
    $(window).on('load scroll', function() { 
        if ($(this).scrollTop() >= '47' && CountUpFlag == 0) {
            $('.header-nav').toggleClass('header-nav-fixed').css('margin-top', '0px');
            $('.header-menu').css('top', '8%');
            $('.header-menu-txt').css('bottom', '10%')
            CountUpFlag = 1;
        } else if ($(this).scrollTop() <= '47' && CountUpFlag == 1)  {
            $('.header-nav').css('margin-top', '10%')
            $('.header-nav').removeClass('header-nav-fixed');
            $('.header-menu-txt').css('bottom', '20%')
            $('.header-menu').css('top', '18%');
            CountUpFlag = 0;
        } else if ($(this).scrollTop() == '0' && CountUpFlag == 0) {
            $('.header-menu').css('top', '20%');
        }
    });
    $(window).on('load resize', function() {
    if ($(window).width() < 315) {
        $('.whatWeDo-txt').css('font-size', '8px');
    };
     if ($(window).width() > 315) {
        $('.whatWeDo-txt').css('font-size', '10px');}
    if ($(window).width() <= 320) {
        $('.header-logo').css('margin-left', '35%');
    }
    if ($(window).width() < 315) {
        $('.carousel').css('height', '270px');
        $('.carousel-item').css('height', '270px');
    }
    if ($(window).width() > 315) {
        $('.carousel').css('height', '389px');
        $('.carousel-item').css('height', '389px');
    }
    });
 });