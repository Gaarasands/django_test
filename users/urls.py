from django.urls import path,include
from users import views

app_name = "users"
urlpatterns = [
    path('add/',views.addUser, name= "add"),
    path('get/<int:id>/',views.getById, name= "get"),
    path('auth/',views.authApi)

]