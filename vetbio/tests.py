from django.test import TestCase
from .models import Tutor, Mascota, Servicio, Atencion, DetalleAtencion
from datetime import date
from django.core.exceptions import ValidationError

class ModelTests(TestCase):
    def test_fecha_nacimiento_no_futura(self):
        tutor = Tutor.objects.create(nombre='A', email='a@example.com', telefono='123')
        mascota = Mascota(tutor=tutor, nombre='M', especie='perro', fecha_nacimiento=date(3000,1,1))
        with self.assertRaises(ValidationError):
            mascota.full_clean()

    def test_monto_total_calculado(self):
        tutor = Tutor.objects.create(nombre='A', email='a2@example.com', telefono='123')
        mascota = Mascota.objects.create(tutor=tutor, nombre='M', especie='gato', fecha_nacimiento=date(2020,1,1))
        servicio = Servicio.objects.create(nombre='S', precio_base=100, tipo='consulta')
        at = Atencion.objects.create(mascota=mascota)
        DetalleAtencion.objects.create(atencion=at, servicio=servicio, cantidad=2)
        at.refresh_from_db()
        self.assertEqual(at.monto_total, 200)
