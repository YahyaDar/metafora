from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('faculty_register', views.register_faculty, name='register_faculty'),
    path('student_register', views.register_student, name='register_student'),
    path('index', views.index, name='index'),
]
