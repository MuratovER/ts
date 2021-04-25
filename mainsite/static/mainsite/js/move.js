"use strict"
/*
TODO

сделать скрин

правильное перемещение левых блоков вправо вверх для этого нужно
найти центр элемента
*/
// первый вариант с событиями HTML5 

const  flexCol = document.querySelectorAll('.grid-col');
flexCol.forEach((item) => {
    item.addEventListener('click', () => {
        let halfHeight = item.clientHeight/2; 
        //console.log(item.getBoundingClientRect().top) ;
    });
})
//функция отрабатывающая при старте перемещение
function onDragStart(event) {
//console.log(event);
  event.dataTransfer.setData('text/plain', event.target.id);
  event.currentTarget.style.backgroundColor = 'lightgrey';
  console.log(event.currentTarget.style.backgroundColor);
}

//сброс событий браузера
function onDragOver(event) {
  
  event.preventDefault();
}

//функция отрабатывающая при окончании перемещения
function onDrop(event, elem) {
    
    const id = event.dataTransfer.getData('text');
   
    const draggableElement = document.getElementById(id);
    const dropzone = event.target.closest(`.grid-col`);
    console.log(dropzone);
    let dropzoneMargin =  getCoords(dropzone);
    
    flexCol.forEach((item, i ) => {
        
        let draggableElementMargin =  getCoords(item);
        
        if (item != draggableElement) {
            return;
        }
        /*
        //условие для предотврощения вставки двух длиных блоков в одну линию
        if (draggableElement.classList.contains('large-col') && (dropzone.classList.contains('small-col'))
        && (draggableElementMargin.top != dropzoneMargin.top) 
        &&(draggableElementMargin.left < dropzoneMargin.left)){
            alert('NO!')
            return;
        }
        */

        if (draggableElementMargin.left < dropzoneMargin.left){
            alert('1 Перемещение левых блоков вправо');
            dropzone.after(draggableElement);
            return;
        } else if (draggableElementMargin.left > dropzoneMargin.left){
            alert('3 Перемещение правых блоков влево');
            dropzone.before(draggableElement);
        } else {
            dropzone.before(draggableElement);
            alert('4 Все остальное');
        }
    });
    draggableElement.style.backgroundColor = '';
    event.dataTransfer.clearData();
  }

function getCoords(elem) { // кроме IE8-
    var box = elem.getBoundingClientRect();
    
    return {
        top: box.top + pageYOffset,
        left: box.left + pageXOffset
    };
}
