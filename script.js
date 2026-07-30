document.addEventListener('DOMContentLoaded', () => {

    // ─── Utility: throttle ────────────────────────────────────────────────────
    const throttle = (fn, ms) => {
        let last = 0;
        return (...args) => {
            const now = Date.now();
            if (now - last >= ms) { last = now; fn(...args); }
        };
    };

    // ─── Utility: debounce ───────────────────────────────────────────────────
    const debounce = (fn, ms) => {
        let t;
        return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
    };

    // =========================================================================
    // 1. Mobile Menu Toggle
    // =========================================================================
    const menuBtn = document.getElementById('menu-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (menuBtn && navMenu) {
        menuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            menuBtn.classList.toggle('active');

            const spans = menuBtn.querySelectorAll('span');
            if (menuBtn.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(7px, -7px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }

    // =========================================================================
    // 2. Navbar Scroll Effect — throttled
    // =========================================================================
    const navbar = document.getElementById('main-nav');
    if (navbar) {
        const isHomePage = document.body.classList.contains('home-page');
        const heroSection = document.querySelector('.hero-section');
        let ticked = false;
        const handleNavScroll = throttle(() => {
            if (!ticked) {
                requestAnimationFrame(() => {
                    const triggerHeight = isHomePage && heroSection 
                        ? (heroSection.offsetHeight - navbar.offsetHeight - 24) 
                        : 50;
                    navbar.classList.toggle('scrolled', window.scrollY > triggerHeight);
                    ticked = false;
                });
                ticked = true;
            }
        }, 80);
        window.addEventListener('scroll', handleNavScroll, { passive: true });
        handleNavScroll();
    }

    // =========================================================================
    // 3. Scroll Reveal — IntersectionObserver (replaces scroll-event polling)
    // =========================================================================
    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });

        revealElements.forEach(el => revealObserver.observe(el));
    }

    // ─── 3b. Staggered Experience Card Reveal ────────────────────────────────
    const experienceCards = document.querySelectorAll('.experience-card');
    if (experienceCards.length > 0) {
        const cardObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('card-revealed');
                    cardObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        experienceCards.forEach(card => cardObserver.observe(card));
    }

    // ─── 3c. Handcrafted Why Moon Island Card Tilt Interaction ───────────────
    const interactiveCards = document.querySelectorAll('.why-card, .about-exp-card, .timeline-node');
    if (interactiveCards.length > 0) {
        interactiveCards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                if (window.innerWidth < 768) return;
                card.style.willChange = 'transform';
            });

            card.addEventListener('mousemove', (e) => {
                if (window.innerWidth < 768) return;
                const rect = card.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                const mouseX = e.clientX - centerX;
                const mouseY = e.clientY - centerY;

                // Max 2 deg rotation on X and Y axes
                const rotateX = (-mouseY / (rect.height / 2)) * 2;
                const rotateY = (mouseX / (rect.width / 2)) * 2;

                card.style.transform = `perspective(1000px) translateY(-10px) scale(1.02) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = '';
                card.style.willChange = '';
            });
        });
    }

    // =========================================================================
    // 4. Cinematic Night Background Parallax & Scroll-Zoom Loop
    // =========================================================================
    let targetX = 0;
    let targetY = 0;
    let currentX = 0;
    let currentY = 0;
    const ease = 0.07; // Smooth LERP easing factor

    let scrollPercent = 0;
    let targetScale = 1.15; // Increased default size by 15% (1.15 base scale)
    let currentScale = 1.15;

    const isMobileDevice = window.innerWidth < 1024 || ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

    const updateScrollState = () => {
        if (isMobileDevice) return;
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        scrollPercent = docHeight > 0 ? scrollTop / docHeight : 0;
        targetScale = 1.15 + scrollPercent * 0.28; // Obvious zoom range 1.15 to 1.43
    };

    if (!isMobileDevice) {
        window.addEventListener('scroll', updateScrollState, { passive: true });
        updateScrollState();

        document.addEventListener('mousemove', (e) => {
            // Magnetic cursor displacement range -40px to 40px
            targetX = ((e.clientX / window.innerWidth) - 0.5) * 80;
            targetY = ((e.clientY / window.innerHeight) - 0.5) * 80;
        }, { passive: true });
    }

    let floatAngleX = 0;
    let floatAngleY = 0;
    const desktopMoonBg = document.querySelector('.desktop-moon-bg');
    const cloudsContainer = document.querySelector('.clouds-container');
    
    // Lazy loaded depth elements for mouse-follow
    let starsL1 = null;
    let starsL2 = null;
    let starsL3 = null;
    let starsL4 = null;
    let starsL5 = null;
    let nebulaMist = null;
    let spaceDust = null;
    let fogLayer = null;

    let rafId = null;
    let isTabVisible = true;

    const updateBackgroundParallax = () => {
        if (isMobileDevice || !isTabVisible) {
            rafId = null;
            return;
        }

        // LERP mouse tracking coordinates
        currentX += (targetX - currentX) * ease;
        currentY += (targetY - currentY) * ease;

        // LERP scroll scale zoom
        currentScale += (targetScale - currentScale) * ease;

        // Eased 3D tilt rotations based on cursor offset
        const tiltX = currentY * 0.15;
        const tiltY = -currentX * 0.15;

        // Slow circular floats (amplitude 15px = 30px floating offset)
        floatAngleX += 0.008;
        floatAngleY += 0.011;
        const floatX = Math.cos(floatAngleX) * 15;
        const floatY = Math.sin(floatAngleY) * 15;
        const floatRot = Math.cos(floatAngleY * 0.5) * 1.5;

        // 1. Moon cursor parallax, floating translation, 3D tilts, scaling zoom, and slow rotation
        if (desktopMoonBg) {
            desktopMoonBg.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translate3d(${currentX + floatX}px, ${currentY + floatY}px, 0) scale(${currentScale}) rotate(${floatRot}deg)`;
        }

        // 2. 5 Nested Stars Layers Parallax (shifting in the opposite direction for parallax depth)
        if (!starsL1) starsL1 = document.querySelector('.stars-layer-1-wrap');
        if (!starsL2) starsL2 = document.querySelector('.stars-layer-2-wrap');
        if (!starsL3) starsL3 = document.querySelector('.stars-layer-3-wrap');
        if (!starsL4) starsL4 = document.querySelector('.stars-layer-4-wrap');
        if (!starsL5) starsL5 = document.querySelector('.stars-layer-5-wrap');

        if (starsL1) starsL1.style.transform = `translate3d(${currentX * -0.1}px, ${currentY * -0.1}px, 0)`;
        if (starsL2) starsL2.style.transform = `translate3d(${currentX * -0.25}px, ${currentY * -0.25}px, 0)`;
        if (starsL3) starsL3.style.transform = `translate3d(${currentX * -0.45}px, ${currentY * -0.45}px, 0)`;
        if (starsL4) starsL4.style.transform = `translate3d(${currentX * -0.65}px, ${currentY * -0.65}px, 0)`;
        if (starsL5) starsL5.style.transform = `translate3d(${currentX * -0.9}px, ${currentY * -0.9}px, 0)`;

        // 3. Nebula Layer
        if (!nebulaMist) nebulaMist = document.querySelector('.nebula-mist');
        if (nebulaMist) {
            nebulaMist.style.transform = `translate3d(${currentX * -0.2}px, ${currentY * -0.2}px, 0)`;
        }

        // 4. Foreground / Clouds
        if (cloudsContainer) {
            cloudsContainer.style.transform = `translate3d(${currentX * 0.6}px, ${currentY * 0.6}px, 0)`;
        }
        if (!spaceDust) spaceDust = document.querySelector('.space-dust-container');
        if (spaceDust) {
            spaceDust.style.transform = `translate3d(${currentX * -0.5}px, ${currentY * -0.5}px, 0)`;
        }
        if (!fogLayer) fogLayer = document.querySelector('.fog-layer');
        if (fogLayer) {
            fogLayer.style.transform = `translate3d(${currentX * -0.3}px, ${currentY * -0.3}px, 0)`;
        }

        rafId = requestAnimationFrame(updateBackgroundParallax);
    };

    // Toggle animations based on tab visibility
    document.addEventListener('visibilitychange', () => {
        isTabVisible = (document.visibilityState === 'visible');
        if (isTabVisible && !rafId && !isMobileDevice) {
            rafId = requestAnimationFrame(updateBackgroundParallax);
        }
    });

    if (!isMobileDevice) {
        rafId = requestAnimationFrame(updateBackgroundParallax);
    }

    // =========================================================================
    // 6. Hero Background Video — robust autoplay
    // =========================================================================
    const heroVideo = document.querySelector('.hero-bg-video');
    if (heroVideo) {
        heroVideo.muted = true;
        const tryPlay = () => heroVideo.play().catch(() => {});
        tryPlay();
        heroVideo.addEventListener('canplaythrough', tryPlay, { once: true });

        // Pause video when it scrolls out of view to save CPU
        if ('IntersectionObserver' in window) {
            const videoObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) { heroVideo.play().catch(() => {}); }
                    else { heroVideo.pause(); }
                });
            }, { threshold: 0.1 });
            videoObserver.observe(heroVideo);
        }
    }

    // =========================================================================
    // 7. Mobile flip cards (close others on tap)
    // =========================================================================
    const experiences = document.querySelectorAll('.experience-card');
    experiences.forEach(card => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('a') || e.target.closest('button')) return;
            card.classList.toggle('flipped');
            experiences.forEach(other => {
                if (other !== card) other.classList.remove('flipped');
            });
        });
    });

    // =========================================================================
    // 8. Smooth Scroll for anchor links
    // =========================================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) target.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // =========================================================================
    // 9. Lazy-load images below the fold using IntersectionObserver
    // =========================================================================
    const lazyImgs = document.querySelectorAll('img[data-src]');
    if (lazyImgs.length > 0) {
        const imgObserver = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    if (img.dataset.srcset) img.srcset = img.dataset.srcset;
                    img.removeAttribute('data-src');
                    obs.unobserve(img);
                }
            });
        }, { rootMargin: '200px 0px' });
        lazyImgs.forEach(img => imgObserver.observe(img));
    }

    // =========================================================================
    // 10. Gallery Carousel — Services page only
    // =========================================================================
    const galleryTrack = document.getElementById('gallery-track');
    const galleryPrev = document.getElementById('gallery-prev');
    const galleryNext = document.getElementById('gallery-next');
    const galleryIndicators = document.getElementById('gallery-indicators');

    if (galleryTrack) {
        const cards = Array.from(galleryTrack.children);
        const totalCards = cards.length;
        let currentIndex = 0;
        let visibleCards = 3;
        let gap = 32;
        let autoPlayInterval = null;

        const updateLayoutVars = () => {
            const w = window.innerWidth;
            if (w <= 768)  { visibleCards = 1; gap = 0; }
            else if (w <= 1024) { visibleCards = 2; gap = 16; }
            else           { visibleCards = 3; gap = 32; }
        };

        const renderIndicators = () => {
            if (!galleryIndicators) return;
            galleryIndicators.innerHTML = '';
            const totalDots = Math.max(1, totalCards - visibleCards + 1);
            for (let i = 0; i < totalDots; i++) {
                const dot = document.createElement('div');
                dot.classList.add('moon-dot');
                if (i === 0) dot.classList.add('active');
                dot.addEventListener('click', () => { goToSlide(i); resetAutoPlay(); });
                galleryIndicators.appendChild(dot);
            }
        };

        const updateTrackPosition = () => {
            if (!cards[0]) return;
            const cardWidth = cards[0].offsetWidth;
            const offset = currentIndex * (cardWidth + gap);
            galleryTrack.style.transform = `translate3d(-${offset}px, 0, 0)`;
            if (!galleryIndicators) return;
            galleryIndicators.querySelectorAll('.moon-dot').forEach((dot, i) => {
                dot.classList.toggle('active', i === currentIndex);
            });
        };

        const goToSlide = (index) => {
            currentIndex = Math.min(Math.max(index, 0), totalCards - visibleCards);
            updateTrackPosition();
        };

        const slideNext = () => {
            currentIndex = currentIndex >= (totalCards - visibleCards) ? 0 : currentIndex + 1;
            updateTrackPosition();
        };

        const slidePrev = () => {
            currentIndex = currentIndex <= 0 ? totalCards - visibleCards : currentIndex - 1;
            updateTrackPosition();
        };

        const startAutoPlay = () => {
            if (autoPlayInterval) clearInterval(autoPlayInterval);
            autoPlayInterval = setInterval(slideNext, 4500);
        };

        const resetAutoPlay = () => startAutoPlay();

        if (galleryPrev) galleryPrev.addEventListener('click', () => { slidePrev(); resetAutoPlay(); });
        if (galleryNext) galleryNext.addEventListener('click', () => { slideNext(); resetAutoPlay(); });

        // Pause on hover
        galleryTrack.addEventListener('mouseenter', () => { if (autoPlayInterval) clearInterval(autoPlayInterval); });
        galleryTrack.addEventListener('mouseleave', startAutoPlay);

        // Pause when gallery is off-screen (save CPU)
        const gallerySection = galleryTrack.closest('section');
        if (gallerySection && 'IntersectionObserver' in window) {
            const galleryObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) { startAutoPlay(); }
                    else { if (autoPlayInterval) clearInterval(autoPlayInterval); }
                });
            }, { threshold: 0.1 });
            galleryObserver.observe(gallerySection);
        } else {
            startAutoPlay();
        }

        // Initialise
        updateLayoutVars();
        renderIndicators();

        window.addEventListener('resize', debounce(() => {
            updateLayoutVars();
            renderIndicators();
            currentIndex = Math.min(currentIndex, totalCards - visibleCards);
            updateTrackPosition();
        }, 200));

        // Gallery background star particles
        const starsLayer = document.getElementById('gallery-stars');
        if (starsLayer) {
            const frag = document.createDocumentFragment();
            for (let i = 0; i < 20; i++) {
                const p = document.createElement('div');
                p.classList.add('floating-star-particle');
                p.style.cssText = [
                    `left:${Math.random() * 100}%`,
                    `top:${Math.random() * 100}%`,
                    `--tx:${(Math.random() - 0.5) * 50}px`,
                    `--ty:${-25 - Math.random() * 45}px`,
                    `--op:${0.2 + Math.random() * 0.45}`,
                    `--dur:${9 + Math.random() * 11}s`,
                    `animation-delay:${Math.random() * -14}s`
                ].join(';');
                frag.appendChild(p);
            }
            starsLayer.appendChild(frag);
        }
    }

    // =========================================================================
    // Cinematic Background System (Nebula, Moon elements, dynamic stars, comets, dust, fireflies)
    // =========================================================================
    const bgWrapper = document.querySelector('.cinematic-bg-wrapper');
    if (bgWrapper) {
        // 1. Nebula Mist Layer (faint static gradient cloud)
        if (!document.querySelector('.nebula-mist')) {
            const nebula = document.createElement('div');
            nebula.className = 'nebula-mist';
            bgWrapper.insertBefore(nebula, bgWrapper.firstChild);
        }

        // 2. Setup Desktop Moon Wrapper, Moonlight Rays & Glowing Auras
        const desktopMoon = document.querySelector('.desktop-moon-bg');
        if (desktopMoon && !document.querySelector('.desktop-moon-inner')) {
            desktopMoon.innerHTML = `
                <div class="moon-aura-pulse"></div>
                <div class="moon-light-rays"></div>
                <div class="moon-edge-scatter"></div>
                <div class="desktop-moon-inner"></div>
            `;
        }

        // 3. Setup Mobile Moon Auras
        const mobileMoonInner = document.querySelector('.mobile-moon-inner');
        if (mobileMoonInner && !document.querySelector('.mobile-moon-aura')) {
            const mobileMoonBg = document.querySelector('.mobile-moon-bg');
            if (mobileMoonBg) {
                const aura = document.createElement('div');
                aura.className = 'mobile-moon-aura';
                mobileMoonBg.insertBefore(aura, mobileMoonInner);
            }
        }

        // 4. Generate stars distributed across 5 separate layers (twinkling and drifting)
        const starsContainer = document.querySelector('.stars-container');
        if (starsContainer) {
            starsContainer.innerHTML = ''; // clear static layers
            
            const starCount = isMobileDevice ? 80 : 320; // Drastically reduce mobile nodes
            const layers = [];
            for (let l = 1; l <= 5; l++) {
                const wrap = document.createElement('div');
                wrap.className = `stars-layer-${l}-wrap`;
                const inner = document.createElement('div');
                inner.className = `stars-layer-${l}-inner`;
                wrap.appendChild(inner);
                starsContainer.appendChild(wrap);
                layers.push(inner);
            }
            
            const frags = Array.from({ length: 5 }, () => document.createDocumentFragment());
            for (let i = 0; i < starCount; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                
                const layerIdx = i % 5;
                let size = 0.8;
                if (layerIdx === 0) size = 0.8;
                else if (layerIdx === 1) size = 1.2;
                else if (layerIdx === 2) size = 1.6;
                else if (layerIdx === 3) size = 2.0;
                else size = 2.5;
                
                star.style.width = `${size}px`;
                star.style.height = `${size}px`;
                star.style.top = `${Math.random() * 100}%`;
                star.style.left = `${Math.random() * 100}%`;
                star.style.animationDelay = `${Math.random() * 4}s`;
                star.style.animationDuration = `${1.5 + Math.random() * 2.5}s`;
                
                frags[layerIdx].appendChild(star);
            }
            
            for (let l = 0; l < 5; l++) {
                layers[l].appendChild(frags[l]);
            }
        }

        // 4b. Generate glowing star clusters (4 clusters on desktop, 1 on mobile)
        if (starsContainer) {
            const clusterCount = isMobileDevice ? 1 : 4;
            for (let i = 0; i < clusterCount; i++) {
                const cluster = document.createElement('div');
                cluster.className = 'star-cluster';
                cluster.style.top = `${15 + Math.random() * 50}%`;
                cluster.style.left = `${10 + Math.random() * 80}%`;
                starsContainer.appendChild(cluster);
            }
        }

        // 5. Generate slowly flying comets (4 comets on desktop, 0 on mobile)
        if (!document.querySelector('.stars-layer-comets')) {
            const cometsLayer = document.createElement('div');
            cometsLayer.className = 'stars-layer-comets';
            starsContainer.appendChild(cometsLayer);
            
            const cometCount = isMobileDevice ? 0 : 4;
            for (let i = 0; i < cometCount; i++) {
                const comet = document.createElement('div');
                comet.className = 'flying-comet';
                comet.style.top = `${10 + Math.random() * 40}%`;
                comet.style.animationDelay = `${i * 9}s`;
                cometsLayer.appendChild(comet);
            }
        }

        // 6. Generate fireflies floating around (20 on desktop, 6 on mobile)
        if (!document.querySelector('.fireflies-container')) {
            const firefliesContainer = document.createElement('div');
            firefliesContainer.className = 'fireflies-container';
            bgWrapper.appendChild(firefliesContainer);
            
            const fireflyCount = isMobileDevice ? 6 : 20;
            const frag = document.createDocumentFragment();
            for (let i = 0; i < fireflyCount; i++) {
                const ff = document.createElement('div');
                ff.className = 'firefly';
                ff.style.top = `${20 + Math.random() * 70}%`;
                ff.style.left = `${Math.random() * 100}%`;
                ff.style.animationDelay = `${Math.random() * -15}s`;
                ff.style.animationDuration = `${12 + Math.random() * 8}s`;
                frag.appendChild(ff);
            }
            firefliesContainer.appendChild(frag);
        }

        // 7. Generate cosmic dust particles (30 on desktop, 10 on mobile)
        if (!document.querySelector('.space-dust-container')) {
            const dustContainer = document.createElement('div');
            dustContainer.className = 'space-dust-container';
            bgWrapper.appendChild(dustContainer);
            
            const dustCount = isMobileDevice ? 10 : 30;
            const frag = document.createDocumentFragment();
            for (let i = 0; i < dustCount; i++) {
                const dust = document.createElement('div');
                dust.className = 'space-dust-particle';
                const size = Math.random() * 3 + 1.5;
                dust.style.width = `${size}px`;
                dust.style.height = `${size}px`;
                dust.style.top = `${Math.random() * 100}%`;
                dust.style.left = `${Math.random() * 100}%`;
                
                const angle = Math.random() * Math.PI * 2;
                const driftX = Math.cos(angle) * (Math.random() * 60 + 40);
                const driftY = Math.sin(angle) * (Math.random() * 60 + 40);
                
                dust.style.setProperty('--drift-x', `${driftX}px`);
                dust.style.setProperty('--drift-y', `${driftY}px`);
                dust.style.animation = `dustFade ${Math.random() * 5 + 5}s infinite ease-in-out alternate`;
                frag.appendChild(dust);
            }
            dustContainer.appendChild(frag);
        }

        // 8. Setup Faint Moving Fog Layer (multiple layers for depth)
        if (!document.querySelector('.fog-layer')) {
            const fog = document.createElement('div');
            fog.className = 'fog-layer';
            bgWrapper.appendChild(fog);
        }

        // 10. Cursor Trailer Emitter (Disable on touch screens)
        const createCursorInteractions = () => {
            if (isMobileDevice) return;
            let lastSpawn = 0;
            
            document.addEventListener('mousemove', (e) => {
                const now = performance.now();
                
                // 1. Trail Particles
                if (now - lastSpawn > 35) {
                     lastSpawn = now;
                     const particle = document.createElement('div');
                     particle.className = 'cursor-trail-particle';
                     particle.style.left = `${e.clientX}px`;
                     particle.style.top = `${e.clientY}px`;
                     
                     const offset = (Math.random() - 0.5) * 12;
                     particle.style.setProperty('--dx', `${offset}px`);
                     
                     bgWrapper.appendChild(particle);
                     setTimeout(() => particle.remove(), 800);
                }
            }, { passive: true });
        };
        createCursorInteractions();
    }

    // =========================================================================
    // 11. Services Page animations: 3D Mouse Tilt, Lift, Hover Scale & Scroll Parallax
    // =========================================================================
    const serviceRows = document.querySelectorAll('.service-section-row');
    if (serviceRows.length > 0) {
        const parallaxTargets = document.querySelectorAll('.service-image-container.parallax-target');
        const imageCols = document.querySelectorAll('.service-image-col');
        
        // ─── A. Mouse Approach Follow & 3D Tilt ──────────────────────────────
        imageCols.forEach(col => {
            const container = col.querySelector('.service-image-container');
            const tiltEl = col.querySelector('.service-image-tilt');
            if (!container || !tiltEl) return;
            
            let isHovered = false;
            let targetTiltX = 0;
            let targetTiltY = 0;
            let targetFollowX = 0;
            let targetFollowY = 0;
            
            let currentTiltX = 0;
            let currentTiltY = 0;
            let currentFollowX = 0;
            let currentFollowY = 0;
            
            const ease = 0.08; // Smooth LERP easing factor
            let localRafId = null;
            
            const animateTilt = () => {
                currentTiltX += (targetTiltX - currentTiltX) * ease;
                currentTiltY += (targetTiltY - currentTiltY) * ease;
                currentFollowX += (targetFollowX - currentFollowX) * ease;
                currentFollowY += (targetFollowY - currentFollowY) * ease;
                
                if (window.innerWidth > 991) {
                    const scale = isHovered ? 1.08 : 1.0;
                    const lift = isHovered ? -15 : 0;
                    tiltEl.style.transform = `perspective(1000px) rotateX(${currentTiltX}deg) rotateY(${currentTiltY}deg) translate3d(${currentFollowX}px, ${lift + currentFollowY}px, 0) scale(${scale})`;
                } else {
                    tiltEl.style.transform = '';
                }
                
                // Stop the RAF loop if the tilt settles to rest
                const diff = Math.abs(targetTiltX - currentTiltX) + 
                             Math.abs(targetTiltY - currentTiltY) + 
                             Math.abs(targetFollowX - currentFollowX) + 
                             Math.abs(targetFollowY - currentFollowY);
                             
                if (isHovered || diff > 0.01) {
                    localRafId = requestAnimationFrame(animateTilt);
                } else {
                    localRafId = null;
                    tiltEl.style.willChange = '';
                }
            };
            
            col.addEventListener('mousemove', (e) => {
                if (window.innerWidth <= 991) return; // Skip on mobile
                
                const rect = container.getBoundingClientRect();
                const containerCenterX = rect.left + rect.width / 2;
                const containerCenterY = rect.top + rect.height / 2;
                
                const dx = e.clientX - containerCenterX;
                const dy = e.clientY - containerCenterY;
                
                const detectionRadius = 300;
                const distance = Math.hypot(dx, dy);
                
                if (distance < detectionRadius) {
                    const factor = (detectionRadius - distance) / detectionRadius; // 1 at center, 0 at boundary
                    
                    // Slightly follow cursor: Max movement 20px
                    targetFollowX = (dx / detectionRadius) * 20 * factor;
                    targetFollowY = (dy / detectionRadius) * 20 * factor;
                    
                    // 3D Tilt: Max 5deg
                    targetTiltX = -(dy / detectionRadius) * 5 * factor;
                    targetTiltY = (dx / detectionRadius) * 5 * factor;
                } else {
                    targetFollowX = 0;
                    targetFollowY = 0;
                    targetTiltX = 0;
                    targetTiltY = 0;
                }
                
                if (!localRafId) {
                    tiltEl.style.willChange = 'transform';
                    localRafId = requestAnimationFrame(animateTilt);
                }
            });
            
            col.addEventListener('mouseenter', () => {
                if (window.innerWidth <= 991) return;
                isHovered = true;
                if (!localRafId) {
                    tiltEl.style.willChange = 'transform';
                    localRafId = requestAnimationFrame(animateTilt);
                }
            });
            
            col.addEventListener('mouseleave', () => {
                isHovered = false;
                targetTiltX = 0;
                targetTiltY = 0;
                targetFollowX = 0;
                targetFollowY = 0;
                if (!localRafId) {
                    tiltEl.style.willChange = 'transform';
                    localRafId = requestAnimationFrame(animateTilt);
                }
            });
        });
        
        // ─── B. Scroll Parallax Animation ────────────────────────────────────
        let scrollTicked = false;
        const updateScrollParallax = () => {
            if (window.innerWidth <= 991) {
                parallaxTargets.forEach(target => {
                    target.style.transform = '';
                });
                return;
            }
            
            const viewportHeight = window.innerHeight;
            
            parallaxTargets.forEach(target => {
                const rect = target.getBoundingClientRect();
                
                if (rect.bottom > -100 && rect.top < viewportHeight + 100) {
                    const elementCenter = rect.top + rect.height / 2;
                    const viewportCenter = viewportHeight / 2;
                    
                    // Normalize progress from -1 (entering bottom) to 1 (leaving top)
                    const scrollProgress = (viewportCenter - elementCenter) / (viewportHeight / 2 + rect.height / 2);
                    
                    // Range: 50px translation
                    const yOffset = -scrollProgress * 50; 
                    
                    target.style.transform = `translate3d(0, ${yOffset}px, 0)`;
                }
            });
        };
        
        window.addEventListener('scroll', () => {
            if (!scrollTicked) {
                requestAnimationFrame(() => {
                    updateScrollParallax();
                    scrollTicked = false;
                });
                scrollTicked = true;
            }
        }, { passive: true });
        
        updateScrollParallax();
    }

    // =========================================================================
    // 9. About Page Specific Luxury Interactions & Animations
    // =========================================================================

    // ─── Kayak Story Hero Parallax & Fade-Out ────────────────────
    const heroKayakContent = document.querySelector('.hero-kayak-content');
    const heroKayakBgImg = document.querySelector('.hero-kayak-bg-img');

    if (heroKayakContent) {
        let storyTicked = false;
        window.addEventListener('scroll', () => {
            if (!storyTicked) {
                requestAnimationFrame(() => {
                    const scrolled = window.scrollY;
                    if (scrolled < 900) {
                        heroKayakContent.style.transform = `translate3d(0, ${scrolled * 0.25}px, 0)`;
                        heroKayakContent.style.opacity = Math.max(0, 1 - (scrolled / 600));
                        if (heroKayakBgImg) {
                            heroKayakBgImg.style.transform = `scale(${1 + (scrolled * 0.00015)}) translate3d(0, ${scrolled * 0.08}px, 0)`;
                        }
                    }
                    storyTicked = false;
                });
                storyTicked = true;
            }
        }, { passive: true });
    }

    // ─── C. Animated Statistics Counter ──────────────────────────────────────
    const counterElements = document.querySelectorAll('.counter-val');
    if (counterElements.length > 0) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const targetNum = parseInt(el.getAttribute('data-target'), 10);
                    let currentNum = 0;
                    const duration = 1800; // ms
                    const stepTime = Math.max(Math.floor(duration / (targetNum || 1)), 20);
                    const increment = Math.max(Math.ceil(targetNum / (duration / stepTime)), 1);
                    
                    const timer = setInterval(() => {
                        currentNum += increment;
                        if (currentNum >= targetNum) {
                            el.textContent = targetNum;
                            clearInterval(timer);
                        } else {
                            el.textContent = currentNum;
                        }
                    }, stepTime);

                    counterObserver.unobserve(el);
                }
            });
        }, { threshold: 0.4 });

        counterElements.forEach(el => counterObserver.observe(el));
    }

    // =========================================================================
    // Parallax for services page custom illustration
    // =========================================================================
    const parallaxIllustration = document.querySelector('.cta-parallax-illustration');
    if (parallaxIllustration && !isMobileDevice) {
        document.addEventListener('mousemove', (e) => {
            const x = (e.clientX - window.innerWidth / 2) * 0.025;
            const y = (e.clientY - window.innerHeight / 2) * 0.025;
            requestAnimationFrame(() => {
                parallaxIllustration.style.setProperty('--px', `${x.toFixed(1)}px`);
                parallaxIllustration.style.setProperty('--py', `${y.toFixed(1)}px`);
            });
        }, { passive: true });
    }

    // =========================================================================
    // Parallax for contact page CTA container text
    // =========================================================================
    const contactCtaContainer = document.querySelector('.contact-cta-container');
    if (contactCtaContainer && !isMobileDevice) {
        document.addEventListener('mousemove', (e) => {
            const x = (e.clientX - window.innerWidth / 2) * 0.008;
            const y = (e.clientY - window.innerHeight / 2) * 0.008;
            requestAnimationFrame(() => {
                contactCtaContainer.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0)`;
            });
        }, { passive: true });
    }

});

