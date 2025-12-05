# bancodedados20252/urls.py
from django.contrib import admin
from django.urls import path, include
from usuario_funcionalidades import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', views.login_usuario, name='login'),
    
    path('logout/', views.logout_usuario, name='logout'),
    
    path('', include('usuario_funcionalidades.urls')),
]