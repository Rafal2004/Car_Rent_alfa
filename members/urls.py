
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
 

urlpatterns = [
    path('login/',  views.login_user, name='login_user'),
    path('logout/',  views.logout_user, name='logout_user'),
    path('register/',  views.register_user, name='register_user'),
    path('myaccount/edit', views.edit_account, name='edit_account'),
    path('myaccount/edit/change-password', views.change_password, name='change_password')
]
