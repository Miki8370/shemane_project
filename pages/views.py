from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Design

# Create your views here.

class HomePage(View):
    def get(self, request):
        designs = Design.objects.all()
        return render(request, 'home.html', {'designs': designs})
        
    