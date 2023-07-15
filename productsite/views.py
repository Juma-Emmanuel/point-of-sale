from django.shortcuts import render
import pyrebase
from django.contrib import auth
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

authe = firebase.auth()
database=firebase.database()

def home(request):
	return render(request,"signIn.html",{})
def signUp(request):
    return render(request, "signUp.html",)

def postsignup(request):
    
    name=request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        message = "unable to create try again"
        return render(request, "signUp.html",{"messg":message})
        uid = user['localId']

    data={"name":name,"status":"1"}

    database.child("users").child(uid).child("details").set(data)
    return render(request,"signIn.html",)
def postsign(request):
    name=request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw,)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "welcome.html", {"n":name})

def logout(request):
    auth.logout(request)
    return render(request,"signIn.html",)






