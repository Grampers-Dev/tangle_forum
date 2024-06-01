
function updateGradient() {
    const width = document.documentElement.scrollWidth;
    const height = document.documentElement.scrollHeight;
    const size = Math.max(width, height) * 2;

    degree = (degree + 0.5) % 360; // Increment degree slowly to animate rotation
    const gradientColor = `linear-gradient(${degree}deg, rgba(255,0,0,1), rgba(0,0,255,1))`;
    bodyElement.style.backgroundImage = gradientColor;
    bodyElement.style.backgroundSize = `${size}px ${size}px`;
    bodyElement.style.backgroundPosition = 'center center';
    bodyElement.style.backgroundRepeat = 'no-repeat';

    animationFrameId = requestAnimationFrame(updateGradient); // Continue the animation
}

function startAnimation() {
    if (!animationFrameId) {
        updateGradient();
    }
}

function stopAnimation() {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Debounced version of updateGradient
const debouncedUpdateGradient = debounce(function() {
    updateGradient();
}, 50);

// Event listener to update gradient immediately on window resize
window.addEventListener('resize', debouncedUpdateGradient);

// MutationObserver to detect DOM changes
const observer = new MutationObserver(debouncedUpdateGradient);
observer.observe(document.body, { childList: true, subtree: true, attributes: true });

// Start the animation when the document is loaded
document.addEventListener('DOMContentLoaded', startAnimation);

// Stop the animation on page unload to prevent memory leaks
window.addEventListener('beforeunload', stopAnimation);

