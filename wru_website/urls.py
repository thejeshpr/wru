from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), {'template_name': 'registration/logged_out.html'},  name='logout'),
    path('admin/', admin.site.urls),
    path('', include('wru.urls')),
]
