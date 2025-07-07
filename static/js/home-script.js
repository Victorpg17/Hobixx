const signOutBtn = document.querySelector('.icon');
const dropdownMenu = document.querySelector('.dropdown-menu');

// SHOW/HIDE MENU FOR SIGN OUT
signOutBtn.addEventListener('click', ()=>{
    dropdownMenu.classList.toggle('displayed');
});


document.querySelectorAll('.input-number').forEach(container => {
    const input = container.querySelector('input');
    const decrementBtn = container.querySelector('.decrement');
    const incrementBtn = container.querySelector('.increment');

    let interval; // To save the setInterval
    const delay = 150; // Continuous increase speed

    // FUNCTIONS TO GET THE MAX AND MIN
    const getMax = () => parseInt(input.max) || 60;
    const getMin = () => parseInt(input.min) || 0;

    // FUNCTION TO VIBRATE 
    function vibrateInput(input) {
      input.classList.add("vibrate");
      setTimeout(() => {
        input.classList.remove("vibrate");
      }, 300); // Duration of animation

      if (navigator.vibrate) {
        navigator.vibrate(100); // vibra por 100 ms
      }
    }

    // INCREMENT CONTROLED FUNCTION 
    function increase() {
      const current = parseInt(input.value) || 0;
      const max = getMax();
      if (current >= max) {
        input.value = 0; // Restart if it reaches the max
      } else {
        input.stepUp();
      }
    }

    // DECREMENT CONTROLED FUNCTION
    function decrease() {
      const current = parseInt(input.value) || 0;
      const min = getMin();
      if (current <= min) {
        input.value = min;
        vibrateInput(input);
      } else {
        input.stepDown();
      }
    }

    function startHold(action) {
      action(); // Run once inmediately
      interval = setInterval(action, delay); // And then every so often
    }
    
    function stopHold() {
      clearInterval(interval);
    }

    // EVENTS TO INCREMENT
    incrementBtn.addEventListener('mousedown', () => startHold(increase));
    incrementBtn.addEventListener('mouseup', stopHold);
    incrementBtn.addEventListener('mouseleave', stopHold);

    // EVENTS TO DECREMENT
    decrementBtn.addEventListener('mousedown', () => startHold(decrease));
    decrementBtn.addEventListener('mouseup', stopHold);
    decrementBtn.addEventListener('mouseleave', stopHold);

    // CHECK INPUTS VALUES WHEN TYPING
    input.addEventListener('input', () => {
        let val = input.value;

        // REMOVE UNNECESSARY ZEROS
        val = val.replace(/^0+(?!$)/, '');

        input.value = val;

        // CHECK LIMITS
        const max = getMax();
        const min = getMin();
        let numericVal = parseInt(val) || 0;

        if (numericVal > max) input.value = max;
        if (numericVal < min) input.value = min;
    });
});

// PROGRESS CIRCLE FILL
document.querySelectorAll('.progress-circle').forEach(circle => {
    const percent = circle.getAttribute('data-percentage');
    circle.style.setProperty('--percentage', percent + '%');
    circle.querySelector('.percentage-text').textContent = percent + '%';
});

// MENU EDIT/DELETE
document.addEventListener('DOMContentLoaded', ()=>{
  const toggleButtons = document.querySelectorAll('.ri-more-line');

  toggleButtons.forEach(button => {
    const hobbieContainer = button.closest('.hobbie');
    const menu = hobbieContainer.querySelector('.menu');

    button.addEventListener('click', ()=>{  
      menu.classList.toggle('hidden');
    });
    
     document.addEventListener('click', (e) => {
      if (!menu.contains(e.target) && e.target !== button) {
        menu.classList.add('hidden');
      }
    });
  });
});