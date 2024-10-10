from django.urls import path
from .views import SignUpPage
from .views import Customer_Profile

urlpatterns = [

    path('signup/', SignUpPage.as_view(), name='signup'),
    path('profile/', Customer_Profile.as_view(), name='profile')

]