/* ==========================================================================
   REVATI ENTERPRISES - 4K Cinematic Video Intro Engine
   ========================================================================== */

(function() {
    'use strict';

    const SCENES = [
        {
            id: 0,
            tag: "01: Corporate HQ",
            title: "CORPORATE HQ & FACILITY MANAGEMENT",
            desc: "ISO 9001:2015 certified integrated facility management for 500+ commercial towers across India.",
            image: "images/video_scene_corporate.jpg",
            caption: "REVATI ENTERPRISES — Delivering 24/7 corporate facility management and executive housekeeping SLA perfection."
        },
        {
            id: 1,
            tag: "02: Spider Glass Facade",
            title: "HIGH-RISE FACADE SPIDER CLEANING",
            desc: "Specialized rope access spider technicians with hydrophobic glass protection.",
            image: "images/video_scene_facade.jpg",
            caption: "HIGH-RISE SPIDER FACADE CARE — Certified rope-access technicians maintaining pristine glass skyscraper exteriors."
        },
        {
            id: 2,
            tag: "03: MEP Technical Hub",
            title: "MEP & ELECTRICAL ENGINEERING",
            desc: "24/7 technical operations, HVAC chiller auditing, and electrical substation management.",
            image: "images/video_scene_mep.jpg",
            caption: "MEP ENGINEERING OPERATIONS — Expert power grid management, HVAC chiller diagnostics, and rapid emergency response."
        },
        {
            id: 3,
            tag: "04: Hygiene SLA",
            title: "HOSPITAL-GRADE SANITIZATION",
            desc: "Mechanized floor scrubbing, hospital-grade sanitization & 99.8% SLA score.",
            image: "images/video_scene_hygiene.jpg",
            caption: "SANITY & HYGIENE SLA — Mechanized floor scrubbing, eco-friendly chemical sanitization, and 99.8% hygiene accuracy."
        }
    ];

    let currentSceneIndex = 0;
    let isPlaying = true;
    let isMuted = true;
    let progressPercent = 0;
    let timerId = null;
    let audioCtx = null;
    let oscillator = null;
    let gainNode = null;
    let typeWriterTimer = null;

    function renderVideoIntroHTML(mountEl) {
        if (!mountEl) return;

        mountEl.innerHTML = `
            <div class="video-intro-wrapper">
                <div class="video-player-container" id="videoPlayerContainer">
                    <!-- Scene Background Images -->
                    ${SCENES.map((scene, idx) => `
                        <img src="${scene.image}" alt="${scene.title}" class="video-scene-bg ${idx === 0 ? 'active' : ''}" data-index="${idx}">
                    `).join('')}

                    <!-- Particle Light Sweep Canvas -->
                    <canvas class="video-canvas-overlay" id="videoCanvasOverlay"></canvas>

                    <!-- Cinematic Vignette & Scanlines -->
                    <div class="video-vignette-overlay"></div>

                    <!-- Tech HUD Crosshair Corners -->
                    <div class="video-hud-corner video-hud-tl"></div>
                    <div class="video-hud-corner video-hud-tr"></div>
                    <div class="video-hud-corner video-hud-bl"></div>
                    <div class="video-hud-corner video-hud-br"></div>

                    <!-- TOP HUD BAR -->
                    <div class="video-top-hud">
                        <div style="display: flex; align-items: center; gap: 0.75rem;">
                            <div class="video-rec-badge">
                                <div class="video-rec-dot"></div>
                                <span>REC</span>
                            </div>
                            <span class="video-quality-tag">4K HDR • 60 FPS</span>
                        </div>

                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <div class="video-eq-container" id="videoEqContainer" style="opacity: 0.4;">
                                <div class="video-eq-bar"></div>
                                <div class="video-eq-bar"></div>
                                <div class="video-eq-bar"></div>
                                <div class="video-eq-bar"></div>
                                <div class="video-eq-bar"></div>
                            </div>
                            <div class="video-timecode" id="videoTimecode">00:00:00</div>
                        </div>
                    </div>

                    <!-- CENTER PLAY OVERLAY -->
                    <div class="video-center-overlay" id="videoCenterOverlay">
                        <button class="video-play-btn-large" id="videoBigPlayBtn" aria-label="Play Video Trailer">
                            <i class="fa-solid fa-play" style="margin-left: 4px;" id="videoBigPlayIcon"></i>
                        </button>
                        <div class="video-play-title" id="videoSceneTitle">${SCENES[0].title}</div>
                        <div class="video-play-subtitle" id="videoSceneDesc">${SCENES[0].desc}</div>
                    </div>

                    <!-- BOTTOM HUD CONTROLS -->
                    <div class="video-bottom-hud">
                        <!-- TIMELINE PROGRESS BAR -->
                        <div class="video-progress-wrapper" id="videoProgressWrapper" title="Click to seek scene">
                            <div class="video-progress-bar" id="videoProgressBar"></div>
                        </div>

                        <!-- SUBTITLE CAPTION BOX -->
                        <div class="video-caption-box">
                            <i class="fa-solid fa-closed-captioning video-caption-icon"></i>
                            <div class="video-caption-text" id="videoCaptionText"></div>
                        </div>

                        <!-- CONTROLS & SCENE PILLS -->
                        <div class="video-controls-row">
                            <div class="video-btn-group">
                                <button class="video-ctrl-btn" id="videoPlayPauseBtn" title="Play / Pause">
                                    <i class="fa-solid fa-pause" id="videoPlayPauseIcon"></i>
                                    <span id="videoPlayPauseLabel">Pause</span>
                                </button>
                                <button class="video-ctrl-btn" id="videoPrevBtn" title="Previous Scene">
                                    <i class="fa-solid fa-backward-step"></i>
                                </button>
                                <button class="video-ctrl-btn" id="videoNextBtn" title="Next Scene">
                                    <i class="fa-solid fa-forward-step"></i>
                                </button>
                                <button class="video-ctrl-btn" id="videoAudioBtn" title="Toggle Cinematic Soundtrack">
                                    <i class="fa-solid fa-volume-xmark" id="videoAudioIcon"></i>
                                    <span id="videoAudioLabel">Mute</span>
                                </button>
                                <button class="video-ctrl-btn" id="videoFullscreenBtn" title="Fullscreen Theater Mode">
                                    <i class="fa-solid fa-expand"></i>
                                </button>
                            </div>

                            <div class="video-scene-pills" id="videoScenePills">
                                ${SCENES.map((scene, idx) => `
                                    <button class="video-pill ${idx === 0 ? 'active' : ''}" data-index="${idx}">
                                        ${scene.tag}
                                    </button>
                                `).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- FULLSCREEN THEATER MODAL -->
            <div class="video-theater-modal" id="videoTheaterModal">
                <button class="video-theater-close" id="videoTheaterCloseBtn"><i class="fa-solid fa-xmark"></i></button>
                <div style="flex: 1; display: flex; align-items: center; justify-content: center; position: relative;">
                    <img src="${SCENES[0].image}" id="theaterBgImage" style="max-width: 92vw; max-height: 80vh; object-fit: contain; border-radius: 16px; border: 1px solid var(--gold-primary); box-shadow: 0 0 50px rgba(212,175,55,0.4);">
                </div>
                <div style="padding: 1.5rem; background: rgba(5,7,12,0.95); text-align: center; border-top: 1px solid var(--border-color);">
                    <h2 id="theaterTitle" style="font-family: 'Cinzel', serif; color: var(--gold-primary); margin-bottom: 0.5rem;">${SCENES[0].title}</h2>
                    <p id="theaterDesc" style="color: var(--text-muted); font-size: 0.95rem;">${SCENES[0].caption}</p>
                </div>
            </div>
        `;

        setupCanvasParticles();
        setupEventListeners();
        startPlaybackLoop();
        typeWriterCaption(SCENES[0].caption);
    }

    function setupEventListeners() {
        const playPauseBtn = document.getElementById('videoPlayPauseBtn');
        const bigPlayBtn = document.getElementById('videoBigPlayBtn');
        const prevBtn = document.getElementById('videoPrevBtn');
        const nextBtn = document.getElementById('videoNextBtn');
        const audioBtn = document.getElementById('videoAudioBtn');
        const fullscreenBtn = document.getElementById('videoFullscreenBtn');
        const progressWrapper = document.getElementById('videoProgressWrapper');
        const pillsContainer = document.getElementById('videoScenePills');
        const theaterCloseBtn = document.getElementById('videoTheaterCloseBtn');

        if (playPauseBtn) playPauseBtn.addEventListener('click', togglePlayPause);
        if (bigPlayBtn) bigPlayBtn.addEventListener('click', togglePlayPause);
        if (prevBtn) prevBtn.addEventListener('click', prevScene);
        if (nextBtn) nextBtn.addEventListener('click', nextScene);
        if (audioBtn) audioBtn.addEventListener('click', toggleAudio);
        if (fullscreenBtn) fullscreenBtn.addEventListener('click', openTheaterModal);
        if (theaterCloseBtn) theaterCloseBtn.addEventListener('click', closeTheaterModal);

        if (pillsContainer) {
            pillsContainer.addEventListener('click', (e) => {
                const pill = e.target.closest('.video-pill');
                if (pill) {
                    const idx = parseInt(pill.getAttribute('data-index'), 10);
                    switchScene(idx);
                }
            });
        }

        if (progressWrapper) {
            progressWrapper.addEventListener('click', (e) => {
                const rect = progressWrapper.getBoundingClientRect();
                const clickX = e.clientX - rect.left;
                const ratio = clickX / rect.width;
                const targetIdx = Math.floor(ratio * SCENES.length);
                switchScene(Math.min(targetIdx, SCENES.length - 1));
            });
        }
    }

    function switchScene(index) {
        currentSceneIndex = index;
        progressPercent = 0;

        // Update Background Images
        const bgImages = document.querySelectorAll('.video-scene-bg');
        bgImages.forEach((img, i) => {
            if (i === index) {
                img.classList.add('active');
            } else {
                img.classList.remove('active');
            }
        });

        // Update Scene Pills
        const pills = document.querySelectorAll('.video-pill');
        pills.forEach((pill, i) => {
            if (i === index) {
                pill.classList.add('active');
            } else {
                pill.classList.remove('active');
            }
        });

        // Update Title and Subtitles
        const titleEl = document.getElementById('videoSceneTitle');
        const descEl = document.getElementById('videoSceneDesc');
        const theaterBg = document.getElementById('theaterBgImage');
        const theaterTitle = document.getElementById('theaterTitle');
        const theaterDesc = document.getElementById('theaterDesc');

        if (titleEl) titleEl.textContent = SCENES[index].title;
        if (descEl) descEl.textContent = SCENES[index].desc;
        if (theaterBg) theaterBg.src = SCENES[index].image;
        if (theaterTitle) theaterTitle.textContent = SCENES[index].title;
        if (theaterDesc) theaterDesc.textContent = SCENES[index].caption;

        typeWriterCaption(SCENES[index].caption);

        // Sound tone update if audio enabled
        if (!isMuted && audioCtx) {
            playUiBeep(440 + index * 110);
        }
    }

    function nextScene() {
        const nextIdx = (currentSceneIndex + 1) % SCENES.length;
        switchScene(nextIdx);
    }

    function prevScene() {
        const prevIdx = (currentSceneIndex - 1 + SCENES.length) % SCENES.length;
        switchScene(prevIdx);
    }

    function togglePlayPause() {
        isPlaying = !isPlaying;
        const icon = document.getElementById('videoPlayPauseIcon');
        const label = document.getElementById('videoPlayPauseLabel');
        const bigIcon = document.getElementById('videoBigPlayIcon');
        const centerOverlay = document.getElementById('videoCenterOverlay');

        if (isPlaying) {
            if (icon) icon.className = 'fa-solid fa-pause';
            if (label) label.textContent = 'Pause';
            if (bigIcon) bigIcon.className = 'fa-solid fa-pause';
            if (centerOverlay) centerOverlay.classList.add('playing');
        } else {
            if (icon) icon.className = 'fa-solid fa-play';
            if (label) label.textContent = 'Play';
            if (bigIcon) bigIcon.className = 'fa-solid fa-play';
            if (centerOverlay) centerOverlay.classList.remove('playing');
        }
    }

    function startPlaybackLoop() {
        let totalSeconds = 0;
        setInterval(() => {
            if (!isPlaying) return;

            progressPercent += 1.66; // 6 seconds total per scene
            if (progressPercent >= 100) {
                progressPercent = 0;
                nextScene();
            }

            const progressBar = document.getElementById('videoProgressBar');
            if (progressBar) {
                const totalProgress = ((currentSceneIndex * 100) + progressPercent) / SCENES.length;
                progressBar.style.width = `${totalProgress}%`;
            }

            totalSeconds += 0.1;
            const timecodeEl = document.getElementById('videoTimecode');
            if (timecodeEl) {
                const mins = String(Math.floor(totalSeconds / 60)).padStart(2, '0');
                const secs = String(Math.floor(totalSeconds % 60)).padStart(2, '0');
                const ms = String(Math.floor((totalSeconds % 1) * 100)).padStart(2, '0');
                timecodeEl.textContent = `00:${mins}:${secs}`;
            }
        }, 100);
    }

    function typeWriterCaption(text) {
        const captionEl = document.getElementById('videoCaptionText');
        if (!captionEl) return;

        if (typeWriterTimer) clearInterval(typeWriterTimer);

        captionEl.textContent = '';
        let i = 0;
        typeWriterTimer = setInterval(() => {
            if (i < text.length) {
                captionEl.textContent += text.charAt(i);
                i++;
            } else {
                clearInterval(typeWriterTimer);
            }
        }, 22);
    }

    function toggleAudio() {
        isMuted = !isMuted;
        const icon = document.getElementById('videoAudioIcon');
        const label = document.getElementById('videoAudioLabel');
        const eq = document.getElementById('videoEqContainer');

        if (!isMuted) {
            if (icon) icon.className = 'fa-solid fa-volume-high';
            if (label) label.textContent = 'Sound ON';
            if (eq) eq.style.opacity = '1';
            initAudioSynth();
        } else {
            if (icon) icon.className = 'fa-solid fa-volume-xmark';
            if (label) label.textContent = 'Mute';
            if (eq) eq.style.opacity = '0.4';
            stopAudioSynth();
        }
    }

    function initAudioSynth() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!audioCtx) audioCtx = new AudioContext();

            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }

            oscillator = audioCtx.createOscillator();
            gainNode = audioCtx.createGain();

            oscillator.type = 'sine';
            oscillator.frequency.setValueAtTime(120, audioCtx.currentTime); // Low cinematic pad
            gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime);

            oscillator.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            oscillator.start();
        } catch(e) {
            console.log('Audio Synth Error:', e);
        }
    }

    function stopAudioSynth() {
        if (oscillator) {
            try {
                oscillator.stop();
                oscillator.disconnect();
            } catch(e){}
        }
    }

    function playUiBeep(freq) {
        try {
            if (!audioCtx) return;
            const beepOsc = audioCtx.createOscillator();
            const beepGain = audioCtx.createGain();
            beepOsc.type = 'triangle';
            beepOsc.frequency.setValueAtTime(freq, audioCtx.currentTime);
            beepGain.gain.setValueAtTime(0.08, audioCtx.currentTime);
            beepGain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.25);
            beepOsc.connect(beepGain);
            beepGain.connect(audioCtx.destination);
            beepOsc.start();
            beepOsc.stop(audioCtx.currentTime + 0.25);
        } catch(e){}
    }

    function openTheaterModal() {
        const modal = document.getElementById('videoTheaterModal');
        if (modal) modal.classList.add('active');
    }

    function closeTheaterModal() {
        const modal = document.getElementById('videoTheaterModal');
        if (modal) modal.classList.remove('active');
    }

    function setupCanvasParticles() {
        const canvas = document.getElementById('videoCanvasOverlay');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        resize();
        window.addEventListener('resize', resize);

        const particles = Array.from({ length: 30 }, () => ({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 2 + 0.5,
            speedX: (Math.random() - 0.5) * 0.5,
            speedY: -Math.random() * 0.8 - 0.2,
            alpha: Math.random() * 0.6 + 0.2
        }));

        let flareX = 0;

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Light Dust Particles
            particles.forEach(p => {
                p.x += p.speedX;
                p.y += p.speedY;
                if (p.y < 0) p.y = canvas.height;
                if (p.x < 0) p.x = canvas.width;
                if (p.x > canvas.width) p.x = 0;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(252, 246, 186, ${p.alpha})`;
                ctx.fill();
            });

            // Cinematic Horizon Sweep Line
            flareX = (flareX + 1.5) % (canvas.width * 2);
            if (flareX < canvas.width) {
                const grad = ctx.createLinearGradient(flareX - 100, 0, flareX + 100, 0);
                grad.addColorStop(0, 'rgba(212, 175, 55, 0)');
                grad.addColorStop(0.5, 'rgba(212, 175, 55, 0.15)');
                grad.addColorStop(1, 'rgba(212, 175, 55, 0)');
                ctx.fillStyle = grad;
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }

            requestAnimationFrame(animate);
        }
        animate();
    }

    // Auto Init on DOM Load
    document.addEventListener('DOMContentLoaded', () => {
        const mountEl = document.getElementById('videoIntroMount');
        if (mountEl) {
            renderVideoIntroHTML(mountEl);
        }
    });

})();
