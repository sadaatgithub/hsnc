const slides = document.querySelectorAll('.slide')
const leftBtn = document.getElementById('left')
const rightBtn = document.getElementById('right')
const time_line = document.querySelector(".time-line");
const cardStory = document.querySelectorAll(".card-story");
const nextBtn = document.querySelector(".next-btn");
const prevBtn = document.querySelector(".prev-btn");
// console.log(cardStory);

slides[0].classList.add('active')

// function setSlideToLeft(){
//     cardStory.forEach(function (slide,index) {
//         slide.style.left = `${index * 100}%`;
//     })
// }
// setSlideToLeft()

// let counter = 0;
// nextBtn.addEventListener("click", function () {
//   counter++;
//   carousel();
//   resetAutoSlide()

// });

// prevBtn.addEventListener("click", function () {
//   counter--;
//   carousel();
//   resetAutoSlide()

// });

// function carousel() {

// //   working with slides
//   if (counter === cardStory.length) {
//     counter = 0;
//   }
//   if (counter < 0) {
//     counter = cardStory.length - 1;
//   }
//   // working with buttons

//   if (counter < cardStory.length - 1 || counter > 0 ) {
//     setSlideToLeft()
  
//   } 
//   cardStory.forEach(function (slide) {
//     slide.style.transform = `translateX(-${counter * 100}%)`;
//   });
// }
// let timePeriod = 4000
// let autoslide = setInterval(() => {
//     counter++
//     carousel()
//   }, timePeriod);

// function resetAutoSlide () {
//     clearInterval(autoslide)
//     autoslide = setInterval(() => {
//         counter++
//         carousel()
//       }, timePeriod);

// }
// prevBtn.style.display = "none";






// --------------------------------- real story slider------------------
function setSlideToLeft(){
    cardStory.forEach(function (slide,index) {
        slide.style.left = `${index * 100}%`;
    })
}
setSlideToLeft()
let counter = 0;

let timeperiod = 4000
let autoslide = setInterval(carousel,timeperiod)

function resetAutoSlide (){
    clearInterval(autoslide)
    autoslide = setInterval(carousel,timeperiod)
}


function cardSlide () {
    cardStory.forEach(function (slide) {
        slide.style.transform = `translateX(-${counter * 100}%)`;
      });
}

nextBtn.addEventListener("click", function () {
    
    counter++;
        if(counter > cardStory.length - 1 ){
            counter = 0
        }
        cardSlide()
        resetAutoSlide()

    
  
  });
  
  prevBtn.addEventListener("click", function () {
    counter--;
    if(counter < 0 ){
        counter = cardStory.length - 1
    }
    cardSlide()
    resetAutoSlide()
    console.log(counter)

  
  });

  function carousel(){
      counter++;
      if(counter > slides.length - 1){
          counter = 0
      }
      cardSlide()
  }




// ------------------------------------------------ real story slider ends here

// slides[0].classList.add('active')
// console.log(slides[0]);

// ---------------------- main slider-----------------------------------------
if (slides) {
let activeSlide = 0;
let interval = setInterval(run, 5000)

function run (){
    activeSlide++;
    if(activeSlide > slides.length - 1) {
        activeSlide = 0;
    }
    setActiveSlide()
    clearInterval(counterLine)
    startTimerLine(0)

}
function resetInterval () {
    clearInterval(interval)
    interval = setInterval(run, 5000)

}
function stopShow(){
    clearTimeout(interval)
    clearTimeout(counterLine)
}
function runShow(){
    interval = setInterval(run, 5000)
    startTimerLine(0)

  
}

rightBtn.addEventListener('click', () => {
    activeSlide++;

    if(activeSlide > slides.length - 1) {
        activeSlide = 0;
    }
    setActiveSlide()
    // changeImage()
    resetInterval()
    clearInterval(counterLine)

    startTimerLine(0)


})
leftBtn.addEventListener('click', () => {
    activeSlide--;

    if(activeSlide < 0) {
        activeSlide = slides.length - 1;
    }
    setActiveSlide()
    // changeImage()
    resetInterval()
    clearInterval(counterLine)
    startTimerLine(0)


})

function setActiveSlide() {
    slides.forEach(slide => 
        slide.classList.remove('active'))

        slides[activeSlide].classList.add('active')
    
}

}

// timeliner
let counterLine;

function startTimerLine(time){
    counterLine = setInterval(timer, 1);
    function timer(){
        time += 0.1; //upgrading time value with 1
        // console.log(time)
        time_line.style.width = time + "%"; //increasing width of time_line with px by time value
        if(time >= 100){ //if time value is greater than 549
            clearInterval(counterLine); //clear counterLine
            // resetInterval()
        }
    }
}

