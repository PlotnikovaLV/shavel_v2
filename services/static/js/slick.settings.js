/*
     _ _      _       _
 ___| (_) ___| | __  (_)___
/ __| | |/ __| |/ /  | / __|
\__ \ | | (__|   < _ | \__ \
|___/_|_|\___|_|\_(_)/ |___/
                   |__/

 Version: 1.6.0
  Author: Ken Wheeler
 Website: http://kenwheeler.github.io
    Docs: http://kenwheeler.github.io/slick
    Repo: http://github.com/kenwheeler/slick
  Issues: http://github.com/kenwheeler/slick/issues

 */
/* global window, document, define, jQuery, setInterval, clearInterval */
$(document).on('ready', function() {
           $(".center").slick({
         	dots: true,
         	infinite: true,
         	centerMode: true,
         	slidesToShow: 3,
         	slidesToScroll: 2,
         	responsive: [
         		{
         		  breakpoint: 768,
         		  settings: {
         			arrows: true,
         			centerMode: false,
         			slidesToShow: 3
         		  }
         		},
         		{
         		  breakpoint: 480,
         		  settings: {
         			arrows: true,
         			centerMode: false,
         			centerPadding: '40px',
         			slidesToShow: 1
         		  }
         		}
         	 ]
           });
         });