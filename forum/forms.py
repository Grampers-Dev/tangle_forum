from django.forms import ModelForm
from .models import Thread, Reply


class ThreadForm(ModelForm):
    """
    Form for creating or updating a thread.
    """
    class Meta:
        model = Thread
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        """
        Initialize form fields with custom attributes.
        """
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder':
                                                      'Enter Thread Name'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Thread Description'})


class ReplyForm(ModelForm):
    """
    Form for creating or updating a reply.
    """
    class Meta:
        model = Reply
        fields = ['message', ]

    def __init__(self, *args, **kwargs):
        """
        Initialize form fields with custom attributes.
        """
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Post a reply...'})