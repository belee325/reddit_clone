from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def signup(request):
    # {'info': info}
    if request.method == 'POST':
        # make a new user
        try:
            User.objects.get_by_natural_key(username=request.POST['username'])
        except:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'],
                                                )
                login(request, user)
                return render(request, 'accounts/signup.html')
            else:
                return render(request, 'accounts/signup.html', {'error': 'Passwords must match!'})

        else:
            return render(request, 'accounts/signup.html', {'error': 'Username already exists!'})

    else:
        return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'accounts/login.html', )
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password!'})
    else:
        return render(request, 'accounts/login.html')
