from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin/', views.Signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
