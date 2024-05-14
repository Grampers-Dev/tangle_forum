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

