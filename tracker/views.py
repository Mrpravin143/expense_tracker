from django.shortcuts import render, redirect
from django.contrib import messages
from tracker.models import Transaction
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


today = timezone.now().date()

@login_required(login_url = "/login/")
def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        if not description:
            messages.warning(request, "Description आवश्यक आहे.")
            return redirect('/')

        try:
            amount = float(amount)
        except ValueError:
            messages.warning(request, "रक्कम योग्य स्वरूपात द्या.")
            return redirect('/')

        Transaction.objects.create(
            description=description,
            amount=amount,
            created_by = request.user,
        )
        messages.success(request, "नोंद जतन झाली.")

        return redirect('/')  # नोंद save झाल्यावर redirect करून परत GET ने 

        
  
    
    context = {
        'transactions': Transaction.objects.filter(created_by = request.user),
        'balance':Transaction.objects.filter(created_by = request.user).aggregate(total_balance = Sum('amount'))['total_balance'] or 0,
        'income':Transaction.objects.filter(created_by = request.user,amount__gte = 0).aggregate(income = Sum('amount'))['income'] or 0,
        'expense':Transaction.objects.filter(created_by = request.user,amount__lte = 0).aggregate(expense = Sum('amount'))['expense'] or 0,
        
    }
    return render(request, 'index.html', context)


@login_required(login_url = "/login/")
def deleteTransactions(request,uuid):
    Transaction.objects.get(uuid = uuid).delete()
    return redirect('/')



# Authentication Sytem start from here
 
def RegisterUser(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')

        user_obj = User.objects.filter(
            Q(username=username) | Q(password=password)
        )

        if user_obj.exists():
            messages.warning(request, "⚠️ Username & Password Already Exists")
            return redirect('/register/')

        user_data=User.objects.create(
            first_name =first_name,
            username=username,
            email=email,
        )
        user_data.set_password(password)
        user_data.save()
        messages.success(request, "✅ Registration successful!")
        return redirect('/login/')

    return render(request,'register.html')



def LoginUser(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user_obj = authenticate(username=username,password=password)

        if not user_obj:
            messages.error(request,"❌ Invalid credentials")
            return redirect('/login/')

        login(request,user_obj)
        return redirect('/')


    return render(request,'loginuser.html')


@login_required(login_url = "/login/")
def logoutUser(request):
    logout(request)
    messages.success(request, "✅ Logged Out Success !")
    return redirect('/login/')