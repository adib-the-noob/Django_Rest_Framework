from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_student/', views.post_student, name='create_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('get_book/', views.get_book, name='get_book'),
]
