from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('promotions/', views.promotions, name="promotions"),
    path('catalog-product/', views.catalog_product, name="catalog_product"),
    path('gallery/', views.gallery, name="gallery"),
    path('contacts/', views.contacts, name="contacts")
]
