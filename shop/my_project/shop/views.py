from django.shortcuts import render
from .models import Paint, Category

def catalog_view(request):
    # Запит до БД: дістаємо всі фарби, які є в наявності
    paints = Paint.objects.filter(in_stock=True)
    categories = Category.objects.all()
    
    context = {
        'paints': paints,
        'categories': categories,
    }
    return render(request, 'shop/catalog.html', context)