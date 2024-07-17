from django.shortcuts import render, redirect
from django.http import HttpResponse
# 认证模块
from django.contrib import auth
from loginportal import models
# 对应数据库
from django.contrib.auth.models import User
from loginportal.function import getusername
# Create your views here.
def login(request):
    if request.method == 'GET':
        next=request.GET.get("next")
        if next:
            request.session["next"] = next
            return render(request, 'login.html', {'next':next})

        return render(request, 'login.html')
    elif request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('pwd')
            if not username:
                    return render(request, 'login.html', {'error': '用户名不能为空'})
            if not password:
                    return render(request, 'login.html', {'error': '密码不能为空'})
            print(username)
            print(password)
            #valid_num = request.POST.get("valid_num")
            #keep_str = request.session.get("keep_str")
            user_obj = auth.authenticate(username=username, password=password)
            #print(user_obj.username)
            #if valid_num.upper() != keep_str.upper():
            #    return render(request, 'login.html', {'error': '验证码错误'})
                #验证码
            if user_obj :
                print("用户名密码正确")


            if not user_obj :
                obj = User.objects.filter(email=username).first()
                if obj :
                    print(obj.username)
                    user_obj = auth.authenticate(username=obj.username, password=password)
                #邮箱登录
                if user_obj :
                    print("邮箱登录成功")

                if not user_obj :
                    print("邮箱登录失败")


            if not user_obj :
                return render(request, 'login.html', {'error': '用户名或密码错误'})
                #用户名或密码验证

            if user_obj.is_active == False :
                return render(request, 'login.html', {'error': '该用户已被封号'})

                #path = request.session.get('next') or "/index/"
                #del request.session["next"]
            print("登陆成功")

            auth.login(request, user_obj)
            return HttpResponse("登录成功")



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        useremail= request.POST.get('useremail')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(useremail)
        if  User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': '用户名已存在'})
        if password != password2:
            return render(request, 'signup.html', {'error': '两次密码不一致'})
        obj = User.objects.create_user (username=username,  email= useremail, password=password, is_active=True)
        models.UserExtra.objects.create(BaseInfo = obj, sth_to_say="", level=0, coin=0, type="普通用户")
        print(obj.email)
        auth.login(request, obj)
        return render(request, 'signup.html', {'success': '注册成功'})
def password_reset(request):
    if request.method == 'GET':
        return render(request, 'password_reset.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        # 这里需要添加密码重置的逻辑
        username = getusername("email",email)
        OK=1
        # ...
        if OK==1:

            return render(request, 'password_reset.html', {'success': '重置成功'})

    return render(request, 'password_reset.html', {'error': '验证码错误'})






