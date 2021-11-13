let findButtoms = document.querySelectorAll('.find_buttom');

if (findButtoms.length > 0) {
    for (let i = 0; i < findButtoms.length; i++) {
        const buttom = findButtoms[i];
        buttom.addEventListener('click', function () {
            const repertoire = buttom.closest('.repertoire_element').querySelector('.repertoire_content');
            buttom.classList.toggle('find_after');
            repertoire.classList.toggle('invisible');
        });
    }
}

let findFullRiders = document.querySelectorAll('.rider_bottom');

if (findFullRiders.length > 0) {
    for (let i = 0; i < findFullRiders.length; i++) {
        const buttom = findFullRiders[i];
        buttom.addEventListener('click', function () {
            const minRider = buttom.closest('.rider_full_body').querySelector('.text_rider_min');
            const fullRider = buttom.closest('.rider_full_body').querySelector('.text_rider');
            minRider.classList.toggle('invisible');
            fullRider.classList.toggle('invisible');
            if (buttom.innerHTML === 'Развернуть') {
                buttom.innerHTML = 'Свернуть';
            } else {
                buttom.innerHTML = 'Развернуть';
            }
        });
    }
}

let burgerBottom = document.querySelector('.burger_bottom');
let burgerFooter = document.querySelector('.burger_body');
let burgerBody = document.querySelector('.burger_footer');
let nav = document.querySelector('.nav');
let burgerLinks = document.querySelectorAll('.burger_body > a')

function toggleBurger() {
    nav.classList.toggle('burger_open');
    burgerFooter.classList.toggle('invisible');
    burgerBody.classList.toggle('invisible');
    burgerBottom.classList.toggle('burger_close');
    document.body.classList.toggle('lock');
}

if (burgerBottom) {
    burgerBottom.addEventListener('click', function () {
        toggleBurger();
    });
}
if (burgerLinks.length > 0) {
    for (let i = 0; i < burgerLinks.length; i++) {
        let el = burgerLinks[i]
        el.addEventListener('click', function () {
            toggleBurger();
        })
    }
}

// smoothScroll
$(document).ready(function(){
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      // event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        window.location.hash = hash;
      });
    }
  });
});
