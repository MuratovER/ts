$('.toolbar').on('click', function () {
    $(this).toggleClass('activated');
    return false;
})

function isChild (obj,parentObj){
    while (obj != undefined && obj != null && obj.classList != 'body'){
        if (obj == parentObj){
            return true;
        }
        obj = obj.parentNode;
    }
    return false;
}

$('.toolbar-i').on('click', function () {
    let selection = document.getSelection(),
        range = new Range(),
        content = [],
        editor = document.querySelector('.editor');
    range.setStart(selection.anchorNode, selection.anchorOffset);
    range.setEnd(selection.focusNode, selection.focusOffset);
    for (let i = 0; i < selection.rangeCount; i++) {
        content.push(selection.getRangeAt(i).cloneContents());
    };
    console.log(content.forEach(function (item) {
        console.log($('.text').find(item.textContent));
    }));
    console.log($('.text').find(content).wrap('<span></span>'));

})

$('.editor-non').on('focusout', function () {
    var element = $(this);
    if (!element.text().replace(' ', '').length) {
        element.empty();
    }
})