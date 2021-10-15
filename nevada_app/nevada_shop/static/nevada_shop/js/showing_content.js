let findButtoms = document.querySelectorAll('.find_buttom')

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
