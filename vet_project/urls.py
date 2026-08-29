from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vetbio.views import TutorViewSet, ServicioViewSet, MascotaViewSet, AtencionViewSet

router = routers.DefaultRouter()
router.register(r'tutores', TutorViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'atenciones', AtencionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
