from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from .views import catalog_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.contacts_view, name='contacts'),
    path('', catalog_list, name="catalog_list"),
    path('products/<int:pk>/', product_detail, name="product_detail"),
]