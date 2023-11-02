from django.forms import ModelForm
from .models import Logging

class LoggingForm(ModelForm):
    class Meta:
        model = Logging
        fields = ['date', 'opened', 'genre']