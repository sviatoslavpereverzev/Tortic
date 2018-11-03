from django.urls import path
from torticapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('order', views.order, name='order'),
    path('reviews', views.reviews, name='reviews'),
    path('stuffing', views.stuffing, name='stuffing'),
    path('contacts', views.contacts, name='contacts'),
]
