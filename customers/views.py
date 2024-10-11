from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from .models import CustomerProfile
# Create your views here.

class SignUpPage(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    

class Customer_Profile(View):
    def get(self, request):
        customer_profile = request.user.customerprofile
        return render(request, 'profile.html', {'customer_profile': customer_profile})
