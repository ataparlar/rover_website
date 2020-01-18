const carouselSlide = document.querySelector('.carousel-slide');
const carouselImages = document.querySelectorAll('.carousel-slide img');

//Buttons

const prevBtn = document.querySelector('#prev');
const pnetxBtn = document.querySelector('#next');

//counter

let counter = 1;
const size = carouselImage[0].clientWidth;

carouselSlide.style.transform = 'translateX(' + (-size*counter) + 'px)';