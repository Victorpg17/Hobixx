document.addEventListener("DOMContentLoaded", function() {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.remove("hidden");
          entry.target.classList.add("visible");
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1  // cuando el 10% de la card es visible
    });

    document.querySelectorAll('.hobbie').forEach(card => {
      observer.observe(card);
    });
  });