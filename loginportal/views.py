from django.shortcuts import render, redirect
# 认证模块
from django.contrib import auth
from loginportal import models
# 对应数据库
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'GET':
        next=request.GET.get("next")
        if next:
            return render(request, 'login.html', {'next':next}))

        return render(request, 'login.html')
    elif request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('pwd')
            #if not username:
                    #return render(request, 'login.html', {'error': '用户名不能为空'})
            #if not password:
                    #return render(request, 'login.html', {'error': '密码不能为空'})
            print(username)
            print(password)
            #valid_num = request.POST.get("valid_num")
            #keep_str = request.session.get("keep_str")
            user_obj = auth.authenticate(username=username, password=password)
            #print(user_obj.username)
            #if valid_num.upper() != keep_str.upper():
            #    return render(request, 'login.html', {'error': '验证码错误'})
                #验证码



            if not user_obj :
                user_obj = auth.authenticate(email=username, password=password)
                #邮箱登录


            if not user_obj :
                return render(request, 'login.html', {'error': '用户名或密码错误'})
                #用户名或密码验证
                obj = models.UserExtra.objects.filter(BaseInfo=User_obj).first()
                if obj.disabled  :
                    return render(request, 'login.html', {'error': '该用户已被封号'})

                path = request.GET.get("next") or "/index/"
                print(path)

                auth.login(request, user_obj)
                return Http



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        useremail= request.POST.get('useremail')
        password = request.POST.get('password')
        if  User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': '用户名已存在'})
        obj = User.objects.create_user (username=username, password=password, email=useremail)
        models.UserExtra.objects.create(BaseInfo = obj, sth_to_say = "这个人很懒，什么也没有留下", level = 0, coin = 0, type="")
        auth.login(request, obj)
        return render(request, 'signup.html', {'success': '注册成功'})