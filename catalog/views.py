from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product


def contacts_view(request):
    return render(request, 'contacts.html')


def contact(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        print(name)
        print(message)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contact.html')


def catalog_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)