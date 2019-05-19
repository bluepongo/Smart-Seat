from django.shortcuts import render
from django.shortcuts import redirect
from smart.models import User, Deskstate, Id
from django.http import HttpResponse
from django.contrib import messages
import random
import time
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
    sta = Deskstate.objects.values_list('state', flat=True)
    list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
    state = []
    for i in range(72):
        b = sta[i]
        d = list[b]
        state.append(d)
    username = request.session.get('user')
    ps1 = User.objects.get(id=username)
    na = ps1.name
    return render(request, 'userindex.html',{'name': na, 'state': state})

def userinformation(request):
    username = request.session.get('user')
    na = User.objects.filter(id = username)
    return render(request, 'userinformation.html', {'name': na})

def userinformation2(request):
    username = request.session.get('user')
    na = User.objects.filter(id=username)
    return render(request, 'userinformation2.html', {'name': na})

def userinformation3(request):
    username = request.session.get('user')
    na = User.objects.filter(id = username)
    return render(request, 'userinformation3.html', {'name': na})

def admindeel(request):
    username = request.session.get('user')
    id = request.POST.get('id')
    request.session['idnum'] = id
    st = Deskstate.objects.get(num=id)
    username = request.session.get('user')
    ps1 = User.objects.get(id=username)
    na = ps1.name
    tim = time.time()
    st.state = 0
    st.save()
    sta = Deskstate.objects.values_list('state', flat=True)
    list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
    state = []
    for i in range(72):
        b = sta[i]
        d = list[b]
        state.append(d)
    messages.success(request, "座位状态修改成功！")
    return render(request, 'admin.html', {'name': na, 'state': state, 'time': tim})

def shifang(request):
    username = request.session.get('user')
    id = request.session.get('idnum')
    st = Deskstate.objects.get(num=id)
    username = request.session.get('user')
    ps1 = User.objects.get(id=username)
    na = ps1.name
    tim = time.time()
    st.state = 0
    st.save()
    sta = Deskstate.objects.values_list('state', flat=True)
    list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
    state = []
    for i in range(72):
        b = sta[i]
        d = list[b]
        state.append(d)
    type = "badge badge-success"
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    id2 = str(a) + str(b) + str(c)
    n = Id.objects.get(id='1')
    n.num = id2
    n.save()
    messages.success(request, "欢迎下次使用！")
    return render(request, 'userindex.html', {'name': na, 'state': state, 'time': tim, 't': type, 'a' : id2,})

def deskstate(request):
    username = request.session.get('user')
    id = request.POST.get('id')
    request.session['idnum'] = id
    st = Deskstate.objects.get(num=id)
    username = request.session.get('user')
    ps1 = User.objects.get(id=username)
    na = ps1.name
    tim = time.time()
    if st.state != '0':
        sta = Deskstate.objects.values_list('state', flat=True)
        list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
        state = []
        for i in range(72):
            b = sta[i]
            d = list[b]
            state.append(d)
        type ="badge badge-warning"
        messages.success(request, "该 座 位 已 被 占 用 或 预 定，请 选 择 其 他 座 位！")
        return render(request, 'userindex.html', {'name': na, 'state': state,'t': type})
    else:
        st.state = 1
        st.save()
        sta = Deskstate.objects.values_list('state', flat=True)
        list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
        state = []
        for i in range(72):
            b = sta[i]
            d = list[b]
            state.append(d)
        mess = "座位预定成功，请尽快前往扫码！"
        type = "badge badge-success"
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        id2 = str(a)+str(b)+str(c)
        n = Id.objects.get(id='1')
        n.num = id2
        n.save()
        return render(request, 'desk.html', {'name': na, 'state': state, 'ms':mess, 't': type, 'a' : id2, 'time':tim})

def check(request):
    username = request.session.get('user')
    n = Id.objects.get(id='1')
    ido = n.num
    idn = request.POST.get('id')
    ps1 = User.objects.get(id=username)
    na = ps1.name
    if ido != idn:
        type = "badge badge-success"
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        id2 = str(a) + str(b) + str(c)
        request.session['id'] = id2
        n = Id.objects.get(id='1')
        n.num = id2
        n.save()
        mess = "座位预定成功，请尽快前往扫码！"
        messages.success(request, "验证码错误，请重新输入！")
        return render(request, 'desk.html', {'name': na, 't': type, 'ms':mess, 'a': id2})
    else:
        id = request.session.get('idnum')
        st = Deskstate.objects.get(num=id)
        st.state = 2
        st.save()
        return render(request, 'using.html', {'name': na,})

def er(request):
    username = request.session.get('user')
    ide = Id.objects.get(id='1')
    ido = ide.num
    ps1 = User.objects.get(id=username)
    na = ps1.name
    return render(request, '2.html', {'name': na, 'er': ido})

def xiuli(request):
    username = request.session.get('user')
    ps1= User.objects.get(id = username)
    na = ps1.name
    id = request.session.get('idnum')
    st = Deskstate.objects.get(num=id)
    st.state = '3'
    st.save()
    sta = Deskstate.objects.values_list('state', flat=True)
    list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
    state = []
    for i in range(72):
        b = sta[i]
        d = list[b]
        state.append(d)
    messages.success(request, "报修成功！")
    return render(request, 'userindex.html', {'name': na, 'state': state})

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
        ps1 = User.objects.get(id=username)
        ps = ps1.password
    except:
        return render(request, 'login.html', {'logine': logingerror})
    if user.id == username and ps == password:
        if username == '201830310222':
            sta = Deskstate.objects.values_list('state', flat=True)
            list = {'0': 'btn', '1': 'btn btn-primary', '2': 'btn btn-success', '3': 'btn btn-warning'}
            state = []
            for i in range(72):
                b = sta[i]
                d = list[b]
                state.append(d)
            ps1 = User.objects.get(id=username)
            na = ps1.name
            request.session['user'] = username
            return render(request, 'admin.html', {'name': na, 'state': state})
        else:
            sta = Deskstate.objects.values_list('state', flat=True)
            list = {'0':'btn', '1':'btn btn-primary', '2':'btn btn-success', '3': 'btn btn-warning'}
            state = []
            for i in range(72):
                b = sta[i]
                d = list[b]
                state.append(d)
            na = ps1.name
            request.session['user'] = username
            return render(request, 'userindex.html', {'name': na, 'state': state})
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



def wexin(request):
    """
    所有的消息都会先进入这个函数进行处理，函数包含两个功能，
    微信接入验证是GET方法，
    微信正常的收发消息是用POST方法。
    """
    # 这个WEIXIN_TOKEN是在测试号的配置页面中配置的，等会会讲到
    WEIXIN_TOKEN = 'kank'
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("error")

