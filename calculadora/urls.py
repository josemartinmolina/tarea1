from django.urls import include,path
from rest_framework import routers
from . import views
from .views import RetoListView, retoDetailView, RetoCreateView, RetoUpdateView, RetoDeleteView

router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)

urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'),
    path('procesamiento', views.procesamiento, name='procesamiento'),
    path('lista',views.lista,name='lista'),
    path('score',views.score,name='score'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d, name='usuarios_d'),
    path('login', views.login, name='login'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('valida_usuario',views.valida_usuario,name='valida_usuario'),
    path('grafica',views.grafica,name='grafica'),
    path('barras',views.barras,name='barras'),
    path('nuevoreto', views.nuevoreto, name='nuevoreto'),
    path('nuevojugador', views.nuevojugador, name='nuevojugador'),
    path('listaretos', RetoListView.as_view(), name='retos'),
    path('detallereto/<int:pk>', retoDetailView.as_view(), name='detallereto'), 
    path('reto/add', RetoCreateView.as_view(), name='add_reto'), 
    path('reto/<int:pk>', RetoUpdateView.as_view(), name='edit_reto'),
    path('reto/delete/<int:pk>', RetoDeleteView.as_view(), name='delete_reto'),
    path('aboutus', views.aboutus, name="aboutus"),
]