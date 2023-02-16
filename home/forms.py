from datetime import datetime

from django  import forms

from .models import Location, Forecast

CHOICES = [
    ('today', 'Today'),
    ('hourly', 'Hourly'),
    ('daily', 'Daily')
]

# format_data = "%Y-%m-%dT%H:%M:%S.%fZ"
class ForecastForm(forms.Form):
    location = forms.CharField(widget=forms.HiddenInput(), initial='Nazaré')
    date = forms.DateField(widget=forms.HiddenInput(), initial="2023-02-10")
    interval = forms.ChoiceField(
        choices = CHOICES,
        initial = 0)

