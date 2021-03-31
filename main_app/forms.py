from django.forms import ModelForm
from .models import Sugar

class SugarForm(ModelForm):
    class Meta:
        model = Sugar
        fields = ['type','amount']
