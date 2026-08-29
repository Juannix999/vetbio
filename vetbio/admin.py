from django.contrib import admin
from .models import Tutor, Mascota, Servicio, Atencion, DetalleAtencion

admin.site.register(Tutor)
admin.site.register(Mascota)
admin.site.register(Servicio)
admin.site.register(Atencion)
admin.site.register(DetalleAtencion)
