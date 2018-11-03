from django.shortcuts import render
from torticapp.models import *


def home(request):
    context = {}
    context['slides'] = Slides.objects.filter(show=True).order_by('order')
    context['categories'] = Category.objects.order_by('order')
    context['reviews'] = Reviews.objects.order_by('order')[:5]
    return render(request, 'home.html', context)


def gallery(request):
    context = {}
    context['cakes'] = Cake.objects.all()
    context['categories'] = Category.objects.all()
    return render(request, 'gallery.html', context)


def stuffing(reguest):
    context = {}
    context['stuffing'] = Stuffing.objects.all()
    return render(reguest, 'stuffing.html', context)


def reviews(request):
    context = {}
    context['reviews'] = Reviews.objects.all()
    return render(request, 'reviews.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def order(request):
    return render(request, 'order.html')
