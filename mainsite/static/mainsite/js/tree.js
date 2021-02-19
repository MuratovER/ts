'use strict'
/*
добавить проверку на повторение сфер
отображать тесты не по номерам а по value
заблокировать уроки пока предыдущий урок не пройден
динамическое создание сфер
при наведении на заблокированную сферу подсказывать, что он заблочен
для оптион установить лэйблы
*/
window.onload = function() { 
    const tree = document.querySelector('.tree--container'),
        rootLists = document.querySelector('.tree--root--lists'),
        crownContent = document.querySelector('.tree--crown--flex'),
        crownItem = document.querySelectorAll('.tree--crown--item'),
        chooseSphereBtn = document.querySelectorAll('.tree--crown--item--btn'),
        crownBranch = document.querySelectorAll('.tree--crown--item--branch'),
        crownTests = document.querySelectorAll('.tree--crown--item--test'),
        crownLink = document.querySelectorAll('.tree--branch--lesson'),
        crownItemSphere = document.querySelectorAll('.tree-crown-sphere');
    let disableSphereObj = [],
        lessonsArr = [],
        lessonsObj = {
        1: {
            1: "Самодисциплина",
            2: "Цели в жизни",
            3: "Что это такое?",
            4: "Изменение",
            5: "Самооценка",
        },
        2: {
            1: "Школа",
            2: "Иностанный язык",
            3: "Эффективные коммуникации",
            4: "Мышление",
            5: "Планирование времени",
            6: "Эффективность",
        },
        3: {
            1: "Прaвильное питание",
            2: "Здоровый сон",
            3: "Движение и закаливание",
            4: "“Ладим” со стрессом",
        },
        4: {
            1: "Конфликты",
            2: "Друзья",
            3: "Умение общаться",
            4: "Отношения в семье",
        }
    }

    //подсчет кол-во уроков в теме
    const lessonCounter = (i) => {
        let counter = 0;
        for (let k in lessonsObj[i]) {
            counter++;
        }

        return counter;
    }

    //стилизация четных и нечетных форм
    crownItemSphere.forEach((item, i) => {
        if(item.parentElement.parentElement.matches(".tree--crown--item-left")) {
            item.style.borderRight = '20px solid #5EA2FF';
        } else {
            item.style.borderLeft = '20px solid #5EA2FF';
            item.dir = 'rtl';
        }
    });

    //стилизация кнопок
    chooseSphereBtn.forEach((item) => {
        if(item.parentElement.matches(".tree--crown--item-left")) {
            item.style.marginRight = '48px';
            item.style.marginLeft = '0px'
        } else {
            item.style.marginLeft = '50px'
            item.style.marginRight = '0px';
        }
    });

    //блокировка ранее выбранных тем
    const disableSphere = (disableObj) => {

        if (disableObj.length == 0) {
            return;
        }

        crownItemSphere.forEach((item) => {
            
            let option = item.querySelectorAll('.sphere--name');

                option.forEach((item, i) => {
                    
                    if (disableObj.includes(i++))  {
                        item.setAttribute('disabled', true);
                    }
                })
        })
    }
    
    //показ нужого теста
    const showTest = (formIndex, sphereIndex, status) => {
        //status переменная от
        if (!status) {
            return;
        }

        crownTests.forEach((item, i) => {
            let testTxt = item.lastElementChild.textContent,
                testIndex = +testTxt[testTxt.length - 1];
                
            if (testIndex == formIndex) {
                item.lastElementChild.setAttribute('href', `http://127.0.0.1:8000/test${sphereIndex}/#`);
                item.classList.remove('test--disabled');
            }
        });
    }

   //показ нужной ветки с уроками 
   const showBranch = (formItem, formIndex, sphereIndex) => {

        let lessonCount = lessonCounter(sphereIndex);
        
        crownBranch.forEach((item, i) => {
            let branchClass = item.classList.value,
                branchIndex = +branchClass[branchClass.length - 1];
            
            if(branchIndex == sphereIndex) {
               
                formItem.insertAdjacentHTML("afterEnd", 
                `<div class="tree--crown--item--branch  tree--crown--item--branch-${sphereIndex}">
                    <img src="tree/lesson${sphereIndex}-branch.png" alt=""
                    class='tree--crown--item--branch--img'>
                </div>`);

                let branch = formItem.parentElement.querySelector('.tree--crown--item--branch');
                
                for (let i = 1; i <= lessonCount; i++)
                 {
                    branch.insertAdjacentHTML('beforeend', 
                    `<a id='branch-${sphereIndex}-lesson-${i}' href='#'class="tree--branch--lesson tree--branch--lesson-${i}">
                        <div class="tree--branch--lesson--border">
                            ${lessonsObj[sphereIndex][i]}
                        </div>
                    </a>`); 
                    console.log(lessonsObj[sphereIndex][i]);
            
                }

                /*
                //добавляется после селект
                formItem.insertAdjacentHTML("afterEnd", 
                `<div class="tree--crown--item--branch  tree--crown--item--branch-${sphereIndex}">
                <img src="../../static/mainsite/images/tree/lesson${sphereIndex}-branch.png" alt=""
                class='tree--crown--item--branch--img'>
                <a id='branch-${sphereIndex}-lesson-1' href='#'class="tree--branch--lesson tree--branch--lesson-1">
                    <div class="tree--branch--lesson--border">
                        1
                    </div>
                </a>
                <a id='branch-${sphereIndex}-lesson-2' href='#'class="tree--branch--lesson tree--branch--lesson-2">
                    <div class="tree--branch--lesson--border">
                        2
                    </div>
                </a>
                <a id='branch-${sphereIndex}-lesson-3'  href='#'class="tree--branch--lesson tree--branch--lesson-3">
                    <div class="tree--branch--lesson--border">
                        3
                    </div>
                </a>
                <a id='branch-${sphereIndex}-lesson-4'  href='#'class="tree--branch--lesson tree--branch--lesson-4">
                    <div class="tree--branch--lesson--border">
                        4
                    </div>
                </a>
                <a id='branch-${sphereIndex}-lesson-5'  href='#'class="tree--branch--lesson tree--branch--lesson-5">
                    <div class="tree--branch--lesson--border">
                        5
                    </div>
                </a>
            </div>`);
            */
           
            let branchLessons = branch.querySelectorAll('.tree--branch--lesson--border');
            
                //изменение отображения ветки 
            if ((formIndex % 2) != (sphereIndex % 2)) {
                console.log(formIndex, sphereIndex, 'НЕ совпадают');

                branch.style.transform = 'matrix(-1, 0, 0, 1, 0, 0)';
                
                //изменение отображения текста после отражения ветки
                branchLessons.forEach((item) => {
                    item.style.transform = 'rotateY(180deg)';
                });
            } 
            }
        });
    };

    //делегироваанное событие на дерево

    tree.addEventListener('click', (event) => {
        let target = event.target;
        
        
        //показ кроны
        if (target == rootLists) {

            rootLists.style.display = 'none';
            crownContent.style.display = 'flex';

            document.body.insertAdjacentHTML("beforeend", 
            `<style>
            .tree--crown--flex {
                bottom: 270px;
                display: flex;
                width: 1400px
                flex-direction: row
                margin-left: auto;
                margin-right:  auto;
            }
            </style>`)
            
        }
        
        //показ формы выбора сферы развития
        if (target.matches('.tree--crown--item--btn')) {
            
            chooseSphereBtn.forEach( (elem, item) => {

                if (elem == target) {
                    elem.style.display = 'none';
                    if (elem.nextElementSibling.parentElement.matches('.tree--crown--item-right')) {
                        elem.nextElementSibling.style.marginLeft = '40px';
                    } else  elem.nextElementSibling.style.marginRight = '40px';
                    elem.nextElementSibling.style.display = 'flex';
                }
            });
        }

        //показ нужной ветки
        if(target.matches('.tree-crown-sphere')) {

            target.addEventListener('change', () => { 

                let indexSelected = target.selectedIndex,
                    formClassValue = target.parentElement.classList.value,
                    formIndex = +formClassValue[formClassValue.length - 1];
                            
                //показ нужной ветки с уроками пока не интерактивно
                showBranch(target.parentElement,formIndex, indexSelected);

                 //показ нужного теста после ответа сервера в будущем
                 let sphereStatus = true; //состояние прохождения сферы и всех уроков

                 showTest(formIndex,indexSelected,sphereStatus);
                
                 target.setAttribute('disabled', 'disabled');
                
                 disableSphereObj.unshift(indexSelected);
            })
            disableSphere(disableSphereObj);
        }
    });
};