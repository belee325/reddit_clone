from django.shortcuts import render

# Create your views here.
def signup(request):
    #{'info': info}
    if request.method == 'POST':
        #make a new user
        print('post workeD!')
        pass
    else:
        return render(request, 'accounts/signup.html')