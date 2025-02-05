from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class ContactDetailView(TemplateView):
    template_name = "catalog/contacts.html"


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


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price')
    success_url = reverse_lazy('catalog:catalog_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price')
    success_url = reverse_lazy('catalog:catalog_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_list')