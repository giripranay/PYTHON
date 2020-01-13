from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import DataForm
import requests
from .models import Bin1,Bin2,Bin3
from django.utils.dateparse import parse_datetime


def index(request):
    values=Bin1.objects.all()

    count = len(values)
    URL="https://io.adafruit.com/api/v2/giripranay/feeds/bin1/data?X-AIO-Key=a68f2ef379d4470780176f536af0f462"
    r = requests.get(url=URL)
    new=r.json()
    count2=len(new)
    if(count!=count2):
        for j in range(0,count2-count):
            i=new[count2-count-j-1]
            temp_date = parse_datetime(i['created_at'])
            obj=Bin1(value=i['value'],date=temp_date)
            obj.save()
    values=Bin1.objects.all()
    count = len(values)
    latest=Bin1.objects.all().order_by('-id')[0]
    data={'lis':new,'count':count,'count2':count2,'values':values,'latest':latest}

    return render(request,'IOT_app/index.html',data)

def data(request):
    if request.method =='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.save()
            return redirect('index')
    else:
        form=DataForm()
    return render(request,'IOT_app/data.html',{'form':form})


def bin1(request):
    bills_list=Bin1.objects.all().order_by('-id')
    data={'lis':bills_list,}
    return render(request,'IOT_app/bin1.html',data)


def bin2(request):
    bills_list=Bin2.objects.all().order_by('-id')
    data={'lis':bills_list,}
    return render(request,'IOT_app/bin2.html',data)

def bin3(request):
    bills_list=Bin3.objects.all().order_by('-id')
    data={'lis':bills_list,}
    return render(request,'IOT_app/bin3.html',data)

def maps(request):
    data={}
    return render(request,'IOT_app/maps.html',data)

def google(request):
    data={}
    return render(request,'IOT_app/google.html',data)
