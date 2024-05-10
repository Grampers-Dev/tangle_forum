from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
#from .models import Reaction



class Profile(models.Model):
    """
    Represents a user profile associated with a Django User.
    Includes additional information about the user, such as likes.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the Profile object.
        """
        return self.user.username


class Thread(models.Model):
    """
    Represents a discussion thread where users can post messages
    and react with likes or dislikes.
    Thread allows users to express their approval (like) or disapproval
    (dislike) of the content.
    """
    title = models.CharField(max_length=50, blank=False,
                             help_text="Title of the thread.")
    description = models.TextField(max_length=100, blank=False,
                                   help_text="Detailed description of thread.")
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="The date and time this thread was created.")

    # Relationships to track which users have liked or disliked the thread
    liked_by = models.ManyToManyField(User, related_name='liked_threads',
                                      blank=True,
                                      help_text="Users who have liked this thread.")
    disliked_by = models.ManyToManyField(User, related_name='disliked_threads',
                                         blank=True,
                                         help_text="Users who have disliked this thread.")

    @property
    def total_likes(self):
        """
        Returns the total number of likes this thread has received.
        """
        return self.liked_by.count()

    @property
    def total_dislikes(self):
        """
        Returns the total number of dislikes this thread has received.
        """
        return self.disliked_by.count()

    def add_like(self, user):
        """
        Adds a like from a user, ensuring they do not also dislike the thread.
        Parameters:
            user (User): The user who is liking the thread.
        """
        self.disliked_by.remove(user)
        self.liked_by.add(user)

    def add_dislike(self, user):
        """
        Adds a dislike from a user, ensuring they do not also like the thread.
        Parameters:
            user (User): The user who is disliking the thread.
        """
        self.liked_by.remove(user)
        self.disliked_by.add(user)

    def __str__(self):
        """
        String representation of the Thread object.
        """
        return self.title

    class Meta:
        ordering = ['-date_created']
        # Orders threads by creation date by default.


class Reply(models.Model):
    """
    Represents a reply to a discussion thread.
    """
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the Reply object.
        """
        return self.message[:50]
    
def toggle_reaction(user, thread_id, reaction):
    # Get or create the profile
    profile, _ = Profile.objects.get_or_create(user=user)
    content_type = ContentType.objects.get_for_model(Thread)
    reaction_obj, created = Reaction.objects.get_or_create(user=user, content_type=content_type, object_id=thread_id)

    if reaction in ['like', 'dislike']:
        reaction_obj.is_liked = (reaction == 'like')
        reaction_obj.save()
    else:
        # If the reaction is neither like nor dislike, delete the reaction object
        reaction_obj.delete()

    # Increment likes count if the reaction is 'like'
    if reaction == 'like':
        profile.likes += 1
        profile.save()

    return {'status': 'success', 'reaction': reaction}
