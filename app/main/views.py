from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Series
from .forms import SeriesForm

# Create your views here.
def get_input(request) :
    if request.method == 'POST' :
        form = SeriesForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('result')
    else:
        form = SeriesForm()    
    return render(request,'input.html',{'form':form})

def result(request) :
    series = Series.objects.all()
    return render(request,'result.html',{'series' : series})