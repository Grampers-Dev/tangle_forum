$(document).ready(function() {
    $('#like-section form').on('submit', function(event) {
        event.preventDefault();  // Stop the form from submitting normally
        var threadId = $('input[name="thread_id"]').val();  // Get the thread ID from the hidden input
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();  // CSRF token for POST request

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),  // Use the action URL from the form itself
            data: {
                'thread_id': threadId,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response) {
                $('#like-count').text(response.total_likes + ' Likes');  // Update the like count
                // Optionally update the button based on the new state
                var button = $('#like-section button');
                if (response.is_liked) {
                    button.removeClass('btn-primary').addClass('btn-danger').text('Dislike');
                } else {
                    button.removeClass('btn-danger').addClass('btn-primary').text('Like');
                }
            },
            error: function(xhr, status, error) {
                console.error("Error: " + error);  // Log errors
            }
        });
    });
});



const pageTitle = document.querySelector('.pageTitle, .big');
const text = pageTitle.innerHTML;
pageTitle.innerHTML = "";

let i = 0;
function typeWriter() {
  if (i < text.length) {
    pageTitle.innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, 150); // Adjust typing speed
  }
}

typeWriter(); // Start the effect

const bodyElement = document.querySelector('body');
let degree = 0;
let animationFrameId;

// Function to update the gradient based on screen size and rotation degree
function updateGradient() {
    const width = window.innerWidth;
    const height = window.innerHeight;
    // Calculate a size that surely covers the entire element even during rapid resizes
    const size = Math.max(width, height) * 2; // Ensure an overly sufficient coverage

    degree = (degree + 0.5) % 360; // Increment degree slowly to animate rotation
    const gradientColor = `linear-gradient(${degree}deg, rgba(255,0,0,1), rgba(0,0,255,1))`;
    bodyElement.style.backgroundImage = gradientColor;
    bodyElement.style.backgroundSize = `${size}px ${size}px`;
    bodyElement.style.backgroundPosition = 'center center';
    bodyElement.style.backgroundRepeat = 'no-repeat';

    animationFrameId = requestAnimationFrame(updateGradient); // Continue the animation
}


// Function to start the animation
function startAnimation() {
    if (!animationFrameId) {
        updateGradient();
    }
}

// Function to stop the animation when it is no longer needed
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
}, 50);  // Adjust delay as necessary, 50ms is generally reasonable

// Event listener to update gradient immediately on window resize
window.addEventListener('resize', updateGradient);

// Start the animation when the document is loaded
document.addEventListener('DOMContentLoaded', startAnimation);

// Stop the animation on page unload to prevent memory leaks
window.addEventListener('beforeunload', stopAnimation);
