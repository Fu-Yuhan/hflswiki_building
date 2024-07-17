from django.contrib.auth.models import User
from loginportal.models import UserExtra
def getusername (method, value):
    if method == "email":
        usrobj=User.objects.filter(email=value).first()
        return usrobj.username
    elif method == "id":
        usr=UserExtra.objects.filter(id=value).first()
        usrobj=usr.BaseInfo().first()
        return usrobj.username
    else:
        return None