import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from vetbio.models import Tutor, Mascota, Servicio, Atencion, DetalleAtencion

class Command(BaseCommand):
    help = 'Genera datos de ejemplo para la aplicación VetBio.'

    def handle(self, *args, **options):
        self.stdout.write('Eliminando datos antiguos...')
        DetalleAtencion.objects.all().delete()
        Atencion.objects.all().delete()
        Servicio.objects.all().delete()
        Mascota.objects.all().delete()
        Tutor.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Datos antiguos eliminados.'))

        fake = Faker('es_ES')

        with transaction.atomic():
            # Crear 10 tutores
            tutores = []
            for _ in range(10):
                tutor = Tutor.objects.create(
                    nombre=fake.name(),
                    email=fake.email(),
                    telefono=fake.phone_number()
                )
                tutores.append(tutor)
            self.stdout.write(self.style.SUCCESS(f'Creados {len(tutores)} tutores.'))

            # Crear 5 servicios básicos
            servicios_data = [
                {'nombre': 'Consulta General', 'precio_base': 25000, 'tipo': 'consulta'},
                {'nombre': 'Vacuna Antirrábica', 'precio_base': 15000, 'tipo': 'vacuna'},
                {'nombre': 'Limpieza Dental', 'precio_base': 50000, 'tipo': 'procedimiento'},
                {'nombre': 'Desparasitación', 'precio_base': 10000, 'tipo': 'vacuna'},
                {'nombre': 'Cirugía Menor', 'precio_base': 80000, 'tipo': 'procedimiento'},
            ]
            servicios = [Servicio.objects.create(**data) for data in servicios_data]
            self.stdout.write(self.style.SUCCESS(f'Creados {len(servicios)} servicios.'))

            # Crear mascotas (1-3 por tutor)
            mascotas = []
            for tutor in tutores:
                num_mascotas = random.randint(1, 3)
                for _ in range(num_mascotas):
                    fecha_nacimiento = fake.date_of_birth(minimum_age=1, maximum_age=10)
                    mascota = Mascota.objects.create(
                        tutor=tutor,
                        nombre=fake.first_name(),
                        especie=random.choice(['perro', 'gato', 'otro']),
                        fecha_nacimiento=fecha_nacimiento
                    )
                    mascotas.append(mascota)
            self.stdout.write(self.style.SUCCESS(f'Creadas {len(mascotas)} mascotas.'))

            # Crear 30 atenciones
            atenciones = []
            for _ in range(30):
                atencion = Atencion.objects.create(
                    mascota=random.choice(mascotas),
                    fecha=fake.date_this_year(),
                    estado=random.choice(['abierta', 'pagada', 'anulada'])
                )
                
                # Crear 1-3 detalles por atención
                num_detalles = random.randint(1, 3)
                for _ in range(num_detalles):
                    servicio = random.choice(servicios)
                    cantidad = random.randint(1, 2)
                    DetalleAtencion.objects.create(
                        atencion=atencion,
                        servicio=servicio,
                        cantidad=cantidad,
                    )
                atenciones.append(atencion)
            self.stdout.write(self.style.SUCCESS(f'Creadas {len(atenciones)} atenciones.'))

        self.stdout.write(self.style.SUCCESS('¡Datos de ejemplo generados con éxito!'))