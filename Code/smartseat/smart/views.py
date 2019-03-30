from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def pwback(request):
    return render(request, 'pwback.html')

def pwset(request):
    return render(request, 'pwset.html')

def userindex(request):
    return render(request, 'userindex.html')
from smart.models import User
from django.http import HttpResponse
def userlogin(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
        else:
            return render(request, 'login.html')
        try:
            user = User.objects.get(id=username)
        except:
            return render(request, 'login.html')
        try:
            ps = User.objects.get(password=password)
        except:
            return render(request, 'login.html')
        if user:
            if user.password == password and ps.password == password:
                return redirect('/userindex')
            else:
                return redirect('/index')
        else:
             return HttpResponse('账号不存在')
