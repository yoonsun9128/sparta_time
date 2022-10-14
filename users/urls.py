from django.urls import path ,include
from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    
]