var scrollTexts = document.querySelectorAll('.faq_text');

scrollTexts.forEach((scrollText) => {
    scrollText.addEventListener('click', () => {
        var hiddenText = scrollText.nextElementSibling.nextElementSibling; // Récupérer le texte caché
        var arrow_icon = scrollText.nextElementSibling;

        if (hiddenText.style.display == 'none' || hiddenText.style.display == '') {
            hiddenText.style.display = 'block'; // Afficher le texte déroulant
            arrow_icon.textContent = "↑";
        } else {
            hiddenText.style.display = 'none'; // Masquer le texte déroulant
            arrow_icon.textContent = "↓";
        }
    });
});