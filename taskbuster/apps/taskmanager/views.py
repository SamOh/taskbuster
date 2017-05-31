from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

@login_required
def task_homepage(request):
    return render(request, 'taskbuster/tasks.html')
