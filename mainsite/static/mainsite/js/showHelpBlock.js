'use strict'

//подсказки о блоках
const hintBtn = document.querySelectorAll('.profile--help-btn'),
      closeHintBtn = document.querySelectorAll('.profile--help-info-close'), 
    helpBtn = document.querySelector('.feedback--error-btn'),
    setFeedbackBtn = document.getElementById('set--feedback-btn'),
    setBugBtn = document.getElementById('set--bug-btn');


    closeHintBtn.forEach(elem => {
        elem.addEventListener('click', (event) => {
            event.currentTarget.closest('.profile--help-info').classList.toggle('active--help-block');
        })
    });

    hintBtn.forEach(btn => {    
        btn.addEventListener('click', (event) => {
            
            event.currentTarget.nextElementSibling.classList.toggle('active--help-block');
        })
    })


    
helpBtn.addEventListener('click', (event)=> {
    console.log(event.currentTarget);
    setFeedbackBtn.parentElement.classList.toggle('activeFlex');
})


setFeedbackBtn.addEventListener('click', (event) => {
    console.log(event.currentTarget);
    setFeedbackBtn.parentElement.classList.toggle('activeFlex');
    document.body.insertAdjacentHTML('afterBegin', 
    `<div class="wrapper">
        <div class="evaluation">
            <button class='evaluation--close-btn'><img src="../../static/mainsite/images/evaluation/close.png" alt=""></button>
            <div class="evaluation--container">
                <div class="evaluation--header">
                    <h1 class="evaluation--title">Оцените наш сервис</h1>
                    <p class="evaluation--hint">Нажмите на один из смайликов, который по вашему мнению <br>
                        олицетворяет наш проект</p>
                </div>
                <div class="evaluation--smiles">
                    <button class="smile-block">1</button>
                    <button class="smile-block">2</button>
                    <button class="smile-block">3</button>
                    <button class="smile-block">4</button>
                    <button class="smile-block">5</button>
                    <button class="smile-block">6</button>
                    <button class="smile-block">7</button>
                    <button class="smile-block">8</button>
                    <button class="smile-block">9</button>
                    <button class="smile-block">10</button>
                   
                </div>
                <textarea name="" id="" class='evaluation--text'  = cols="30" rows="10" placeholder="Кратко расспишите ваше мнение о нас или о нашем проекте"></textarea>
                <div class="evaluation--question-line">
                    <p class="evaluation--question-txt">Посоветуете ли вы наш проект своим друзьям или знакомым</p>
                    <select name="" id="" class='evaluation--select'>
                        <option value="" selected class="evaluation--question-option">Однозначно да</option>
                        <option value="" class="evaluation--question-option">Однозначно нет</option>
                        <option value="" class="evaluation--question-option">Скорее всего нет</option>
                        <option value="" class="evaluation--question-option">Возможно нет</option>
                        <option value="" class="evaluation--question-option">Может быть</option>
                        <option value="" class="evaluation--question-option">Возможно да</option>
                        <option value="" class="evaluation--question-option">Скорее всего да</option>
                    </select>
                </div>
            </div>
            <a class="evaluation--send"><img src="../../static/mainsite/images/evaluation/check.png" alt="">Отправить</a>
        </div>
        <div class="evaluation--close-block">
            <button class='evaluation--close-btn'><img src="../../static/mainsite/images/evaluation/close.png" alt=""></button>
            <div class="evaluation--close--info">
                <img src="../../static/mainsite/images/evaluation/circle_check_outline.png" alt="" class="evaluation--close-img">
                <h1 class="evaluation--close-title">Спасибо за вашу оценку</h1>
                <p class="evaluation--close-hint">это окно закроется через 5 секунд...</p>
            </div>
        </div>
    </div>
    `);
    showFeedback();
});

setBugBtn.addEventListener('click', () => {
    setFeedbackBtn.parentElement.classList.toggle('activeFlex');
    document.body.insertAdjacentHTML('afterBegin', 
    `<div class="error-wrapper">
    <div class="collectErrors--block">
        <button class='collectErrors--close-btn'><img src="../../static/mainsite/images/errors/close.png" alt=""></button>
        <div class="collectErrors--container">
            <div class="collectErrors--container">
                <div class="collectErrors--header">
                    <h1 class="collectErrors--title">Вы нашли ошибку в нашей системе?</h1>
                    <p class="collectErrors--hint">Если вы случайно нажали на клавиши, пожалуйста нажмите на крестик, чтобы <br> выйти из этого меню</p>
                </div>
                <div class="collectErrors--errorInfo">
                    <h2 class="errorInfo--title">Где вы обнаружили ошибку?</h2>
                    <textarea name="" id="" cols="30" rows="1" class="error--textarea" placeholder="Напишите где вы обнаружили ошибку, желательно прикрепите ссылку на страницу"></textarea>
                    <div class="dropError--img">
                        <div class="dropError--info">
                            <h2 class="dropError--title"><img src="../../static/mainsite/images/errors/upload.png" alt="">
                                Выберите изображение</h2>
                            <p class="dropError--txt">Размер изображения не более 10 мб</p>
                        </div>
                    </div>
                    <div class="collectErrors--btnBlock">
                        <button class='send--error'><img src="../../static/mainsite/images/errors/check.png" alt="">Добавить</button>
                        <button class='close--error'><img src="../../static/mainsite/images/errors/close2.png" alt="">Отмена</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>`);
    collectErrors();
});

const showFeedback = () => {

    const sendBtn = document.querySelector('.evaluation--send'),
        evaluationCloseBtn = document.querySelector('.evaluation--close-btn'),
        evaluationWrapper = document.querySelector('.wrapper'),
        evaluationBlock = document.querySelector('.evaluation'),
        evaluationHintBlock = document.querySelector('.evaluation--close-block'),
        evaluationHintClose = evaluationHintBlock.querySelector('.evaluation--close-btn');

       

    sendBtn.addEventListener('click', () => {
        evaluationBlock.style.display = 'none';
        evaluationHintBlock.style.display = 'flex';

        let evaluationHide = setTimeout(() => {
            evaluationHintBlock.style.display = 'none';
            evaluationWrapper.style.display = 'none';
        }, 5000);

        evaluationHintClose .addEventListener('click', () => {
            evaluationHintBlock.style.display = 'none';
            evaluationWrapper.style.display = 'none';
            clearTimeout(evaluationHide);
        });
    });

    evaluationCloseBtn.addEventListener('click', () => {
        evaluationHintBlock.style.display = 'none';
        evaluationWrapper.style.display = 'none';
    });
}

const collectErrors = () => {
    const errorWrapper = document.querySelector('.error-wrapper'),
        collectErrorsBlock = document.querySelector('.collectErrors--block'),
        sendErrorBtn = document.querySelector('.send--error'),
        collectErrorsCloseBtn = document.querySelector('.collectErrors--close-btn')

    collectErrorsCloseBtn.addEventListener('click', () => {
        errorWrapper.style.display = 'none';
        collectErrorsBlock.style.display = 'none';
    });

    sendErrorBtn.addEventListener('click', () => {
        console.log(1);
        if (true) {
            sendErrorBtn.style.color = '#3751FF';
            sendErrorBtn.firstChild.setAttribute('src', '../../static/mainsite/images/errors/blueCheck.png')
        }
    });
}