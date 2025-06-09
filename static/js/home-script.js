const signOutBtn = document.querySelector('.icon');
const dropdownMenu = document.querySelector('.dropdown-menu');

signOutBtn.addEventListener('click', ()=>{
    dropdownMenu.classList.toggle('displayed');
});