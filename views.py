
from base64 import urlsafe_b64encode
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from avishkar import settings
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")
def contact(request):
    return render(request,"authentication/contact.html")

def signup(request):
   
    if request.method == "POST":
        
     #   username =request.POST.get['username']
        
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        myuser = User.objects.create_user(username,email,pass1)
        if User.objects.filter(username=username):
            def messages():
               messages.error(request,"username already exist! Please try some other username")
               return redirect("home")
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect("home")
            
        if pass1 != pass2:
            messages.error(request,"Passwords didn't match!")
            
            
        
        User.objects.create(username = request.POST.get("username"), email = request.POST.get("email"),password=request.POST.get("pass1"))
        myuser = User.objects.create_user(username = username, email = email, password=pass1)
        
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        user.set_password(user.password)
        myuser.save()
        messages()
        messages.success(request,"You're logged successfully created. We have sent you a confirmation email please confirm your email in order to activate your account")
       
       
        user = authenticate(username=username, password='secret')
        
    #EmailMessages
        
        subject = "Welcome to NEW  - Django Login!"
        messages = "Hello " + myuser.first_name +  "!! \n" + "Welcome TO NEW!! \n Thanks you for visiting our Website \n We have also sent you a confirmation email, please confirm your email address in order to activate your account \n\n Thanking You\n Arpit"
        from_email =  settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, messages,from_email, to_list,fail_silently=True)
        
                
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ NEW - Django Login!"
        message2 = render_to_string("email_confirmation.html",{
         'name' : myuser.first_name,
         'domain' : current_site.domain,
         'uid' : urlsafe_b64encode(force_bytes(myuser.pk)),
         'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail.silently = True
        email.send()
        
        
        return redirect("signin")
        return Database.Cursor.execute(self, quer, params)
        
    return render(request,"authentication/signup.html")
def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_dencode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError,OverflowError,User.DoesNotExist):
        myyser = None
        IntegrityError
       

        raise MultiValueDictKeyError(KEY_A1)
    
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser)
        messages.success(request,"Your Account has been acctivated !!")
        return redirect('signin')
    else:
        return render(request, 'activation_failed.html')
    
         
   
   

def signin(request):
    
    if request.method == "POST":
        if messages.is_valid():
             username = request.POST.get('username')
             pass1 = request.POST.get('pass1')
             user = authenticate(username=username, password='secret')
        
             if user is not None:
               login(request, user)
               fname = user.first_name
               return render(request, "authentication/index.html", {'fname':fname})
             else:
                messages.error(request,"Bad Credential")
                return redirect('home')
    
    
    return render(request,"authentication/signin.html",{'page_title' : 'Se connector'})
           

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("home")
    
    

