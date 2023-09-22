from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.TextField(max_length=250)
    slug = models.SlugField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
