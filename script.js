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
        const handleNavScroll = throttle(() => {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        }, 100);
        window.addEventListener('scroll', handleNavScroll, { passive: true });
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

    // =========================================================================
    // 4. Cinematic Night Background Parallax — batched in single rAF loop
    // =========================================================================
    if (window.innerWidth >= 1024) {
        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let rafPending = false;

        const heroLeft = document.querySelector('.hero-left');
        const desktopMoonBg = document.querySelector('.desktop-moon-bg');
        const cloudsContainer = document.querySelector('.clouds-container');

        const applyParallax = () => {
            rafPending = false;
            const x = (mouseX / window.innerWidth - 0.5) * 2;
            const y = (mouseY / window.innerHeight - 0.5) * 2;

            if (heroLeft) heroLeft.style.transform = `translate3d(${x * -10}px, ${y * -10}px, 0)`;
            if (desktopMoonBg) desktopMoonBg.style.transform = `translate3d(${x * -12}px, ${y * -8}px, 0)`;
            if (cloudsContainer) cloudsContainer.style.transform = `translate3d(${x * 12}px, ${y * 8}px, 0)`;
        };

        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            if (!rafPending) {
                rafPending = true;
                requestAnimationFrame(applyParallax);
            }
        }, { passive: true });
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

});
