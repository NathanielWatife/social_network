from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Profile

# Create your views here.
def home(request):
    return render(request, "index.html")


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
            user_model = User.objects.create(username=username)
            new_profile = Profile.objects.get(user=username, id_user=user_model.id)
            new_profile.save()
            return redirect('/') 
            
            
    else:
        return render(request, "register.html")

def login(request):
    return render(request, "login.html")