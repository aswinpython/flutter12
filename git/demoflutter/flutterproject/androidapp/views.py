from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AndroidForm
from.models import Android


# Create your views here.
def list(request):
    android=Android.objects.all()
    context={'android_list':android}
    return render(request,'index.html',context)
def detail(request,android_id):
    android=Android.objects.get(id=android_id)
    return render(request,'detail.html',{'android':android})
def add_app(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        android=Android(name=name,desc=desc,year=year,img=img)
        android.save()
    return render(request,'add.html')
def update(request,id):
    android=Android.objects.get(id=id)
    form=AndroidForm(request.POST or None,request.FILES,instance=android)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'android':android})
def delete(request,id):
    if request.method=="POST":
        android=Android.objects.get(id=id)
        android.delete()
        return redirect('/')
    return render(request,'delete.html')