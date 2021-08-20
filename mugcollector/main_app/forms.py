from django.forms import ModelForm
from .models import Teatime


class TeatimeForm(ModelForm):
    class Meta:
        model = Teatime
        fields = ["date", "tea"]
