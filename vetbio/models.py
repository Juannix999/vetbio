from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Choices para los campos con opciones predefinidas
ESPECIE_CHOICES = [
    ('perro', 'Perro'),
    ('gato', 'Gato'),
    ('otro', 'Otro'),
]

TIPO_CHOICES = [
    ('consulta', 'Consulta'),
    ('vacuna', 'Vacuna'),
    ('procedimiento', 'Procedimiento'),
]

ESTADO_CHOICES = [
    ('abierta', 'Abierta'),
    ('pagada', 'Pagada'),
    ('anulada', 'Anulada'),
]

# Modelo Tutor
class Tutor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15) # Puedes añadir un validador en el formulario si es necesario

    def __str__(self):
        return self.nombre

# Modelo Mascota
class Mascota(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    fecha_nacimiento = models.DateField()

    def clean(self):
        # Regla de negocio: la fecha de nacimiento no debe ser futura
        if self.fecha_nacimiento and self.fecha_nacimiento > timezone.now().date():
            raise ValidationError('La fecha de nacimiento no puede ser en el futuro.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.tutor.nombre})"

# Modelo Servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def clean(self):
        # Regla de negocio: el precio base debe ser mayor o igual a 0
        if self.precio_base < 0:
            raise ValidationError('El precio base no puede ser negativo.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} (${self.precio_base})"

# Modelo Atencion
class Atencion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='atenciones')
    fecha = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierta')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Atención de {self.mascota.nombre} ({self.fecha})"

# Modelo DetalleAtencion (relación intermedia)
class DetalleAtencion(models.Model):
    atencion = models.ForeignKey(Atencion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    monto_linea = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Regla de negocio: precio_unitario se copia de Servicio.precio_base
        if not self.id:
            self.precio_unitario = self.servicio.precio_base
        
        # Regla de negocio: monto_linea se calcula automáticamente
        self.monto_linea = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

        # Regla de negocio: actualiza el monto_total de la atención
        self.atencion.monto_total = sum(
            detalle.monto_linea for detalle in self.atencion.detalleatencion_set.all()
        )
        self.atencion.save()

    def __str__(self):
        return f"{self.cantidad} de {self.servicio.nombre}"