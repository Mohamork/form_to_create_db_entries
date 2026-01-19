from django.forms import ModelForm
from .models import Series

class SeriesForm(ModelForm) :
    class Meta :
        model = Series
        fields = ['name']