//CHANGE NAVBAR ON SCROLL
//=====================METHOD 1 FOR CHANGING NAVBAR ON SCROLL=========================================
// window.addEventListener('scroll', () => {
//     document.querySelector('nav').classList.toggle('window-scroll', window.scrollY > 0)
// })//note: window-scroll is a class created and styled in css


//=====================METHOD 2 FOR CHANGING NAVBAR ON SCROLL=========================================
        //using ARROW FUNCTION
// const navScroll = document.querySelector('nav');
// window.addEventListener('scroll', ()=>{
//     navScroll.classList.toggle('window-scroll', window.scrollY > 0)
// })


//=====================METHOD 3 FOR CHANGING NAVBAR ON SCROLL========================================
const navOnScroll = document.querySelector('nav')
window.addEventListener('scroll', function(){
    navOnScroll.classList.toggle('window-scroll', window.scrollY > 0)
    //NOTE: classList.toggle() toggles between adding/removing a classList. if the class styling is absent, it will add it. but ifit is present, it will remove it
    //in the contest above it will add the styling with the class of window-scroll
})

//=============================TOGGLE FAQS

const faqs = document.querySelectorAll('.faq')

faqs.forEach(faq => {
    faq.addEventListener('click', () => {
        faq.classList.toggle('open')
        //change icon from + to - and vice versa
        const icon = faq.querySelector('.faq-icon i');
        if(icon.className === 'uil uil-plus'){
            icon.className ='uil uil-minus'   //not the single =
        }
        else{
            icon.className = 'uil uil-plus'
        }
    })
})




//==============================TOGGLE NAVBAR FOR MOBILE VIEW vs DESKTOP VIEW=============================
const menus = document.querySelector('.nav-menu');
const openBtns = document.querySelector('#open-menu-btn')
const closeBtns = document.querySelector('#close-menu-btn')

openBtns.addEventListener('click', () => {
    menus.style.display = 'flex'
    closeBtns.style.display = "inline-block"
    openBtns.style.display = "none"
})

//close nav menu
const closeNav = () =>{
    menus.style.display = "none";
    closeBtns.style.display = "none"
    openBtns.style.display= "inline-block"
}

closeBtns.addEventListener('click', closeNav);