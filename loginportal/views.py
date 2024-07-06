from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == 'admin' and password == 'admin':
                condition = True
                return render(request, 'login.html', {'username_correct': condition})
            else:
                return redirect('/index.php')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        useremail= request.POST.get('useremail')
        password = request.POST.get('password')
        return render(request, 'signup.html', {'username': username, 'useremail': useremail, 'password': password})