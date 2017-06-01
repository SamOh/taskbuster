from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from . models import Profile, Project, Tag, Task


@login_required
def task_homepage(request):
    # Check to make sure current user has a profile, if not, create one
    if not(Profile(user=request.user)):
        new_profile = Profile(user=request.user)
        new_profile.save()

    return render(request, 'taskbuster/tasks.html')


@login_required
def add_task(request):
    if request.method == 'POST':
        new_task = Task()
        new_task.save()
        # add the task to database...
    return redirect()
