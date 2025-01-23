from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        category, _ = Category.objects.get_or_create(name='Категория1')


        products = [
            {'name': 'Продукт1', 'description': 'Описание 1', 'price': 1, 'category': category},
            {'name': 'Продукт2', 'description': 'Описание 2', 'price': 1, 'category': category},
            {'name': 'Продукт3', 'description': 'Описание 3', 'price': 1, 'category': category},
        ]

        # Создание продуктов
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                print(f'Создан продукт: {product}')
            else:
                print(f'Продукт с названием {product_data["name"]} уже существует')

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {product}'))
            else:
                self.stdout.write(self.style.WARNING(f'{product} already exists: '))
