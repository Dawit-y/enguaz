from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import AvailableBus, Seat
 
@receiver(post_save, sender=AvailableBus)
def change_is_availaible_field(sender, instance, created, **kwargs):
    instance.bus.is_availaible = False
    instance.bus.save()
    if created:
        instance.bus.is_availaible = False
        instance.bus.save()

@receiver(pre_delete, sender=AvailableBus)
def change_is_listed_and_is_availaible(sender, instance, **kwargs):
    instance.bus.is_availaible = True
    instance.bus.is_listed = False
    instance.bus.save()


@receiver(post_save, sender=Seat)
def check_if_the_bus_is_full(sender, instance, created, **kwargs):
    num_of_seats = instance.bus.num_of_seats
    bus = instance.bus
    occupied_seats = bus.seat_set.all().count()
    if num_of_seats == occupied_seats:
        availaible_bus = bus.list_of_buses.all()
        for item in availaible_bus:
            item.delete()
    
    