const container = document.querySelector('.container');
const signupBtn = document.getElementById('sign-up');
const loginBtn = document.getElementById('login');
const [loginForm, signupForm] = document.querySelectorAll('form');

// Reset form with delay
function delayedReset(form, delay = 1200) {
    setTimeout(() => form.reset(), delay);
}

signupBtn.addEventListener('click', ()=>{
    container.classList.add('active');
    delayedReset(loginForm);
});

loginBtn.addEventListener('click', ()=>{
    container.classList.remove('active');
    delayedReset(signupForm);
});

