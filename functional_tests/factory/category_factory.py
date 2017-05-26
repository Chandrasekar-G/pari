import factory
from category.models import Category
from django.utils.text import slugify


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Things we do"
    slug = "things-we-do"
    description = "The world of rural labour"
    order = 1
