from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from emp.views import sign_up, user_login, Management, clients1, clients2, clients3, ManagementDetails, logoutUser, save_data_test

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
    path('update-employee/<int:id>',save_data_test, name='update-employee'),
    path('test/',Management.as_view(), name='post'),
]