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
let burgerContain = document.querySelector('.burger_contain');
let nav = document.querySelector('.nav');

if (burgerBottom) {
    burgerBottom.addEventListener('click', function () {
        nav.classList.toggle('burger_open');
        burgerContain.classList.toggle('invisible');
        burgerBottom.classList.toggle('burger_close');
    });
}
