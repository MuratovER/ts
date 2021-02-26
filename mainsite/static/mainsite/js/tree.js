'use strict'
/*
TODO
заблокировать уроки пока предыдущий урок не пройден
при наведении на заблокированную сферу подсказывать, что он заблочен

для дерева получать данные из бд хранить в кэше
при обновлении в БД обновлять кэш

для теста в будущем получать условие из бд что все лекции и дз пройдены
для оптион установить selected из кэша
*/


window.onload = function() { 
    const tree = document.querySelector('.tree--container'),
        rootLists = document.querySelector('.tree--root--lists'),
        crownContent = document.querySelector('.tree--crown--flex'),
        crownItem = document.querySelectorAll('.tree--crown--item'),
        chooseSphereBtn = document.querySelectorAll('.tree--crown--item--btn'),
        sphereForm = document.querySelectorAll('.tree-sphere--form'),
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
    }, 

    lessonsLinksObj = {
        1: {
            1: "/first/first_chapters_self_discipline/",
            2: "/first/first_chapters_aims_in_life/",
            3: "/first/first_chapters_what_is_it/",
            4: "/first/first_chapters_edit/",
            5: "/first/first_chapters_self_assessment/",
        },
        2: {
            1: "/second/second_chapters_AimofLearning/",
            2: "/second/second_chapters_ForeignLanguage/",
            3: "/second/second_chapters_EfficientСommunications/",
            4: "/second/second_chapters_Thoughts/",
            5: "/second/second_chapters_ControlofTime/",
            6: "/second/second_chapters_ControlofTimeEfficiency/",
        },
        3: {
            1: "/third/third_chapters_GoodNutrition/",
            2: "/third/third_chapters_HealthySleep/",
            3: "/third/third_chapters_MovementandHardening/",
            4: "/third/third_chapters_LadieswithStress/",
        },
        4: {
            1: "/fourth/fourth_chapters_Conflicts/",
            2: "/fourth/fourth_chapters_Friends/",
            3: "/fourth/fourth_chapters_AbilitytoCommunicate/",
            4: "/fourth/fourth_chapters_RelationshipsintheFamily/",
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

    //показ нужной ветки
    const showBranch = (formItem, formIndex, sphereIndex) => {

        let lessonCount = lessonCounter(sphereIndex);
        
        crownBranch.forEach((item, i) => {
            let branchClass = item.classList.value,
                branchIndex = +branchClass[branchClass.length - 1];
            
            if(branchIndex == sphereIndex) {
               
                formItem.insertAdjacentHTML("afterEnd", 
                `<div class="tree--crown--item--branch  tree--crown--item--branch-${sphereIndex}">
                    <img src="../../static/mainsite/images/tree/lesson${sphereIndex}-branch.png" alt=""
                    class='tree--crown--item--branch--img tree--crown--item--branch--img--${sphereIndex}'>
                </div>`);

                let branch = formItem.parentElement.querySelector('.tree--crown--item--branch');
                
                // add links to lessons here
                for (let i = 1; i <= lessonCount; i++)
                {
                    branch.insertAdjacentHTML('beforeend', 
                    `<a id='branch-${sphereIndex}-lesson-${i}' href='${lessonsLinksObj[sphereIndex][i]}'class="tree--branch--lesson tree--branch--lesson-${i}">
                        <div class="tree--branch--lesson--border">
                            ${lessonsObj[sphereIndex][i]}
                        </div>
                    </a>`); 
                }
 
            let branchLessons = branch.querySelectorAll('.tree--branch--lesson--border');
            
                //изменение отображения ветки 
            if ((formIndex % 2) != (sphereIndex % 2)) {
                //console.log(formIndex, sphereIndex, 'НЕ совпадают');

                branch.style.transform = 'matrix(-1, 0, 0, 1, 0, 0)';
                
                //изменение отображения текста после отражения ветки
                branchLessons.forEach((item) => {
                    item.style.transform = 'rotateY(180deg)';
                });
            } 
            }
        });
    };
    
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

    //блокировка ранее выбранных тем
    const disableSphere = (disableObj, formNumber) => {
        
        if (disableObj.length == 0) {
            return;
        }
        let getArr = String(JSON.parse(localStorage.getItem(formNumber)));

        crownItemSphere.forEach((item, i) => {
           console.log(item);
            let option = item.querySelectorAll('.sphere--name');
            
                option.forEach((item, i) => {
                   //console.log(item, ++i);
                    for (let char of disableObj) {
                        
                        if (char == i) {
                            item.setAttribute('disabled', true);
                            //console.log(item);
                        }
                    }
                })
                for (let index of getArr) {
                    if (index == 1) {
                        crownItemSphere[2].setAttribute('disabled', 'disabled');
                    }
                    if (index == 2) {
                        crownItemSphere[0].setAttribute('disabled', 'disabled');
                    }
                    if (index == 3) {
                        crownItemSphere[3].setAttribute('disabled', 'disabled');
                    }
                    if (index == 4) {
                        crownItemSphere[1].setAttribute('disabled', 'disabled');
                    }
                }
        })
    }

    //получение и вставка свойств из LocalStorage
    const getProperty = (className, strClass) => {
        for (let key in localStorage) {

            if (localStorage.hasOwnProperty(strClass)) {
                
                let arr = localStorage.getItem(strClass),
                    modifyArr  = arr.split(' ');
                    
                modifyArr.forEach((item) => {
                    className.classList.add(item);
                })
            }
            else {
                console.log('такого свойства нет');
                return;
            }
        }
    }

    //общая функция работы с кэшом для кнопок и форм
    const getPropertyItem = ( formNumber, elements, addClass, environment) => {
        
        if (localStorage.hasOwnProperty(formNumber)) {
            
            let getArr = String(JSON.parse(localStorage.getItem(formNumber)));
            
            for (let index of getArr) {
                elements.forEach((item, i) => {
                    
                    if (+index == 1) {
                        elements[2].classList.add(addClass);
                    }
                    if (+index == 2) {
                        elements[0].classList.add(addClass);
                    }
                    if (+index == 3) {
                        elements[3].classList.add(addClass);
                    }
                    if (+index == 4) {
                        elements[1].classList.add(addClass);
                    }
                    if (environment) {
                        elements[0].style.marginRight = '40px';
                        elements[1].style.marginRight = '40px';
                    } 
                })
            }        
        } 
    }

    //получение веток из Кэша
    const getBranch = ( elemName) => {

        if (localStorage.hasOwnProperty(elemName)) {
            
            let getArr = String(JSON.parse(localStorage.getItem(elemName)));
                getArr = getArr.replace(/\\+/gi,"").replace(/\"+/gi,"");
                getArr = getArr.split(' ');
            
            getArr.forEach((item, i) => {
                
                if (isNaN(item)) {
                    let form = document.querySelector(`.${item}`);
                
                    showBranch(form, getArr[++i], getArr[++i]);
                    
                    showTest(getArr[--i], getArr[++i], true);
                }
            })
               
        } 
    }
    
     //render
     const render = () => {
          
            getProperty(rootLists, 'rootLists');
            getProperty(crownContent, 'crownContent');
            
        if (localStorage.hasOwnProperty('btnArr')) {

             getPropertyItem('btnArr',chooseSphereBtn, 'displayNone', false);
                
        } else {
            console.log('такого свойства нет');
            return;
        }
        
        if (localStorage.hasOwnProperty('sphereFormNumber')) {

            getPropertyItem('sphereFormNumber', sphereForm, 'displayFlex', true);
           
        }  else {
            console.log('такого свойства нет');
            return;
        }

        if (localStorage.hasOwnProperty('branchArr')) {

            getBranch('branchArr', crownItemSphere, 'none', false);
           
        }  else {
            console.log('такого свойства нет');
            return;
        }
        if (localStorage.hasOwnProperty('disableFormArr')) {
            let disableFormArr = localStorage.getItem('disableFormArr');
            disableFormArr = disableFormArr.replace(/\\+/gi,"").replace(/\"+/gi,"");
            //console.log(disableFormArr);
            disableSphere(disableFormArr, 'sphereFormNumber');
        }
    }   

    render();

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
            item.style.marginRight = '40px';
            item.style.marginLeft = '0px';
        } else {
            item.style.marginLeft = '40px';
            item.style.marginRight = '0px';
        }
    });

    //делегироваанное событие на дерево
    tree.addEventListener('click', (event) => {

        let target = event.target;
        
        //показ кроны
        if (target == rootLists) {
            
            rootLists.classList.add('displayNone');
            crownContent.classList.add('tree--crown--flex-active');

            localStorage.rootLists = rootLists.classList;
            localStorage.crownContent = crownContent.classList;
        }
        
        //показ формы выбора сферы развития
        if (target.matches('.tree--crown--item--btn')) {
            
            chooseSphereBtn.forEach( (elem, item) => {

                if (elem == target) {
                    let form2ClassValue = elem.nextElementSibling.classList.value,
                        form2Index = parseInt(form2ClassValue.replace(/\D+/g,""));
                    
                    elem.classList.add('displayNone');

                    if (elem.nextElementSibling.parentElement.matches('.tree--crown--item-right')) {
                        elem.nextElementSibling.style.marginLeft = '40px';
                    } else  elem.nextElementSibling.style.marginRight = '40px';

                    elem.nextElementSibling.classList.add('displayFlex');

                    //добавление кнопок в кэш
                    if (localStorage.hasOwnProperty('btnArr')) {
                        let btnArr = localStorage.getItem('btnArr');
                        btnArr = btnArr + form2Index;
                        
                        localStorage.btnArr = JSON.stringify(+btnArr);
                    } else {
                        let btnArr = + form2Index;
                        
                        localStorage.btnArr= JSON.stringify(btnArr);

                    }

                    //добавление форм в кэш
                    if (localStorage.hasOwnProperty('sphereFormNumber')) {
                        let sphereFormNumber = localStorage.getItem('sphereFormNumber');
                            
                        sphereFormNumber = sphereFormNumber + form2Index;
                        
                        localStorage.sphereFormNumber = JSON.stringify(+sphereFormNumber);
                    } else {
                        let sphereFormNumber = + form2Index;
                        localStorage.sphereFormNumber = JSON.stringify(sphereFormNumber);
                    }
                 
                }
            });
        }

        //показ нужной ветки
        if(target.matches('.tree-crown-sphere')) {

            target.addEventListener('change', () => { 

                let indexSelected = target.selectedIndex,
                    formClassValue = target.parentElement.classList.value,
                    formIndex = parseInt(formClassValue.replace(/\D+/g,""));

                //показ нужной ветки с уроками 
                showBranch(target.parentElement, formIndex, indexSelected);

                //добавление ветки в кэш
                if (localStorage.hasOwnProperty('branchArr')) {
                    let branchArr = localStorage.getItem('branchArr');
                    
                    branchArr = branchArr + target.parentElement.classList[1] + " " + formIndex + " " + indexSelected + " ";

                    localStorage.branchArr = JSON.stringify(branchArr);
                } else {
                    let branchArr;

                    branchArr = target.parentElement.classList[1] + " " + formIndex + " " + indexSelected + " ";
                    
                    localStorage.branchArr = JSON.stringify(branchArr);
                }
                
                 //показ нужного теста после ответа сервера в будущем
                 let sphereStatus = true; //состояние прохождения сферы и всех уроков

                 showTest(formIndex,indexSelected,sphereStatus);
               
                 target.setAttribute('disabled', 'disabled');

                 if (localStorage.hasOwnProperty('disableFormArr')) {
                    let disableFormArr= localStorage.getItem('disableFormArr');
                    disableFormArr = disableFormArr.replace(/\\+/gi,"").replace(/\"+/gi,"");
                    disableFormArr += indexSelected;
                    disableFormArr = disableFormArr.replace(/\\+/gi,"").replace(/\"+/gi,"");
                    localStorage.disableFormArr = JSON.stringify(disableFormArr);

                    disableSphere(disableFormArr);
                } else {
                    let disableFormArr = '';

                    disableFormArr += indexSelected;
                    
                    localStorage.disableFormArr = JSON.stringify(disableFormArr);

                    disableFormArr = disableFormArr.replace(/\\+/gi,"").replace(/\"+/gi,"");
                    disableSphere(disableFormArr);
                }                 
            })
        }
    });
};