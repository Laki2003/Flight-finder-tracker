from django.forms import ModelForm
from .models import Let

class LetForm(ModelForm):
    class Meta:
        