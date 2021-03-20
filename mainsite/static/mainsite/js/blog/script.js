// Жирный (b)
$(`body`).on('click', '.toolbar-b', function(){
    document.execCommand('bold', false, null);
    return false;
});

// Курсив (i)
$('body').on('click', '.toolbar-i', function(){
    document.execCommand('italic', false, null);
    return false;
});

// Подчёркнутый текст (u)
$('body').on('click', '.toolbar-u', function(){
    document.execCommand('underline', false, null);
    return false;
});

// Зачёркнутый текст (strike)
$('body').on('click', '.toolbar-s', function(){
    document.execCommand('strikethrough', false, null);
    return false;
});

// Верхний индекс (sup)
$('body').on('click', '.toolbar-sup', function(){
    document.execCommand('superscript', false, null);
    return false;
});

// Нижний индекс (sub)
$('body').on('click', '.toolbar-sub', function(){
    document.execCommand('subscript', false, null);
    return false;
});

// Маркированный список (ul)
$('body').on('click', '.toolbar-ul', function(){
    document.execCommand('insertUnorderedList', false, null);
    return false;
});

// Нумерованный список (ol)
$('body').on('click', '.toolbar-ol', function(){
    document.execCommand('insertOrderedList', false, null);
    return false;
});

// Параграф (p)
$('body').on('click', '.toolbar-p', function(){
    document.execCommand('formatBlock', false, 'p');
    return false;
});

// Заголовок (h1)
$('body').on('click', '.toolbar-h1', function(){
    document.execCommand('formatBlock', false, 'h1');
    return false;
});

// Горизонтальная линия (hr)
$('body').on('click', '.toolbar-hr', function(){
    document.execCommand('insertHorizontalRule', false, null);
    return false;
});

// Цитата (blockquote)
$('body').on('click', '.toolbar-blockquote', function(){
    document.execCommand('formatBlock', false, 'blockquote');
    return false;
});

// Изображение (img)
$('body').on('click', '.toolbar-img', function(){
    var url = prompt('Введите адрес изображения', 'https://snipp.ru/demo/526/image.jpg');
    document.execCommand('insertImage', false, url);
    return false;
});

// Ссылка (a)
$('body').on('click', '.toolbar-a', function(){
    var url = prompt('Введите URL', '');
    document.execCommand('CreateLink', false, url);
    return false;
});

// Удаление ссылки
$('body').on('click', '.toolbar-unlink', function(){
    document.execCommand('unlink', false, null);
    return false;
});

// Вставить html
$('body').on('click', '.toolbar-html', function(){
    var html = prompt('Введите HTML код', '');
    document.execCommand('insertHTML', false, html);
    return false;
});

// Вставить текст
$('body').on('click', '.toolbar-text', function(){
    var text = prompt('Введите текст', '');
    document.execCommand('insertText', false, text);
    return false;
});

// Выравнивание текста по левому краю
$('body').on('click', '.toolbar-left', function(){
    document.execCommand('justifyLeft', false, null);
    return false;
});

// Выравнивание текста по центру
$('body').on('click', '.toolbar-center', function(){
    document.execCommand('justifyCenter', false, null);
    return false;
});

// Выравнивание текста по правому краю
$('body').on('click', '.toolbar-right', function(){
    document.execCommand('justifyRight', false, null);
    return false;
});

// Выравнивание по ширине
$('body').on('click', '.toolbar-justify', function(){
    document.execCommand('justifyFull', false, null);
    return false;
});

// Шрифт
$('body').on('input', '.toolbar-font', function(){
    var val = $(this).val();
    document.execCommand('styleWithCSS', false, true);
    document.execCommand('fontName', false, val);
    document.execCommand('styleWithCSS', false, false);
});

// Размер шрифта
$('body').on('input', '.toolbar-size', function(){
    var val = $(this).val();
    document.execCommand('styleWithCSS', false, true);
    document.execCommand('fontSize', false, val);
    document.execCommand('styleWithCSS', false, false);
});

// Цвет шрифта
$('body').on('input', '.toolbar-color', function(){
    var val = $(this).val();
    document.execCommand('styleWithCSS', false, true);
    document.execCommand('foreColor', false, val);
    document.execCommand('styleWithCSS', false, false);
});

// Цвет фона
$('body').on('input', '.toolbar-bg', function(){
    var val = $(this).val();
    document.execCommand('styleWithCSS', false, true);
    document.execCommand('hiliteColor', false, val);
    document.execCommand('styleWithCSS', false, false);
});

// Отмена
$('body').on('click', '.toolbar-undo', function(){
    document.execCommand('undo', false, null);
    return false;
});

// Повтор
$('body').on('click', '.toolbar-redo', function(){
    document.execCommand('redo', false, null);
    return false;
});

// Удалить
$('body').on('click', '.toolbar-delete', function(){
    document.execCommand('delete', false, null);
    return false;
});

// Выделить всё
$('body').on('click', '.toolbar-selectAll', function(){
    document.execCommand('selectAll', false, null);
    return false;
});

// Очистить стили
$('body').on('click', '.toolbar-removeFormat', function(){
    document.execCommand('removeFormat', false, null);
    return false;
});

// Вырезать
$('body').on('click', '.toolbar-cut', function(){
    document.execCommand('cut', false, null);
    return false;
});

// Копировать
$('body').on('click', '.toolbar-copy', function(){
    document.execCommand('copy', false, null);
    return false;
});

$('body').on('focusout', '.editor', function() {
    var element = $(this);
    if (!element.text().replace(' ', '').length) {
        element.empty();
    }
});