from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AvailableBus
 
@receiver(post_save, sender=AvailableBus)
def change_is_availaible_field(sender, instance, created, **kwargs):
    instance.bus.is_availaible = False
    instance.bus.save()
    if created:
        instance.bus.is_availaible = False
        instance.bus.save()
