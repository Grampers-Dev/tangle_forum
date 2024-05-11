from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ExtendedUserCreationForm
from django.contrib import messages



def register(request):
    """
    View for user registration.

    Handles the registration form submission and creates a new user account.
    Sends a welcome email to the newly registered user.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page upon successful registration.
    """
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            #Send welcome email to the newly registered user
            subject = 'Welcome to Tangle!'
            context = {'username': user.username}  # Pass any additional context variables needed for the email template
            html_message = render_to_string('welcome_email.html', context)
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'tangleforum.info@gmail.com', [user.email], html_message=html_message)

            messages.success(request, 'Your account has been created. Please log in.')
            return redirect('login')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'user_profile/register.html', {'form': form})


@login_required
def profile(request):
    """
    View for user profile.

    Renders the user profile page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered user profile page.

    Reference:
        Django authentication:
        https://docs.djangoproject.com
        /en/stable/topics/auth/default/#the-login-required-decorator
    """
    return render(request, 'user_profile/profile.html')


def custom_login(request):
    """
    Custom login view.

    Handles user authentication and login.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the home page upon successful login.

    References:
        Django authentication:
        https://docs.djangoproject.com
        /en/stable/topics/auth/default/#how-to-log-a-user-in
        Django forms: https://docs.djangoproject.com/en/stable/topics/forms/
        Django messages:
        https://docs.djangoproject.com/en/stable/ref/contrib/messages/
    """

    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request,
                               'Invalid username or password Please try again')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'user_profile/login.html', {'form': form})


def custom_logout(request):
    """
    Custom logout view.

    Handles user logout.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page upon logout.

    Reference:
        Django authentication:
        https://docs.djangoproject.com
        /en/stable/topics/auth/default/#how-to-log-a-user-out
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
    