from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('Partogram_dets', views.Partogram_dets, name='Partogram_dets'),
    path('Section1', views.Section1_view, name='Section1'),
    path("Section2", views.Section2_view, name='Section2'),
    path("home", views.home, name="home")
]

