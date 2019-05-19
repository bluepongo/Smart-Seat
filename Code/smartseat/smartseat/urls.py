"""smartsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smart.views import register,login,pwback,pwset, userlogin, userindex,userregister, userinformation, userinformation2,userinformation3,alterpassword,deskstate,check,wexin,er,xiuli,admindeel,shifang
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('register/',register, name='register'),
    path('pwback/',pwback, name='pwback'),
    path('pwset/',pwset, name='pwset'),
    path('userlogin/', userlogin),
    path('userindex/', userindex, name='userindex'),
    path('userregister/', userregister, name='userregister'),
    path('userinformation/', userinformation, name='userinformation'),
    path('userinformation2/', userinformation2, name='userinformation2'),
    path('userinformation3/', userinformation3, name='userinformation3'),
    path('alterpassword/', alterpassword),
    path('deskstate/', deskstate, name='deskstate'),
    path('check/', check),
    path('weixin/', wexin, name='wexin'),
    path('er/', er),
    path('xiuli/', xiuli, name='xiuli'),
    path('admindeel/', admindeel, name='admindeel'),
    path('shifang/', shifang, name='shifang')
]
