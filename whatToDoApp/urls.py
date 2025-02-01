from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskHome.as_view(), name='home'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('update/<int:id>/', views.TaskUpdate.as_view(), name='update'),
    path('delete/<int:id>/', views.TaskDelete.as_view(), name='delete'),
    path('register/', views.create_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
]