from django.urls import path,re_path 
from loginportal import views # 从自己的 app 目录引入 views 
urlpatterns = [ 
               path('', views.login),
               re_path('^signup/', views.signup)
               ]
