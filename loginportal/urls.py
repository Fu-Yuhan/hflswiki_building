from django.urls import path,re_path 
from loginportal import views # 从自己的 app 目录引入 views 
urlpatterns = [ 
               path('login/', views.login),
               path('login/signin', views.signup)
               ]
