from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product
def home_view(request):
    return render(request, 'home.html')


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
    product = Product.objects.all()
    context = {
        "products": product,
    }
    return render(request, 'product_list.html', context=context)
