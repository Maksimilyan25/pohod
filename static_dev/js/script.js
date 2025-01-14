document.addEventListener("DOMContentLoaded", function() {
    const textElement = document.querySelector('.overlay-text5');

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function handleScroll() {
        if (isElementInViewport(textElement)) {
            textElement.style.opacity = 1; // Устанавливаем непрозрачность в 1
            textElement.style.transform = 'translateX(0)'; // Возвращаем в конечную позицию
        } else {
            textElement.style.opacity = 0; // Устанавливаем непрозрачность в 0
            textElement.style.transform = 'translateX(-20px)'; // Возвращаем в начальную позицию
        }
    }

    // Добавляем обработчик события прокрутки
    window.addEventListener('scroll', handleScroll);

    // Вызываем handleScroll сразу, чтобы проверить видимость текста при загрузке страницы
    handleScroll();

    function initSecondScript() {
        const textElement2 = document.querySelector('.overlay-text');
        
        function handleScroll2() {
            if (isElementInViewport(textElement2)) {
                textElement2.style.opacity = 1;
                textElement2.style.transform = 'translateY(0)';
            } else {
                textElement2.style.opacity = 0;
                textElement2.style.transform = 'translateY(20px)';
            }
        }

        window.addEventListener('scroll', handleScroll2);
        handleScroll2(); // Проверка видимости при загрузке
    }

    // Инициализация скриптов
    initFirstScript();
    initSecondScript();
});

document.addEventListener("DOMContentLoaded", function() {
    const poemElement = document.getElementById('overlay-textdetail');
    const text = poemElement.innerText;
    const words = text.split(' '); // Разбиваем текст на слова
    let newText = '';
    
    for (let i = 0; i < words.length; i++) {
        newText += words[i] + ' ';
        
        // Проверяем, нужно ли добавить разрыв строки
        if ((i + 1) % 4 === 0) {
            newText += '\n'; // Добавляем перенос строки после каждых 4 слов
        }
    }
    
    poemElement.innerText = newText; // Обновляем текст с переносами
});