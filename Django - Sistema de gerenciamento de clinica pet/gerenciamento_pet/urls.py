from django.contrib import admin
from django.urls import path, include
from app.views import autenticacao_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', autenticacao_views.login_usuario, name='login'),
    path('logout', autenticacao_views.deslogar_usuario, name='logout'),
]
