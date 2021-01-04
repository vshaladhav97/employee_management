"""emp_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from emp.views import sign_up, user_login, Management, clients, clients1, clients2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', sign_up, name='signup'),
    path('login/', user_login, name='login'),
    path('rest_client1/classproduct/', Management.as_view()),
    path('create/classproduct/', Management.as_view()),
    path('show/classproduct/', Management.as_view()),
    path('rest_client1/', clients),
    path('create/', clients1),
    path('show/', clients2),
    # re_path('classproduct/(?P<code>\w+)/$', ManagementUpdate.as_view()),
    path('test/',Management.as_view(), name='post'),
]
