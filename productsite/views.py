from django.shortcuts import render
import pyrebase
# Create your views here.

config = {
    "apiKey": "AIzaSyD0BtuWBuMH4lDxhJKMaQghop2ebpkc7-k",
    "authDomain": "cpanel-c8e63.firebaseapp.com",
    "projectId": "cpanel-c8e63",
    "databaseURL": "https://cpanel-c8e63-default-rtdb.firebaseio.com",
    "storageBucket": "cpanel-c8e63.appspot.com",
    "messagingSenderId": "362165925051",
    "appId": "1:362165925051:web:858705054be9874750a59e"
  }
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def home(request):
	return render(request,"signIn.html",{})

def postsign(request):
	email=request.POST.get('email')
	passw = request.POST.get('pass')
	user= auth.sign_in_with_email_and_password(email,passw)
    


	return render(request,"welcome.html",{})