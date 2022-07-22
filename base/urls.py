from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path("student/", StudentAPI.as_view(), name="api-student"),
    # path('create_student/', views.post_student, name='create_student'),
    # path('update_student/<int:id>/', views.update_student, name='update_student'),
    # path('delete_student/<id>/', views.delete_student, name='delete_student'),
    path('get_book/', views.get_book, name='get_book'),
]
