from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import DetalleAtencion, Atencion


def recalc_monto(atencion):
    total = atencion.detalleatencion_set.aggregate(total=Sum('monto_linea'))['total'] or 0
    # Use update to avoid recursive saves
    Atencion.objects.filter(pk=atencion.pk).update(monto_total=total)


@receiver(post_save, sender=DetalleAtencion)
@receiver(post_delete, sender=DetalleAtencion)
def detalle_changed(sender, instance, **kwargs):
    if instance.atencion_id:
        recalc_monto(instance.atencion)
