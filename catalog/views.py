from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy, reverse

from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ContactDetailView(TemplateView):
    template_name = "catalog/contacts.html"


# def contact(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         print(name)
#         print(message)
#         # Здесь мы просто возвращаем простой ответ
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'contact.html')


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('catalog.can_publish_product'):
            return Product.objects.all()
        return Product.objects.filter(is_publish=True)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return redirect(reverse('catalog:catalog_list'))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_list')
    context_object_name = 'product'
