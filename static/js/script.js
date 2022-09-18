
// const textEl = document.getElementById('welcome-text')
const text = "Welcome to Hemophiia Society Nagpur Chapter..!"
const burger = document.getElementById('burger-menu')
const openMenu = document.getElementById('nav-div')
const toggle = document.querySelector('.toggle-theme')
// console.log(darkTheme);



burger.addEventListener('click', () =>{
    openMenu.classList.toggle('show');
    if(openMenu.classList.contains('show')){
        burger.innerHTML = "&#10006;"
    } else{burger.innerHTML = '&#9776;' }
    // console.log('clicked')
})

// //<-------------------- animation on scroll ---------------------->

// //initialize throttleTimer as false
// let throttleTimer = false;
 
// const throttle = (callback, time) => {
//     //don't run the function while throttle timer is true
//     if (throttleTimer) return;
     
//     //first set throttle timer to true so the function doesn't run
//     throttleTimer = true;
     
//     setTimeout(() => {
//         //call the callback function in the setTimeout and set the throttle timer to false after the indicated time has passed 
//         callback();
//         throttleTimer = false;
//     }, time);
// }
// window.addEventListener('scroll', () => {
//     throttle(animateDiv, 250);
//   })

// const scrollElement = document.querySelectorAll('.scroll-element');
// // window.addEventListener('scroll',checkBoxes);


// animateDiv();
// function animateDiv() {
//    const triggerBottom=window.innerHeight / 5 * 4;

//    scrollElement.forEach(div => {
//        const divTop = div.getBoundingClientRect().top;

//        if(divTop < triggerBottom ){
//            div.classList.add('scrolled');

//        }
//        else {
//            div.classList.remove('scrolled');
//        }
//    })
// }


// progress bar


const progressBar = document.getElementById('progress-bar')
const section = document.getElementById('progress-div')
const goTotop = document.getElementById("go-to-top")
const animateProgressBar = () =>{
    let scrollDistance = -section.getBoundingClientRect().top;
    let progressWidth = (scrollDistance / (section.getBoundingClientRect().height - document.documentElement.clientHeight)) * 100
    // console.log(section.getBoundingClientRect().height)
    let value = Math.floor(progressWidth)
    progressBar.style.width = value + "%"
    if(value < 0){
        progressBar.style.width = "0%"
        
    }
    else if(value > 55){
        goTotop.classList.add('show')
    }
    else if(value > 100){
        progressBar.style.width = "100%"
    }
    else if(value < 55){
        goTotop.classList.remove('show')

    }
}
window.addEventListener('scroll',animateProgressBar)

const skeletons = document.querySelectorAll('.skeleton')
skeletons.forEach((skeleton) => {
 setTimeout(() => {
 skeleton.classList.remove('skeleton')
 }, 4000)
})


// preloader ----------------------->

var load = document.getElementById("loading");
function loader(){
    load.style.display = "none"
    // setTimeout(() => {
    //     load.style.display = "none"
    //     }, 2000)
}

// dark mode------------------------------->
// toggle.addEventListener('click', (e) => {
//     const html = document.querySelector('html')
//     const darkTheme = document.getElementById('fa-sun')

//     if(html.classList.contains('dark')) {
//         html.classList.remove('dark')
//         darkTheme.classList.remove('fa-moon')
//         darkTheme.classList.add('fa-sun')
//         // e.target.innerHTML = "Dark Mode"
//     } else {
//         html.classList.add('dark')
//         // e.target.innerHTML = "Light Mode"
//         darkTheme.classList.remove('fa-sun')
//         darkTheme.classList.add('fa-moon')
//     }
// })