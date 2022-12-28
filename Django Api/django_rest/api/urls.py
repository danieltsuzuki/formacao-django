from django.urls import path
from .views import tecnologia_view, vaga_view, usuario_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('tecnologias/', tecnologia_view.TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>/', tecnologia_view.TecnologiaDetalhes.as_view(), name='tecnologia-detalhes'),
    path('vagas/', vaga_view.VagaList.as_view(), name='vaga-list'),
    path('vagas/<int:id>/', vaga_view.VagaDetalhes.as_view(), name='vaga-detalhes'),
    path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]