from django.shortcuts import render
from . import forms

def home(request):
    dform = forms.DForm()
    return render(request, 'form.html', {'form': dform})

def model(request):
    mform = forms.MForm()
    return render(request, 'form.html', {'form': mform})