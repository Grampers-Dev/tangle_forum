$(document).ready(function() {
    var passwordInput = $('#password1');
    var messageContainer = $('#password-strength-indicator');

    if (passwordInput.length && messageContainer.length) {
        passwordInput.on('input', function() {
            var password = $(this).val();

            // Make AJAX request to evaluate password strength
            $.ajax({
                url: '/evaluate_password_strength/',
                method: 'GET',
                data: {
                    password: password
                },
                success: function(response) {
                    var strength = response.strength;

                    // Update message container based on password strength
                    // You can customize this based on your requirements
                    messageContainer.html("Password strength: " + strength);
                },
                error: function(xhr, status, error) {
                    // Handle error
                    console.error('Error:', status);
                }
            });
        });
    }
});
