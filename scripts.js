// Instagram Sign Up Modal Functionality

document.addEventListener('DOMContentLoaded', function() {
    const openAppBtn = document.getElementById('openAppBtn');
    const signupBtn = document.getElementById('signupBtn');
    const signupModal = document.getElementById('signupModal');
    
    // Open Instagram App Button Handler
    if (openAppBtn) {
        openAppBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Try to open Instagram app
            const instagramAppUrl = 'instagram://';
            const instagramWebUrl = 'https://www.instagram.com/';
            
            // Attempt to open Instagram app
            window.location.href = instagramAppUrl;
            
            // Fallback to web if app doesn't open
            setTimeout(function() {
                window.open(instagramWebUrl, '_blank');
            }, 500);
            
            console.log('Opening Instagram app...');
        });
    }
    
    // Sign Up Button Handler
    if (signupBtn) {
        signupBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Redirect to Instagram sign up page
            const signupUrl = 'https://www.instagram.com/accounts/emailsignup/';
            window.open(signupUrl, '_blank');
            
            console.log('Redirecting to Instagram sign up...');
        });
    }
    
    // Terms and Privacy Policy Link Handlers
    const termsLinks = document.querySelectorAll('.terms-link');
    termsLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const href = this.getAttribute('href');
            if (href === '#') {
                // Default behavior - you can customize these URLs
                if (this.textContent.includes('Terms')) {
                    window.open('https://help.instagram.com/581066165581870', '_blank');
                } else if (this.textContent.includes('Privacy')) {
                    window.open('https://help.instagram.com/519522125107875', '_blank');
                }
            } else {
                window.open(href, '_blank');
            }
        });
    });
    
    // Optional: Add keyboard navigation
    document.addEventListener('keydown', function(e) {
        // ESC key to close modal (if needed in future)
        if (e.key === 'Escape') {
            // Add close functionality if needed
        }
        
        // Enter key on buttons
        if (e.key === 'Enter') {
            const focusedElement = document.activeElement;
            if (focusedElement === openAppBtn || focusedElement === signupBtn) {
                focusedElement.click();
            }
        }
    });
    
    // Optional: Add touch event handlers for better mobile experience
    if (openAppBtn) {
        openAppBtn.addEventListener('touchstart', function() {
            this.style.opacity = '0.8';
        });
        
        openAppBtn.addEventListener('touchend', function() {
            this.style.opacity = '1';
        });
    }
    
    if (signupBtn) {
        signupBtn.addEventListener('touchstart', function() {
            this.style.opacity = '0.8';
        });
        
        signupBtn.addEventListener('touchend', function() {
            this.style.opacity = '1';
        });
    }
    
    console.log('Instagram Sign Up Modal initialized');
});

