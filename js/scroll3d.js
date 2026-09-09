/* ==========================================================================
   REVATI ENTERPRISES - 3D Scroll & Interactive Slider Engine
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    init3DScrollEffects();
    initWelcome3DSlider();
    init3DTiltOnMouse();
});

// 1. DYNAMIC 3D SCROLL REVEAL ON EVERY SCROLL
function init3DScrollEffects() {
    const targets = document.querySelectorAll('.page-part-3d, .card, .stat-item, .section-wrapper, .scroll-3d-element, .form-card, .sidebar-3d');
    
    targets.forEach(el => {
        el.classList.add('scroll-3d-element');
        el.classList.add('scroll-3d-hidden');
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.remove('scroll-3d-hidden');
                entry.target.classList.add('scroll-3d-visible');
            } else {
                // Re-trigger 3D rotation when scrolling out and back in
                if (entry.boundingClientRect.top > 0) {
                    entry.target.classList.add('scroll-3d-hidden');
                    entry.target.classList.remove('scroll-3d-visible');
                }
            }
        });
    }, {
        threshold: 0.12,
        rootMargin: "0px 0px -50px 0px"
    });

    targets.forEach(el => observer.observe(el));

    // Dynamic 3D parallax scroll depth shift
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const orbs = document.querySelectorAll('.bg-3d-orb');
        orbs.forEach((orb, idx) => {
            const speed = (idx + 1) * 0.15;
            orb.style.transform = `translateY(${scrolled * speed}px) rotate(${scrolled * 0.05}deg)`;
        });
    }, { passive: true });
}

// 2. INTERACTIVE 3D WELCOME SLIDER
let currentSlideIndex = 0;
let slideInterval = null;

function initWelcome3DSlider() {
    const track = document.getElementById('welcomeSliderTrack');
    const slides = document.querySelectorAll('.welcome-slide');
    const dots = document.querySelectorAll('.slider-dot');
    
    if (!track || slides.length === 0) return;

    function goToSlide(index) {
        if (index < 0) index = slides.length - 1;
        if (index >= slides.length) index = 0;
        currentSlideIndex = index;
        
        track.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
        
        dots.forEach((dot, i) => {
            if (i === currentSlideIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    const prevBtn = document.getElementById('sliderPrevBtn');
    const nextBtn = document.getElementById('sliderNextBtn');

    if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            goToSlide(currentSlideIndex - 1);
            resetSlideTimer();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            goToSlide(currentSlideIndex + 1);
            resetSlideTimer();
        });
    }

    dots.forEach((dot, idx) => {
        dot.addEventListener('click', (e) => {
            e.preventDefault();
            goToSlide(idx);
            resetSlideTimer();
        });
    });

    // Touch Swipe Support for Mobile & Tablet Devices
    let touchStartX = 0;
    let touchEndX = 0;

    track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        const swipeDistance = touchEndX - touchStartX;
        if (swipeDistance < -40) {
            goToSlide(currentSlideIndex + 1);
            resetSlideTimer();
        } else if (swipeDistance > 40) {
            goToSlide(currentSlideIndex - 1);
            resetSlideTimer();
        }
    }, { passive: true });

    function startSlideTimer() {
        if (slideInterval) clearInterval(slideInterval);
        slideInterval = setInterval(() => {
            goToSlide(currentSlideIndex + 1);
        }, 5000);
    }

    function resetSlideTimer() {
        if (slideInterval) clearInterval(slideInterval);
        startSlideTimer();
    }

    startSlideTimer();
}

// 3. MOUSE DYNAMIC 3D TILT EFFECT ON CARDS
function init3DTiltOnMouse() {
    const tiltCards = document.querySelectorAll('.hero-section, .stat-item, .card-3d');
    
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -5;
            const rotateY = ((x - centerX) / centerX) * 5;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
        });
    });
}
