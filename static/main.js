document.addEventListener('DOMContentLoaded', function() {
    // Handle contact form submission with reCAPTCHA v3
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            grecaptcha.ready(function() {
                grecaptcha.execute('{{ recaptcha_site_key }}', {action: 'submit'}).then(function(token) {
                    document.getElementById('recaptchaResponse').value = token;
                    contactForm.submit();
                });
            });
        });
    }


    // 1. Initialize AOS (Animate on Scroll) Library
    AOS.init({
        duration: 800,
        once: true,
        offset: 50,
    });

    // 2. Initialize Typed.js for the typing animation
    // Check if the target element exists before initializing
    if (document.getElementById('typed-text')) {
        const typed = new Typed('#typed-text', {
            strings: ['Hi, I\'m Diego Natanael.'],
            typeSpeed: 50,
            startDelay: 900,
            showCursor: false,
        });
    }

    // 3. Initialize Particles.js (only once)
    if (document.getElementById('particles-js')) {
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#555555" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5, "random": false },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": true, "distance": 150, "color": "#444444", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 2, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": false }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": false }, "resize": true },
                "modes": { "repulse": { "distance": 100, "duration": 0.4 } }
            },
            "retina_detect": true
        });
    }

    // 4. Make the "Enter My Workshop" button scroll smoothly
    const ctaButton = document.querySelector('.cta-button');
    if (ctaButton) {
        ctaButton.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }

    // 5. Iframe Modal Logic
    const modal = document.getElementById('demo-modal');
    const iframe = document.getElementById('demo-iframe');
    const closeModalBtn = document.querySelector('.close-modal-btn');

    // Make sure the modal elements exist before adding listeners
    if (modal && iframe && closeModalBtn) {
        // Use event delegation for the demo buttons for robustness
        document.body.addEventListener('click', function(e) {
            if (e.target.classList.contains('launch-demo-btn')) {
                const demoUrl = e.target.dataset.demourl;
                if (demoUrl) {
                    iframe.src = demoUrl;
                    modal.style.display = 'block';
                }
            }
        });

        const closeModal = function() {
            modal.style.display = 'none';
            iframe.src = ''; // Stop the iframe content from running
        };

        closeModalBtn.addEventListener('click', closeModal);

        window.addEventListener('click', function(e) {
            if (e.target == modal) {
                closeModal();
            }
        });
    }
});