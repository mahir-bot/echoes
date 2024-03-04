from django import forms
from .import models


class StoryForm(forms.ModelForm):
    class Meta:
        model = models.Stories
        fields = ['title', 'content','slug', 'thumbnil']