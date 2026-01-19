from django.forms import ModelForm
from .models import Series

class SeriesForm(ModelForm) :
    class meta :
        model = Series
    fields = ['name']