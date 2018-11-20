from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        print(user_name)
        print(pass_word)
        user = authenticate(user_name, pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        return render(request, 'index.html')
    elif request.method == 'GET':
        return render(request, 'login.html', {})