document.addEventListener('DOMContentLoaded', () => {
    const root = document.querySelector('#app-root');
    const previewState = document.querySelector('.state-preview');
    const immersiveState = document.querySelector('.state-immersive');
    const ctaState = document.querySelector('.state-cta');
    const playTrigger = document.querySelector('[data-role="play-trigger"]');
    const profileImgs = document.querySelectorAll('[data-profile-img]');
    const videoEl = document.getElementById('immersiveVideo');
    const ctaButton = document.getElementById('ctaButton');
    const ctaModal = document.querySelector('.cta-modal');
    const circularReveal = document.querySelector('.circular-reveal-container');
    const requiredAssets = {
        video: 'https://video.wixstatic.com/video/8455f5_03845574298047bab65cfd1c0e15e5ff/480p/mp4/file.mp4',
        thumbnail: 'https://static.wixstatic.com/media/8455f5_a1a05e78db8345938482383301ff10bc~mv2.png',
        profile: 'https://static.wixstatic.com/media/8455f5_c082110886634d768b1c7a9f956c3b1b~mv2.jpg',
    };

    let stateTwoTimer = null;
    let timerStart = 0;
    const STATE_TWO_DURATION = 5000; // ms
    const TIMER_TOLERANCE = 100;
    const CTA_ANIMATION_MAX = 800;
    const PREVIEW_TRANSITION_DURATION = 420; // ms

    const logValidation = (message) => console.info(`[Validation] ${message}`);

    const preloadProfile = () => {
        const img = new Image();
        return new Promise((resolve, reject) => {
            img.src = requiredAssets.profile;
            img.onload = () => {
                profileImgs.forEach((node) => {
                    node.src = img.src;
                });
                resolve();
            };
            img.onerror = reject;
        });
    };

    const verifyAssets = async () => {
        const checks = await Promise.allSettled([
            fetch(requiredAssets.video, { method: 'HEAD' }),
            fetch(requiredAssets.thumbnail, { method: 'HEAD' }),
            fetch(requiredAssets.profile, { method: 'HEAD' }),
        ]);
        const failed = checks.filter((c) => c.status === 'rejected');
        if (failed.length) {
            console.warn('Asset validation failed. Experience may degrade.', failed);
        } else {
            logValidation('Assets accessible');
        }
    };

    const setState = (state) => {
        root.dataset.state = state;
        const showPreview = state === 'preview';
        const showImmersive = state === 'immersive' || state === 'cta';
        const showCta = state === 'cta';

        previewState.classList.toggle('is-active', showPreview);
        immersiveState.classList.toggle('is-active', showImmersive);
        ctaState.classList.toggle('is-active', showCta);
        ctaState.classList.toggle('active', showCta);
        ctaState.setAttribute('aria-hidden', (!showCta).toString());
    };

    const cleanupTimer = () => {
        if (stateTwoTimer) {
            cancelAnimationFrame(stateTwoTimer);
            stateTwoTimer = null;
        }
    };

    const transitionToStateTwo = () => {
        setState('immersive');
        videoEl.currentTime = 0;
        const playPromise = videoEl.play();
        if (playPromise?.catch) {
            playPromise.catch(() => {
                immersiveState.classList.add('show-fallback');
                logValidation('Autoplay blocked, showing fallback');
            });
        }
        timerStart = performance.now();
        const tick = (now) => {
            const elapsed = now - timerStart;
            if (elapsed >= STATE_TWO_DURATION - TIMER_TOLERANCE) {
                logValidation(`State 2 timer reached ${elapsed.toFixed(2)}ms`);
                transitionToStateThree(now);
                return;
            }
            stateTwoTimer = requestAnimationFrame(tick);
        };
        stateTwoTimer = requestAnimationFrame(tick);
    };

    const transitionToStateThree = (timestamp) => {
        cleanupTimer();
        videoEl.pause();
        setState('cta');
        ctaState.dataset.animationStart = timestamp;
        startCtaAnimation();
        setTimeout(() => {
            const animationElapsed = performance.now() - timestamp;
            if (animationElapsed <= CTA_ANIMATION_MAX) {
                logValidation(`CTA animation completed in ${animationElapsed.toFixed(2)}ms`);
            } else {
                console.warn('CTA animation exceeded required duration');
            }
        }, CTA_ANIMATION_MAX);
    };

    const startCtaAnimation = () => {
        if (!ctaModal) return;
        circularReveal?.classList.remove('revealed');
        requestAnimationFrame(() => {
            setTimeout(() => {
                circularReveal?.classList.add('revealed');
            }, 120);
        });
    };

    const animatePreviewExit = () => new Promise((resolve) => {
        if (!previewState) {
            resolve();
            return;
        }
        const finish = () => {
            previewState.classList.remove('is-transitioning');
            resolve();
        };
        previewState.classList.add('is-transitioning');
        const timeoutId = setTimeout(finish, PREVIEW_TRANSITION_DURATION + 60);
        previewState.addEventListener('animationend', () => {
            clearTimeout(timeoutId);
            finish();
        }, { once: true });
    });

    const init = async () => {
        await verifyAssets();
        try {
            await preloadProfile();
            logValidation('Profile image cached');
        } catch (err) {
            console.warn('Profile preload failed, using fallback', err);
            profileImgs.forEach((node) => {
                node.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80"%3E%3Ccircle cx="40" cy="40" r="40" fill="%23333"/%3E%3Ctext x="40" y="48" fill="white" font-size="24" alignment-baseline="middle" text-anchor="middle"%3F%3E%F0%9F%90%BB%3C/text%3E%3C/svg%3E';
            });
        }

        playTrigger?.addEventListener('click', async (event) => {
            event.preventDefault();
            if (root.dataset.state !== 'preview') return;
            playTrigger.setAttribute('disabled', 'true');
            await animatePreviewExit();
            logValidation('Entering State 2');
            transitionToStateTwo();
        });

        ctaButton?.addEventListener('click', () => {
            const url = ctaButton.dataset.targetUrl;
            if (!url) {
                console.warn('CTA URL not configured yet.');
                return;
            }
            ctaButton.disabled = true;
            ctaButton.textContent = 'Redirecting…';
            window.location.href = url;
        });

        window.addEventListener('beforeunload', cleanupTimer);
        window.addEventListener('resize', () => {
            if (root.dataset.state === 'immersive') {
                logValidation('Resize detected during State 2, maintaining full screen');
            }
        });

        setState('preview');
        logValidation('State 1 ready, waiting for interaction');
    };

    init();
});