var scrollTexts = document.querySelectorAll('.faq_text');

scrollTexts.forEach((scrollText) => {
    scrollText.addEventListener('click', () => {
        const hiddenText = scrollText.nextElementSibling.nextElementSibling; // Récupérer le texte caché
        if (hiddenText.style.display == 'none' || hiddenText.style.display == '') {
            hiddenText.style.display = 'block'; // Afficher le texte déroulant
        } else {
            hiddenText.style.display = 'none'; // Masquer le texte déroulant
        }
    });
});