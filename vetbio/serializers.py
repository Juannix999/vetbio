from rest_framework import serializers
from .models import Tutor, Mascota, Servicio, Atencion, DetalleAtencion

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class DetalleAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleAtencion
        fields = '__all__'

class AtencionSerializer(serializers.ModelSerializer):
    detalles = DetalleAtencionSerializer(source='detalleatencion_set', many=True, read_only=True)

    class Meta:
        model = Atencion
        fields = ['id', 'mascota', 'fecha', 'estado', 'monto_total', 'detalles']
