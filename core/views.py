from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Profile

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, "index.html")

@login_required(login_url='login')
def setting(request):
    return render(request, "setting.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                message.info(request, 'Username alreadly exist, Try a new one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                message.info(request, "Email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, "No match for Password")
            return redirect('register')

        # create a new user profile for the user new user
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('/') 
            
            
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user details are available
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')