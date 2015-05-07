/* jshint devel:true */
$(document.ready).ready(function() {
  'use strict';
  $('.select-sign form').submit(function(event) {
    /*jshint -W020 */
    event.preventDefault();
    var day = $('#day').val();
    var month = $('#month').val();
    var birthcode = month + day;
    var astrology;
    birthcode = Number(birthcode);
    switch (true) {

      case (birthcode <= 120):
        astrology = 'capricorn';
        break;

      case (birthcode <= 218):
        astrology = 'aquarius';
        break;

      case (birthcode <= 320):
        astrology = 'pisces';
        break;

      case (birthcode <= 420):
        astrology = 'aries';
        break;

      case (birthcode <= 521):
        astrology = 'taurus';
        break;

      case (birthcode <= 621):
        astrology = 'gemini';
        break;

      case (birthcode <= 722):
        astrology = 'cancer';
        break;

      case (birthcode <= 823):
        astrology = 'leo';
        break;

      case (birthcode <= 923):
        astrology = 'virgo';
        break;

      case (birthcode <= 1023):
        astrology = 'libra';
        break;

      case (birthcode <= 1122):
        astrology = 'scorpio';
        break;

      case (birthcode <= 1222):
        astrology = 'sagittarius';
        break;

      case (birthcode <= 1231):
        astrology = 'capricorn';
        break;

      default:
        astrology = 'Mystery';
        break;
    }

    // $('.selected_sign').text(astrology).show();
    // $('.select-sign').hide();
    // $('body').removeClass('no-scroll');
    // $('.menu-trigger .zodiac__img--big').show();
    location = '/'+astrology+'';
    return false;
  });

  $('.select-sign input').keydown(function(e) {
    // Allow: backspace, delete, tab, escape, enter and .
    if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
      // Allow: Ctrl+A
      (e.keyCode === 65 && e.ctrlKey === true) ||
      // Allow: Ctrl+C
      (e.keyCode === 67 && e.ctrlKey === true) ||
      // Allow: Ctrl+X
      (e.keyCode === 88 && e.ctrlKey === true) ||
      // Allow: home, end, left, right
      (e.keyCode >= 35 && e.keyCode <= 39)) {
      // let it happen, don't do anything
      return;
    }
    // Ensure that it is a number and stop the keypress
    if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
      e.preventDefault();
    }
  }).keydown(function(e) {
    var charLimit = $(this).attr('maxlength');
    var keys = [8, 9, 13, 19, 20, 27, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 144, 145];

    if (e.which === 8 && this.value.length === 0) {
      $(this).removeClass('filled');
      $(this).closest('.col-4').prev().children('input').focus();
    } else if ($.inArray(e.which, keys) >= 0) {
      return true;
    } else if (this.value.length >= charLimit) {
      $(this).addClass('filled');
      $(this).closest('.col-4').next().children('input').focus();
      return false;
    } else if (e.shiftKey || e.which < 48 || e.which > 57) {
      return false;
    }

    if ($('.select-sign .filled').length === 3) {
      $('.select-sign form').submit();
    }
  }).keyup(function() {
    var charLimit = $(this).attr('maxlength');
    if (this.value.length >= charLimit) {
      $(this).addClass('filled');
      $(this).closest('.col-4').next().children('input').focus();
      return false;
    }
  }).keypress(function(e) {
    if (e.which === 13) {
      console.log('enter');
      e.preventDefault();
      $('.select-sign form').submit();
    }
  });


  $('.zodiac__link').on('click', function() {
    $('.zodiac__link.active').removeClass('active');
    $(this).toggleClass('active');
  });

  $('.carousel__item').on('click', function() {
    $('.carousel__item.active').removeClass('active');
    $(this).toggleClass('active');
  });

  var carousel = $('.carousel');
  carousel.on('initialized.owl.carousel', function(){
    carousel.children('.owl-stage-outer').css('padding-left', 0);
  });
  carousel.owlCarousel({
    stagePadding: 50,
    loop: false,
    margin: 20,
    responsive: {
      0: {
        items: 1
      },
      350: {
        items: 2
      },
      500: {
        items: 3
      },
      600: {
        items: 4
      },
      800: {
        items: 4
      },
      1000: {
        items: 5
      },
      1200: {
        items: 7
      }
    }
  });
});
