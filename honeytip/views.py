from django.shortcuts import render
from .models import Tip
# Create your views here.

def honeytip(request):
    tips = Tip.objects
    return render(request, 'honeytip.html', {'tips': tips})