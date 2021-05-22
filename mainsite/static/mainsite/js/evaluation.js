const showFeedback = () => {

    const sendBtn = document.querySelector('.evaluation--send'),
        evaluationCloseBtn = document.querySelector('.evaluation--close-btn'),
        evaluationWrapper = document.querySelector('.wrapper'),
        evaluationBlock = document.querySelector('.evaluation'),
        evaluationHintBlock = document.querySelector('.evaluation--close-block'),
        evaluationHintClose = evaluationHintBlock.querySelector('.evaluation--close-btn');

        /*  document.getElementById('dialog').classList.add('show')
        const scrollY = document.documentElement.style.getPropertyValue('--scroll-y');
        const body = document.body;
        body.style.position = 'fixed';
        body.style.top = `-${scrollY}`;
        };
        const closeDialog = () => {
        const body = document.body;
        const scrollY = body.style.top;
        body.style.position = '';
        body.style.top = '';
        window.scrollTo(0, parseInt(scrollY || '0') * -1);
        document.getElementById('dialog').classList.remove('show');
        }
        window.addEventListener('scroll', () => {
        document.documentElement.style.setProperty('--scroll-y', `${window.scrollY}px`);
        });*/

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

