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
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from emp.views import sign_up, user_login, Management, clients, clients1, clients2, clients3, ManagementDetails, logoutUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', sign_up, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', logoutUser, name="logout"),
    path('rest_client1/classproduct/', Management.as_view()),
    path('',login_required(clients2), name='show'),
    path('<int:id>', clients2),
    path('classproduct/', login_required(Management.as_view())),
    path('classproduct/<int:id>', ManagementDetails.as_view()),
    path('create/', login_required(clients1)),
    path('create/classproduct/', Management.as_view()),   
    path('create/classproduct/<int:addressdetails>', ManagementDetails.as_view()),
    path('update/', clients3),
    path('update/<int:id>', clients3),
    path('update/classproduct/', Management.as_view()),
    path('update/classproduct/<int:id>', ManagementDetails.as_view()),
    path('rest_client1/', clients),
    
    
    # path('test1/', logins),
    path('test/',Management.as_view(), name='post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
