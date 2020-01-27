from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item, Company


def list_item(request):
    items = Item.objects.all()
    companies = Company.objects.all()
    data = {
        'items': items,
        'companies': companies,
    }
    return render(request, "nyshop/list_item.html", data)

def list_company(request):
    companies = Company.objects.all()
    data = {
        'companies': companies,
    }
    return render(request, "nyshop/list_company.html", data)

def register_item(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        image = request.POST.get('image', None)
        info = request.POST.get('info', None)
        price = request.POST.get('price', None)
        remaining = request.POST.get('remaining', None)
        client = request.POST.get('client', None)
        if name and image and info and price and remaining and client:
            item = Item.objects.create(
                name=name,
                image=image,
                info=info,
                price=price,
                remaining=remaining,
                client=client,
            )
            return redirect(reverse('list_item', kwargs={'pk':item.pk}))
    return render(request, 'nyshop/register_item.html')

def detail_item(request, pk):
    item = Item.objects.get(pk=pk)
    data = {
        'item': item,
    }
    return render(request, 'nyshop/detail_item.html', data)

def register_company(request):
    if request.method == 'POST':
        companyName = request.POST.get('companyName', None)
        tel = request.POST.get('tel', None)
        address = request.POST.get('address', None)
        if companyName and tel and address:
            company = Company.objects.create(
                companyName=companyName,
                tel=tel,
                address=address,
            )
            return redirect(reverse('list_item', kwargs={'pk':company.pk}))
    return render(request, 'nyshop/register_company.html')

def detail_company(request, pk):
    company = Company.objects.get(pk=pk)
    data = {
        'company': company,
    }
    return render(request, "nyshop/detail_company.html", data)