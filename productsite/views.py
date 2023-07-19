from django.shortcuts import render
import pyrebase
from django.contrib import auth
import firebase_admin







# Create your views here.
# Initialize the Firebase Admin SDK
#cred = credentials.Certificate('E:/myprograms/productapp/serviceAccountKey.json')
#second_app = firebase_admin.initialize_app(cred, name="second_app")
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
        uid=user['localId']
    except:
        message = "unable to create try again"
        return render(request, "signUp.html",{"messg":message})
        

    data={"name":name,"status":"1"}

    database.child("users").child(uid).child("details").set(data)
    return render(request,"signIn.html",)

'''def get_user_name(request):

    #if request.user.is_authenticated:
        # Retrieve the name from the currently authenticated user
    user_name = request.user.name  # Replace 'name' with the actual attribute name

    return user_name
    #else:
   '''  #   return None

def postsign(request):
    name=request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw,)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html",{"messg":message})
    #print(user['idToken'])
    session_id = user['idToken']
    request.session['uid']=str(session_id)

    

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("hi"+str(a))
    context = {  
        
        "display": 'link'
    }
    
    if (a =='ULSWyaqHKuY4SreAlBvDFIHiehj1') or (a == 'p5acZtl0u7XMR4nLSZcZBIAOfP92'):
        return render(request, "welcome.html", )
    else:
        
        return render(request, "welcome.html",context)

def logout(request):
    auth.logout(request)
    return render(request,"signIn.html",)

def create(request):
    return render(request, 'create.html',)


def postcreate(request):
    productId =request.POST.get('productId')
    productName = request.POST.get('productName')
    productDescription = request.POST.get('productDescription')
    productPrice = request.POST.get('productPrice' )

    idtoken = request.session(uid)


    data = {
        "productId":productId,
        "productName":productName,
        "productDescription": productDescription,
        "productPrice":productPrice,
    }
    database.child(product).child(prod_info).set(data)

    return render(request, 'welcome.html',)


