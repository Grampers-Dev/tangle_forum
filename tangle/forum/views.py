from django.shortcuts import render, redirect, get_object_or_404
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import ThreadForm, ReplyForm
from .models import Thread, Reply
from django.views.generic.base import View
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    """
    Render the index page with a form to create new threads and
    display existing threads.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered index page template.
    """
    form = ThreadForm()

    threads = Thread.objects.all()

    context = {'form': form, 'threads': threads}
    return render(request, 'forum/index.html', context)


def thread(request, thread_id):
    """
    Display a specific thread with its replies and a form to post new replies.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread to display.

    Returns:
        HttpResponse: Rendered thread page template.
    """
    thread = Thread.objects.get(pk=thread_id)
    replies = thread.reply_set.all()
    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = thread
            reply.user = request.user
            reply.save()
            return redirect('thread', thread_id=thread_id)

    context = {
        'thread': thread,
        'form': form,
        'replies': replies,
    }
    return render(request, 'forum/thread.html', context)


def thread_detail(request, pk):
    """
    Display the details of a specific thread.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the thread to display.

    Returns:
        HttpResponse: Rendered thread detail page template.
    """
    thread = get_object_or_404(Thread, pk=pk)
    return render(request, 'thread_detail.html', {'thread': thread})


@login_required
@require_POST
def likes(request):
    """
    Toggle like on a thread and return updated like status via AJAX.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with updated like status.
    """
    thread_id = request.POST.get('thread_id')
    thread = get_object_or_404(Thread, pk=thread_id)

    # Toggle like
    if thread.liked_by.filter(id=request.user.id).exists():
        thread.liked_by.remove(request.user)
        is_liked = False
    else:
        thread.liked_by.add(request.user)
        is_liked = True

    total_likes = thread.liked_by.count()  # Simplified for clarity

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'total_likes': total_likes,
            'is_liked': is_liked
        })

    return redirect('thread_detail', pk=thread.id)


@login_required
def like_thread(request, thread_id):
    """
    Like or unlike a thread.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread to like or unlike.

    Returns:
        JsonResponse: JSON response with updated likes and dislikes count.
    """
    thread = Thread.objects.get(id=thread_id)
    user = request.user
    if user in thread.liked_by.all():
        thread.liked_by.remove(user)  # User unlikes the thread
    else:
        thread.liked_by.add(user)
        thread.disliked_by.remove(user)  # Remove dislike if present
    return JsonResponse({'likes': thread.total_likes,
                         'dislikes': thread.total_dislikes})


@login_required
def dislike_thread(request, thread_id):
    """
    Dislike or undislike a thread.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread to dislike or undislike.

    Returns:
        JsonResponse: JSON response with updated likes and dislikes count.
    """
    thread = Thread.objects.get(id=thread_id)
    user = request.user
    if user in thread.disliked_by.all():
        thread.disliked_by.remove(user)  # User undislikes the thread
    else:
        thread.disliked_by.add(user)
        thread.liked_by.remove(user)  # Remove like if present
    return JsonResponse({'likes': thread.total_likes,
                         'dislikes': thread.total_dislikes})


@require_POST
def new_thread(request):
    """
    Create a new thread.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the newly created thread or
        re-renders the index page with errors.
    """
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save()
            return redirect('thread', thread_id=thread.id)
            # Redirect to the newly created thread
    else:
        form = ThreadForm()
    return render(request, 'forum/index.html', {'form': form})


def update_thread(request, thread_id):
    """
    Update an existing thread.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread to update.

    Returns:
        HttpResponse: Redirects to the updated thread or re-renders the
        update thread page with errors.
    """
    thread = Thread.objects.get(pk=thread_id)
    form = ThreadForm(instance=thread)

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread', thread_id=thread_id)

    context = {'form': form}
    return render(request, 'forum/update_thread.html', context)


def delete_thread(request, thread_id):
    """
    Delete an existing thread.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread to delete.

    Returns:
        HttpResponse: Redirects to the index page after deleting the thread.
    """
    thread = Thread.objects.get(pk=thread_id)

    if request.method == 'POST':
        thread.delete()
        return redirect('index')

    context = {'thread': thread}
    return render(request, 'forum/thread.html', context)


def delete_reply(request, thread_id, reply_id):
    """
    Delete an existing reply.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread containing the reply.
        reply_id (int): The ID of the reply to delete.

    Returns:
        HttpResponse: Redirects to the thread page after deleting the reply.
    """
    reply = get_object_or_404(Reply, pk=reply_id)

    # Check if the current user is the owner of the reply
    if request.user == reply.user:
        if request.method == 'POST':
            reply.delete()
            return redirect('thread', thread_id=thread_id)
            # Use thread_id from the URL pattern

        context = {'reply': reply, 'thread': reply.thread,
                   'replies': reply.thread.reply_set.all()}
        return render(request, 'forum/thread.html', context)
    else:
        # If the user is not the owner, redirect them or show an error message
        return redirect('permission_denied')


def update_reply(request, thread_id, reply_id):
    """
    Update an existing reply.

    Parameters:
        request (HttpRequest): The HTTP request object.
        thread_id (int): The ID of the thread containing the reply.
        reply_id (int): The ID of the reply to update.

    Returns:
        HttpResponse: Redirects to the thread page after updating the reply.
    """
    reply = get_object_or_404(Reply, pk=reply_id)
    form = ReplyForm(instance=reply)

    # Check if the current user is the owner of the reply
    if request.user == reply.user:
        if request.method == 'POST':
            form = ReplyForm(request.POST, instance=reply)
            if form.is_valid():
                form.save()
                return redirect('thread', thread_id=thread_id)

        context = {'form': form, 'thread': reply.thread, 'reply': reply}
        # Include 'reply' in the context
        return render(request, 'forum/thread.html', context)
    else:
        # If the user is not the owner, redirect them or show an error message
        return redirect('permission_denied')


@require_POST
@login_required  # Uncomment if login is required
def update_likes(request):
    """
    Update likes or dislikes count for a thread.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with updated likes and dislikes count.
    """
    thread_id = request.POST.get('id')
    action = request.POST.get('action')

    try:
        thread = Thread.objects.get(pk=thread_id)
        if action == 'like':
            thread.likes += 1
        elif action == 'dislike':
            thread.dislikes += 1
        thread.save()

        return JsonResponse({'status': 'ok', 'likes': thread.likes,
                             'dislikes': thread.dislikes})
    except Thread.DoesNotExist:
        return JsonResponse({'status': 'error', 'error':
                             'Thread not found'}, status=404)

