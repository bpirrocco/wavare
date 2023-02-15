from django  import forms

from .models import Location, Forecast

CHOICES = [
    ('today', 'Today'),
    ('hourly', 'Hourly'),
    ('daily', 'Daily')
]

class ForecastForm(forms.Form):
    model_choice = forms.ChoiceField(
        choices = CHOICES,
        initial = 0)

