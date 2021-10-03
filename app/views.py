from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages

from .models import Form

from .forms import SimpleForm

from datetime import datetime




# Create your views here.

def index(request):
    if request.method == 'POST':
        raw = request.POST.copy()
        subjects = raw.getlist('subjects')
        raw['subjects'] = '&'.join(subjects)
        submitted_dict = raw.dict()
        del submitted_dict['csrfmiddlewaretoken']
        form = Form(submit_time=timezone.now(), **submitted_dict)
        form.save()
        messages.success(request, 'Form submitted successfully!')
        return redirect('/')
    
    form = SimpleForm()
    return render(request, 'index.html',)