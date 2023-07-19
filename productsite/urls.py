from django.urls import path
from . import views
urlpatterns = [
   path('',views.home, name="home"), 
   path('postsign/',views.postsign, name="postsign"),
   path('logout/',views.logout, name="log"), 
   path('signUp/',views.signUp, name="signup"), 
   path('postsignup/',views.postsignup, name="postsignup"),
   path('create/',views.create, name="create"),
]
