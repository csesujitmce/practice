from django.urls import path
from todo import views

urlpatterns = [
    path('',views.home_page, name='home'),
    path('remove/<int:id>/', views.delete_todo_item, name='del'),
]
