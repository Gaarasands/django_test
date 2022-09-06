from django.urls import path
from recipe import views

urlpatterns = [
    path('get/<int:id>/',views.getById),
    path('add/',views.addrecipe),
    path('delete/',views.deleterecipe)
]
