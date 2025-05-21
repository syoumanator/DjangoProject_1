from .models import Category, Product


class CategoryService:
    @staticmethod
    def get_all_categories():

        return Category.objects.all()

    @staticmethod
    def get_products_from_category(category):

        return Product.objects.filter(category=category)
