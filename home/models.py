from datetime import time

from django.db import models


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

class ForecastTest(models.Model):
    location =  models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateField()
    interval = models.CharField(max_length = 6, choices = INTERVAL_CHOICES, default = 'today')
    filename = models.CharField(max_length = 100)

    def __str__(self):
        return f"Forecast for max wave height - {self.interval} in {self.location} on {self.date}"

