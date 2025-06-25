from django.urls import path
from tracker.views import index,deleteTransactions,RegisterUser,LoginUser,logoutUser

urlpatterns = [
    path('',index, name='index'),
    path('delete-Transactions/<uuid>/',deleteTransactions,name='deleteTransactions'),
    path('register/',RegisterUser , name='RegisterUser'),
    path('login/',LoginUser , name='LoginUser'),
    path('logout/',logoutUser , name='logoutUser'),
   
 
]
