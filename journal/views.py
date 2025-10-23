from django.shortcuts import render, redirect
from .models import BietOn, MuonLam, BaiHoc

def index(request):
    return render(request, 'index.html')

def bieton(request):
    if request.method == 'POST':
        NoiDung = request.POST.get('NoiDung')
        if NoiDung:
            BietOn.objects.create(NoiDung=NoiDung)
        return redirect('bieton')
    data = BietOn.objects.all().order_by('-id')
    return render(request, 'bieton.html', {'data': data})

def muonlam(request):
    if request.method == 'POST':
        NoiDung = request.POST.get('NoiDung')
        if NoiDung:
            MuonLam.objects.create(NoiDung=NoiDung)
        return redirect('muonlam')
    data = MuonLam.objects.all().order_by('-id')
    return render(request, 'muonlam.html', {'data': data})

def baihoc(request):
    if request.method == 'POST':
        NoiDung = request.POST.get('NoiDung')
        if NoiDung:
            BaiHoc.objects.create(NoiDung=NoiDung)
        return redirect('baihoc')
    data = BaiHoc.objects.all().order_by('-id')
    return render(request, 'baihoc.html', {'data': data})
