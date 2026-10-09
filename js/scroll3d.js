/* ==========================================================================
   REVATI ENTERPRISES - 3D Scroll & Interactive Slider Engine
   ========================================================================== */

function checkIsWelcomePage() {
    const path = window.location.pathname.toLowerCase();
    return path.endsWith('welcome.html') ||
           path.endsWith('/welcome') ||
           (document.body && document.body.classList.contains('welcome-page')) ||
           (document.title && document.title.toLowerCase().startsWith('welcome'));
}

document.addEventListener('DOMContentLoaded', () => {
    const isWelcome = checkIsWelcomePage();
    // On the Welcome page, all 3D movement, tilting, and 3D scroll rotations are disabled
    if (!isWelcome) {
        init3DScrollEffects();
        init3DTiltOnMouse();
    }
    initWelcome3DSlider(isWelcome);
});

// 1. CLEAN SCROLL PRESENTATION (Ensures no scroll locks, no disappearing cards, no jitter)
function init3DScrollEffects() {
    const targets = document.querySelectorAll('.page-part-3d, .card, .stat-item, .section-wrapper, .scroll-3d-element, .form-card, .sidebar-3d');
    
    // Ensure all elements are immediately visible without inline transform collisions
    targets.forEach(el => {
        el.classList.remove('scroll-3d-hidden');
        el.classList.add('scroll-3d-visible');
        el.style.opacity = '1';
    });
}

// 2. INTERACTIVE WELCOME SLIDER (Stationary & 2D on Welcome Page)
let currentSlideIndex = 0;
let slideInterval = null;

function initWelcome3DSlider(isWelcome) {
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
            if (!isWelcome) resetSlideTimer();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            goToSlide(currentSlideIndex + 1);
            if (!isWelcome) resetSlideTimer();
        });
    }

    dots.forEach((dot, idx) => {
        dot.addEventListener('click', (e) => {
            e.preventDefault();
            goToSlide(idx);
            if (!isWelcome) resetSlideTimer();
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
            if (!isWelcome) resetSlideTimer();
        } else if (swipeDistance > 40) {
            goToSlide(currentSlideIndex - 1);
            if (!isWelcome) resetSlideTimer();
        }
    }, { passive: true });

    function startSlideTimer() {
        if (isWelcome) return; // Completely disable auto-advancing movement on the Welcome page
        if (slideInterval) clearInterval(slideInterval);
        slideInterval = setInterval(() => {
            goToSlide(currentSlideIndex + 1);
        }, 5000);
    }

    function resetSlideTimer() {
        if (isWelcome) return;
        if (slideInterval) clearInterval(slideInterval);
        startSlideTimer();
    }

    if (!isWelcome) {
        startSlideTimer();
    }
}

// 3. MOUSE DYNAMIC TILT (Clean & lightweight)
function init3DTiltOnMouse() {
    // Disabled to preserve 60FPS fluid scrolling and responsive page interaction
}
