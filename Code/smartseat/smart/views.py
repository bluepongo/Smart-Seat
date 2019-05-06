from django.shortcuts import render
from django.shortcuts import redirect
from smart.models import User
from django.http import HttpResponse
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

def userinformation(request):
    username = request.session.get('user')
    na = User.objects.filter(id = username)
    return render(request, 'userinformation.html', {'name': na})

def userinformation2(request):
    username = request.session.get('user')
    na = User.objects.filter(id = username)
    return render(request, 'userinformation2.html', {'name': na})

def userinformation3(request):
    username = request.session.get('user')
    na = User.objects.filter(id = username)
    return render(request, 'userinformation3.html', {'name': na})

def table(request):
    return render(request, 'table.html')

def alterpassword(request):
    username = request.session.get('user')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1:
        if password2:
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request, 'userinformation3.html', locals())
            else:
                na = User.objects.get(id=username)
                password = na.password
                ps = User.objects.get(password=password)
                ps.password = password1
                ps.save()
                success = '密码修改成功,请在下方重新登录:'
                return render(request, 'login.html', locals())
        else:
            message = "请再次输入密码！"
            return render(request, 'userinformation3.html', locals())
    else:
        message = "密码不能为空！"
        return render(request, 'userinformation3.html', locals())

def userlogin(request):
        logingerror = "账号密码错误，请重新输入!!"
        notnull = "账号密码不能为空！"
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
        else:
            return render(request, 'login.html', {'null': notnull})
        try:
            user = User.objects.get(id=username)
        except:
            return render(request, 'login.html', {'logine': logingerror})
        try:
            ps = User.objects.get(password=password)
        except:
            return render(request, 'login.html', {'logine': logingerror})
        if user.id == username and ps.password == password:
            na = User.objects.filter(password = password)
            request.session['user'] = username
            return render(request, 'userindex.html', {'name': na})
        else:
            return render(request, 'login.html', {'logine': logingerror})


def userregister(request):
            username = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if username:
                if name:
                    if email:
                        if password1:
                            if password2:
                                if password1 != password2:
                                     message = "两次输入的密码不同！"
                                     return render(request, 'register.html', locals())
                                else:
                                    same_id_user = User.objects.filter(id=username)
                                    if same_id_user:  # 学号唯一
                                        message = '此学号已注册，请勿重复注册！'
                                        return render(request, 'register.html', locals())
                                    same_name_user = User.objects.filter(name=name)
                                    if same_name_user:  # 姓名唯一
                                        message = '此用户已注册，请勿重复注册！'
                                        return render(request, 'register.html', locals())
                                    same_email_user = User.objects.filter(email=email)
                                    if same_email_user:  # 邮箱地址唯一
                                        message = '该邮箱地址已被注册，请使用别的邮箱！'
                                        return render(request, 'register.html', locals())

                                    # 当一切都OK的情况下，创建新用户

                                    new_user = User.objects.create(id=username, name=name, email=email, password=password1)
                                    success = '注册成功！请在下方登录:'
                                    return render(request, 'login.html', locals())
                            else:
                                message = "请再次输入密码！"
                                return render(request, 'register.html', locals())
                        else:
                            message = "密码不能为空！"
                            return render(request, 'register.html', locals())
                    else:
                        message = "邮箱不能为空！"
                        return render(request, 'register.html', locals())
                else:
                    message = "姓名不能为空！"
                    return render(request, 'register.html', locals())
            else:
                message = "学号不能为空！"
                return render(request, 'register.html', locals())


