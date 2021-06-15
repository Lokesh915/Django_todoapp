from django.urls import path,include
from todoapp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('addtodo/', views.addtodo, name='add'),
    path('delete/<int:id>/', views.deletetodo, name='del'),
]
