from django.shortcuts import render, redirect
from .models import BietOn, MuonLam, BaiHoc
from django.core.paginator import Paginator

def index(request):
    return render(request, 'journal/index.html')

def bieton(request):
    if request.method == 'POST':
        nd = request.POST.get('NoiDung')
        if nd:
            BietOn.objects.create(NoiDung=nd)
        return redirect('bieton')
    items = BietOn.objects.all().order_by('-Ngay')
    paginator = Paginator(items, 6)  # 6 note / page
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'journal/bieton.html', {'page_obj': page_obj, 'type':'bieton'})

def muonlam(request):
    if request.method == 'POST':
        nd = request.POST.get('NoiDung')
        if nd:
            MuonLam.objects.create(NoiDung=nd)
        return redirect('muonlam')
    items = MuonLam.objects.all().order_by('-Ngay')
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'journal/muonlam.html', {'page_obj': page_obj, 'type':'muonlam'})

def baihoc(request):
    if request.method == 'POST':
        nd = request.POST.get('NoiDung')
        if nd:
            BaiHoc.objects.create(NoiDung=nd)
        return redirect('baihoc')
    items = BaiHoc.objects.all().order_by('-Ngay')
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'journal/baihoc.html', {'page_obj': page_obj, 'type':'baihoc'})
