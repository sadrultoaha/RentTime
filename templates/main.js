const settingsIndicatorSlide = () => {
  const settingsIndicator = document.querySelector('.indicator');
  settingsIndicator.classList.toggle('active')
}


const postDetail = () => {
  window.location = "seller-details.html";
}
const goToCollectPeremeter = () => {
  window.location = "for-rent.html";
}

// Settings Menu Toggle
const settingMenu = document.querySelector('.setting-menu')
function settingsMenuToggle(){
    settingMenu.classList.toggle('setting-menu-height');
}


// Register
const studnet = document.getElementById('student');
const ownerII = document.getElementById('owner');
const btn = document.getElementById('btn');
const studentBtn = document.getElementById('studentBtn');
const ownerBtn = document.getElementById('ownerBtn');

const owner = () =>{
  studnet.style.left = '-100%'
  ownerII.style.left = '8%'
  btn.style.left = '50%'
  ownerBtn.style.color = 'white'
  studentBtn.style.color = '#2f3a4a'

}
const student = () =>{
  studnet.style.left = '8%'
  ownerII.style.left = '100%'
  btn.style.left = '0%'
  studentBtn.style.color = 'white'
  ownerBtn.style.color = '#2f3a4a'
}

// Multi page resgi
const slidePage = document.querySelector('.slide-page')
const FirstNextBtn = document.querySelector('.next-1')
const FirstPrevBtn = document.querySelector('.prev-1')
const secondPrevBtn = document.querySelector('.prev-2')

FirstNextBtn.addEventListener('click', ()=> {
  slidePage.style.marginLeft = '-50%';
});
secondPrevBtn.addEventListener('click', ()=>{
  slidePage.style.marginLeft = '0%';
})

// nav var
document.getElementById('nav-bar-open').addEventListener('click', () =>{
  const navItems = document.getElementById('nav-items');
  const close = document.getElementById('nav-bar-close');
  const open = document.getElementById('nav-bar-open');

  navItems.style.display = 'block';
  close.style.display = 'block';
  open.style.display = 'none';
})
document.getElementById('nav-bar-close').addEventListener('click', () =>{
  const navItems = document.getElementById('nav-items');
  const open = document.getElementById('nav-bar-open');
  const close = document.getElementById('nav-bar-close');

  navItems.style.display = 'none';
  open.style.display = 'block';
  close.style.display = 'none';
})

// Testimonail Section
const swiper = new Swiper('.swiper', {
    scrollbar: {
      el: '.swiper-scrollbar',
      draggable: true,
    },
});

