import os

from django.db import models
from django.dispatch import receiver


class Location(models.Model):
    location = models.CharField(max_length = 75, unique = True)

    def __str__(self):
        return f"{self.location}"


INTERVAL_CHOICES = [
    ('today', 'Today'),
    ('hourly', 'Hourly'),
    ('daily', 'Daily'),
]

class Forecast(models.Model):
    location =  models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateField()
    interval = models.CharField(max_length = 6, choices = INTERVAL_CHOICES, default = 'today')
    filename = models.FileField(upload_to = 'test/')

    def __str__(self):
        return f"Forecast for max wave height - {self.interval} in {self.location} on {self.date}"

@receiver(models.signals.post_delete, sender=Forecast)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """ Deletes file from filesystem

    when corresponding `Forecast` object is deleted.

    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Forecast)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes old file from filesystem

    when corresponding `MediaFile` object is updated

    with new file.

    """
    if not instance.pk:
        return False

    try:
        old_file = Forecast.objects.get(pk=instance.pk).file
    except Forecast.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)