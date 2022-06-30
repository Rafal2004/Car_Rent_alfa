
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_car, name="add_car"),
    path('rent/', views.rent_car, name="rent_car"),
    path('detail/<int:pk>', views.detail_car, name="detail_car"),
    path('myaccount/<views>', views.my_account, name="my_account"),
    path('myaccount/edit/<int:pk>', views.edit_car, name="edit_car"),

]
