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

const postDetail = () => {
    window.location = "seller-details.html";
}

