from django.urls import path
from home.views import search,send_otp

urlpatterns = [
    path('search',search,name='search'),
    path('phone-number/',send_otp),
 
]
