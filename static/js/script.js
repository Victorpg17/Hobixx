// VARIABLES
const container = document.querySelector('.container');
const signupBtn = document.getElementById('sign-up');
const loginBtn = document.getElementById('login');

const signupForm =  document.getElementById('signupForm');
const loginForm = document.getElementById('loginForm');
const matchMsg = document.querySelector('.pswrd-match');

const password = signupForm.querySelector('input[name="password"]');
const confirmPassword = signupForm.querySelector('input[name="confirmPassword"]');

const toggleBtn = document.querySelectorAll('.toggleBtn');

// RESET FORMS WITH DELAY
function delayedReset(form, delay = 1200) {
    setTimeout(() => form.reset(), delay);
    if (form == signupForm) {
        setTimeout(() => form.classList.remove('success'), delay);
        setTimeout(() => form.classList.remove('error'), delay);
    }    
}

// ADD/REMOVE CLASS FOR BG ANIMATION
signupBtn.addEventListener('click', ()=>{
    container.classList.add('active');
    delayedReset(loginForm);
});

loginBtn.addEventListener('click', ()=>{
    container.classList.remove('active');
    delayedReset(signupForm);
});

// SHOW PASSWORDS
toggleBtn.forEach(element => {
    let pswrd = element.previousElementSibling;
    
    element.addEventListener('click', ()=>{
        if (pswrd.type === 'password'){
            pswrd.setAttribute('type', 'text')
            element.classList.add('hide')
        } else {
            pswrd.setAttribute('type', 'password')
            element.classList.remove('hide')
        }
    })
});

// CHECK PASSWORD AND HER CONFIRMATION
function checkPasswords() {
    if (confirmPassword.value == '') {
        signupForm.classList.remove('success')
        signupForm.classList.remove('error')
        return;
    }

    if (password.value === confirmPassword.value) {
        signupForm.classList.add('success');
        signupForm.classList.remove('error');
    } else {
        signupForm.classList.add('error')
        signupForm.classList.remove('success');
    }
}

// LISTEN CHANGES WHILE TYPE
password.addEventListener('input', checkPasswords);
confirmPassword.addEventListener('input', checkPasswords);

// CHECK PASSWORD AND HER CONFIRMATION
signupForm.addEventListener('submit', (e)=>{
    if (password.value !== confirmPassword.value) {
        e.preventDefault();
        password.style.borderColor = 'red';
        confirmPassword.style.borderColor = 'red';
    }
});