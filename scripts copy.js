js
document.addEventListener('DOMContentLoaded', () => {
    const state1 = document.getElementById('state1');
    const state2 = document.getElementById('state2');
    const state3 = document.getElementById('state3');

    const playButton = state1.querySelector('.play-button');
    const immersiveVideo = document.getElementById('immersive-video');
    const modalProfilePic = state3.querySelector('.modal-profile-pic');
    const finalCtaButton = document.getElementById('final-cta-button');

    let state2Timer;
    let cachedProfilePicUrl = '';
    const CTA_REDIRECT_URL = 'https://www.instagram.com/accounts/signup/phone?next=%2Freel%2FDP095S7Cujq%2F%3Fl%3D1'; // Your target URL

    // --- State Transition Functions ---

    function activateState(targetState) {
        // Deactivate all states
        [state1, state2, state3].forEach(s => s.classList.remove('active'));
        // Activate the target state
        targetState.classList.add('active');
    }

    function enterState1() {
        activateState(state1);
        // Ensure video is paused if returning from State 2
        if (immersiveVideo) {
            immersiveVideo.pause();
            immersiveVideo.currentTime = 0;
        }
        // Clear any ongoing timers
        clearTimeout(state2Timer);
    }

    function enterState2() {
        activateState(state2);

        // Get profile picture URL from State 2 UI overlay
        const userProfilePicElement = state2.querySelector('.user-profile-pic');
        if (userProfilePicElement) {
            cachedProfilePicUrl = userProfilePicElement.src;
        }

        // Start video playback
        if (immersiveVideo) {
            immersiveVideo.play().catch(error => {
                console.error("Video autoplay failed:", error);
                // Handle autoplay policy: maybe show a play button if blocked
            });
        }

        // Start timer for State 3 transition
        clearTimeout(state2Timer); // Clear any previous timer
        state2Timer = setTimeout(() => {
            exitState2AndEnterState3();
        }, 8000); // 8 seconds as per specification
    }

    function exitState2AndEnterState3() {
        // Stop video playback
        if (immersiveVideo) {
            immersiveVideo.pause();
        }
        clearTimeout(state2Timer); // Ensure timer is cleared

        activateState(state3);
        setupState3Modal();
    }

    // --- State 3 Specific Logic ---

    function setupState3Modal() {
        // Set the cached profile pic in the modal
        if (modalProfilePic && cachedProfilePicUrl) {
            modalProfilePic.src = cachedProfilePicUrl;
        }

        // Trigger the circular reveal animation after a brief delay
        // to allow the modal to fade in first.
        setTimeout(() => {
            const revealContainer = state3.querySelector('.circular-reveal-container');
            if (revealContainer) {
                revealContainer.classList.add('revealed');
            }
        }, 100); // 100ms delay
    }

    // --- Event Listeners ---

    if (playButton) {
        playButton.addEventListener('click', enterState2);
    }

    if (finalCtaButton) {
        finalCtaButton.addEventListener('click', () => {
            window.location.href = CTA_REDIRECT_URL;
        });
    }

    // --- Initial State ---
    enterState1(); // Start with State 1 when the page loads
});