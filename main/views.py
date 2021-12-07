from django.shortcuts import render


# Create your views here.

# top-menu:
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def promotions(request):
    return render(request, 'main/promotions.html')

def catalog_product(request):
    return render(request, 'main/catalog-product.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def contacts(request):
    return render(request, 'main/contacts.html')
