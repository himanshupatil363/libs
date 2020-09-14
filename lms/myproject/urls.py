from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('books',views.books,name='books'),
    path('faq',views.faq,name='faq'),
    path('mybooks',views.mybooks,name='mybooks'),
    path('support',views.support,name='support'),
    path('update',views.update,name='update'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('request',views.request,name='request'),
    path('recover',views.recover,name='recover'),
    path('account_created',views.account_created,name='account_created'),

   
]












