import re
from django.shortcuts import redirect, render
from .models import Stories
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.


def story_list(request):
    story = Stories.objects.all().order_by('created_at')

    return render(request, 'stories/story_list.html', {
        'Story': story
    })


def story_detail(request, slug):
    story = Stories.objects.get(slug=slug)
    return render(request, 'stories/story_detail.html', {
        'Story': story
    })


@login_required(login_url='account:login')
def story_create(request):
    if request.method == 'POST':
        form = forms.StoryForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('stories:list')
    else:
        form = forms.StoryForm()
    return render(request, 'stories/story_create.html', {
        'form': form
    })
