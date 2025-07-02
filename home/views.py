from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Product,UserProfile,StudentData,Colleges
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank,TrigramSimilarity
from django.core.mail import send_mail
import random
from django.core.cache import cache
from ratelimit.decorators import ratelimit

# Create your views here.

def search(request):
    search = request.GET.get('search')
    if search:
        query = SearchQuery(search)
        vector = (
            SearchVector('title', weight = "A") +
            SearchVector('description', weight = "B") +
            SearchVector('category', weight = "C") +
            SearchVector('brand', weight = "D"))

        rank = SearchRank(vector,query)
        results = Product.objects.annotate(
            rank=rank,
            similarity = TrigramSimilarity('title',search) + TrigramSimilarity('description',search) +
            TrigramSimilarity('category',search) + TrigramSimilarity('brand',search)

        ).filter(Q(rank__gte = .03) | Q(similarity__gte = .03)).distinct().order_by('-rank','-similarity')
        print(rank)

        brand = Product.objects.all().distinct('brand').order_by('brand')
        category = Product.objects.all().distinct('category').order_by('category')

        if request.GET.get('brand'):
            results = results.filter(
                brand = request.GET.get('brand')
            ).order_by('price')

        
        
    else:
        results = Product.objects.all() 
    return render(request,'search.html',{'results':results,'brand':brand,'category':category})


def send_otp(request):
    if request.method == "POST":
        phone = request.POST.get('phone')

        profile_qs = UserProfile.objects.filter(phone_number=phone)
        print(profile_qs)

    return render(request,'phone_number.html')




# Implementing Cache 
def student_databse(request):
    message = cache.get('greeting_msg')

    if message is None:
        message="Hello! This is your first visit. Data cached now."
        cache.set('greeting_msg',message,timeout=60)
        status = "Fetch data from logic"

    else:
        status="Aleardy Fecth data"
        message = "Data is Now in Cashed"

    

    # Return response
    return HttpResponse(f"{status}</br>{message}")



# Implement Rate Limiting 
@ratelimit(key='ip', rate='3/m', block=True)
def contact_form_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Here you would normally save to DB or send email
        return HttpResponse(f"Thank you, {name}. Your message has been received.")

        
    return HttpResponse("""
    <form method="post">
        Name: <input type="text" name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <input type="submit" value="Send">
    </form>
    """)





    














    




        




    

 

