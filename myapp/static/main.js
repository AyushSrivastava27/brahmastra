AOS.init();
const navbar=document.querySelector('.navbar');
//const menuBtn=document.querySelector('.menu-btn');
// const menu=document.querySelector('.menu');
//menuBtn.addEventListener('click',()=>{menu.classList.add('menu-open')});
window.addEventListener('click',e=>{if(e.target.classList.contains('menu-open')){e.target.classList.remove('menu-open')}});
window.addEventListener("scroll",()=>{if(scrollY>0){
   
    navbar.classList.add('mynavbar-active')}else{navbar.classList.remove('mynavbar-active')}});

const swiper=new Swiper(".mySwiper",{slidesPerView:1,spaceBetween:30,slidesPerGroup:1,loop:!0,loopFillGroupWithBlank:!0,breakpoints:{'800':{slidesPerView:2,slidesPerGroup:2},'1000':{slidesPerView:3,slidesPerGroup:3},},pagination:{el:".swiper-pagination",clickable:!0,},navigation:{nextEl:".swiper-button-next",prevEl:".swiper-button-prev",},})

// popup javascript//

window.addEventListener("load",function(){
    this.setTimeout(
        function open(event){
            document.querySelector(".popup").style.display="block"
        },
        1000
    )
});
document.querySelector("#close").addEventListener("click",function(){
    document.querySelector(".popup").style.display="none";
});