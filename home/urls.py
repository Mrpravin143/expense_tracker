from django.urls import path
from home.views import search,send_otp,student_databse,contact_form_view

urlpatterns = [
    path('search',search,name='search'),
    path('phone-number/',send_otp),
    path('student/',student_databse),
    path('contact/',contact_form_view),
 
]
