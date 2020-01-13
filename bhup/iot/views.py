from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

from .models import table
from .forms import ContactForm


def index(request):
    values=table.objects.all()
    data={'lis':values}
    return render(request, 'iot/index.html', data)



def addnew(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.save()
            return redirect('index')
    else:
        form=ContactForm()
    return render(request,'iot/addnew.html',{'form':form})
